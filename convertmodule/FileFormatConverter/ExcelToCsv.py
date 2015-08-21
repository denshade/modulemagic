__author__ = 'lveeckha'

import sys
import csv

import convertmodule.FileFormatConverter.ExcelToCsvClass

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(convertmodule.FileFormatConverter.ExcelToCsvClass.show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    convertmodule.FileFormatConverter.ExcelToCsvClass.validate(sys.argv[2])


input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        convertmodule.FileFormatConverter.ExcelToCsvClass.execute(row)