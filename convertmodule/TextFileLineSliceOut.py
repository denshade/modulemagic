__author__ = 'lveeckha'

import sys
import csv

import convertmodule.TextFileLineSliceOutClass

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(convertmodule.TextFileLineSliceOutClass.show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    convertmodule.TextFileLineSliceOutClass.validate(sys.argv[2])


input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        convertmodule.TextFileLineSliceOutClass.execute(row)