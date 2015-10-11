__author__ = 'Lieven'

import sys
import csv
import os


def execute(row):
    directory = row['Directory']
    os.system("start " + directory)

def show_params():
    return "Directory\n"



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

