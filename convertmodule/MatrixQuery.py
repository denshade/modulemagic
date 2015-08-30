import os

__author__ = 'lveeckha'

import sys
import csv

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print("Query,ResultFile\nThe query sqlite3.,The result file.")
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass

def execute(row):
    Query = row['Query']
    ResultFile = row['ResultFile']
    os.system("q \"" + Query + "\" > " + ResultFile + " -d ,")

input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)

