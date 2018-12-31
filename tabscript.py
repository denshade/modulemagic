import sys
import csv
import os
from subprocess import call
from shutil import copyfile



class resource:
    def __init__(self, filename):
        self.filename = filename

class FileResource(resource):
    def exec(self, other_resource: resource):
        if type(other_resource) == FileResource:
            print("Copied file from " + self.filename, other_resource.filename)
            copyfile(self.filename, other_resource.filename)
        if type(other_resource) == TProcessResource:
            print("Watch out, trying to call a regular file with a table proc!")
            if other_resource.filename.endswith(".py"):
                call(["python", other_resource.filename, self.filename])
            else:
                call([other_resource.filename, self.filename])
        if type(other_resource) == ProcessResource:
            print("Calling " + other_resource.filename + " " + self.filename)
            if other_resource.filename.endswith(".py"):
                call(["python", other_resource.filename, self.filename])
            else:
                call([other_resource.filename, self.filename])



class TableResource(resource):
    def exec(self, other_resource: resource):
        if type(other_resource) == TProcessResource:
            print("Calling " + other_resource.filename, self.filename)
            if other_resource.filename.endswith(".py"):
                call(["python", other_resource.filename, self.filename])
            else:
                call([other_resource.filename, self.filename])


class ProcessResource(resource):
    def exec(self, other_resource: resource):
        pass


class TProcessResource(resource):
    def exec(self, other_resource: resource):
        pass


def parseresource(resource: str) -> resource:
    if resource.startswith("file://"):
        filename = resource[len("file://"):]
        return FileResource(filename)

    if resource.startswith("table://"):
        filename = resource[len("table://"):]
        return TableResource(filename)

    if resource.startswith("proc://"):
        filename = resource[len("proc://"):]
        return ProcessResource(filename)
    if resource.startswith("tproc://"):
        filename = resource[len("tproc://"):]
        return TProcessResource(filename)
    sys.stderr.write("Unknown resource " + resource)
    sys.exit(4)


# from file to file = copy file to file.
# from file to table = impossible
# from file to process = pipe data from file to process as input.
# from file to tprocess = impossible.

# from table to file = stores the tsv to a file.
# from table to table = copy
# from table to process = for each row in the process
# from table to tprocess = process gets the file.

# from proc to file = stores output to a file.
# from proc to table = stores output to a tsv file.
# from proc to process = pipe output to next file
# from proc to tprocess = pipe output to a tprocess. Assume the output is a table.

# from tproc to file = stores output to a file.
# from tproc to table = stores output to a tsv file.
# from tproc to process = pipe output to next file
# from tproc to tprocess = pipe output to a tprocess.


def execute_resource_chain(resource_chain):
    for i in range(0, len(resource_chain) - 1):
        from_chain_resource = resource_chain[i]
        to_chain_resource = resource_chain[i + 1]
        from_chain_resource.exec(to_chain_resource)

def parseline(line: str):
    if line == "":
        return
    line = line.replace("\n", "")
    lineparts = line.split(" ")
    if not lineparts[0] == "FROM":
        sys.stderr.write("Line doesn't start with FROM " + line)
        sys.exit(3)
    resource_chain = []
    for i in range(1, len(lineparts)):
        if i % 2 == 0 and lineparts[i] != "TO":
            sys.stderr.write("Expected TO clause at parameter " + str(i) + " but got " + lineparts[i])
            sys.exit(3)
        elif i % 2 == 1:
            resource_chain.append(parseresource(lineparts[i]))

    execute_resource_chain(resource_chain)


if len(sys.argv) != 2:
    print("""\
            Usage: tablescript <recipe.tab>
      """)
    sys.exit(2)
inputFile = sys.argv[1]
working_dir = os.path.dirname(os.path.realpath(__file__))
with open(inputFile, 'r') as recipefile:
    for line in recipefile.readlines():
        parseline(line)
