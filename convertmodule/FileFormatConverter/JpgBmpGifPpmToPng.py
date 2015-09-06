__author__ = 'Lieven'

from PIL import Image

import sys
import csv


def execute(row):
    source_file = row["SourceFile"]
    destination_file = row["DestinationFile"]
    im = Image.open(source_file)
    im.save(destination_file, 'PNG')


def show_params():
    return "SourceFile,DestinationFile\nSource file.,The destination file"



if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass
    #validate(sys.argv[2])



input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)