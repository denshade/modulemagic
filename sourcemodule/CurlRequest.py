__author__ = 'Lieven'

import sys
import csv

import sourcemodule.CurlRequestClass

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(sourcemodule.CurlRequestClass.show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    sourcemodule.CurlRequestClass.validate(sys.argv[2])

input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sourcemodule.CurlRequestClass.execute(row)