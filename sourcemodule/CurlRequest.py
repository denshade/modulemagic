__author__ = 'Lieven'

import sys
import csv
import urllib.request



def execute(tuple):
    Url = tuple["URL"]
    DestinationFile = tuple["DestinationFile"]
    response = urllib.request.urlopen(Url)
    data = response.read()      # a `bytes` object
    with open(DestinationFile, "wb") as output_file:
        output_file.write(data)


def show_params():
    return "URL,DestinationFile\nhostname must include protocol. eg. http://www.something.com;name of the file where to write to"

def validate(file_to_validate):
    pass

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass

input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)