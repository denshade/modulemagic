import sys
import csv
import os
import subprocess
from shutil import copyfile


def writeoutput(output : str):
    f = open("current.csv", 'w')
    f.write(output)
    f.close()


class resource:
    def __init__(self, filename):
        self.filename = filename


def proc(myresource : resource, other_resource : resource):
    print("Calling " + other_resource.filename, myresource.filename)
    if other_resource.filename.endswith(".py"):
        output = subprocess.checkoutput(["python", other_resource.filename, myresource.filename])
    else:
        output = subprocess.checkoutput([other_resource.filename, myresource.filename])
    writeoutput(output)


class FileResource(resource):
    def exec(self, dest_resource: resource):
        if type(dest_resource) == FileResource:
            print("Copied file from " + self.filename, dest_resource.filename)
            copyfile(self.filename, dest_resource.filename)
        if type(dest_resource) == TProcessResource:
            print("Watch out, trying to call a regular file with a table proc!")
            if dest_resource.filename.endswith(".py"):
                subprocess.checkoutput(["python", dest_resource.filename, self.filename])
            else:
                subprocess.checkoutput([dest_resource.filename, self.filename])
        if type(dest_resource) == ProcessResource:
            proc(self, dest_resource)


def row_to_param(row):
    str = ""
    for key in row:
        str += "--"+key+"="+row[key]
    return str


class TableResource(resource):
    def exec(self, dest_resource: resource):
        if type(dest_resource) == FileResource or type(dest_resource) == TableResource:
            print("Copied file table " + self.filename + " to " + dest_resource.filename)
            copyfile(self.filename, dest_resource.filename)
        if type(dest_resource) == TProcessResource:
            proc(self, dest_resource)
        if type(dest_resource) == ProcessResource:
            reader = csv.DictReader(self.filename)
            for row in reader:
                print("Calling " + dest_resource.filename + row_to_param(row))
                if dest_resource.filename.endswith(".py"):
                    output = subprocess.checkoutput(["python", dest_resource.filename, row_to_param(row)])
                else:
                    output = subprocess.checkoutput([dest_resource.filename, row_to_param(row)])
                writeoutput(output)


class ProcessResource(resource):
    def exec(self, dest_resource: resource):
        #use current.csv
        sourcefile = "current.csv"
        if type(dest_resource) == FileResource:
            print("Copied file from " + sourcefile + " " + dest_resource.filename)
            copyfile(self.sourcefile, dest_resource.filename)
        if type(dest_resource) == TProcessResource:
            print("Watch out, trying to call a regular file with a table proc!")
            if dest_resource.filename.endswith(".py"):
                subprocess.checkoutput(["python", dest_resource.filename, sourcefile])
            else:
                subprocess.checkoutput([dest_resource.filename, sourcefile])
        if type(dest_resource) == ProcessResource:
            print("Calling " + dest_resource.filename + sourcefile)
            if dest_resource.filename.endswith(".py"):
                output = subprocess.checkoutput(["python", dest_resource.filename, sourcefile])
            else:
                output = subprocess.checkoutput([dest_resource.filename, sourcefile])
            writeoutput(output)



class TProcessResource(resource):
    def exec(self, dest_resource: resource):
        #use current.csv
        sourcefile = "current.csv"
        if type(dest_resource) == FileResource:
            print("Copied file from " + sourcefile + " " + dest_resource.filename)
            copyfile(self.sourcefile, dest_resource.filename)
        if type(dest_resource) == TProcessResource:
            if dest_resource.filename.endswith(".py"):
                subprocess.checkoutput(["python", dest_resource.filename, sourcefile])
            else:
                subprocess.checkoutput([dest_resource.filename, sourcefile])
        if type(dest_resource) == ProcessResource:
            print("Calling " + dest_resource.filename + sourcefile)
            if dest_resource.filename.endswith(".py"):
                output = subprocess.checkoutput(["python", dest_resource.filename, sourcefile])
            else:
                output = subprocess.checkoutput([dest_resource.filename, sourcefile])
            writeoutput(output)


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
# from file to process = feed file as parameter to process.
# from file to tprocess = impossible. Warn.

# from table to file = stores the csv to a file.
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
