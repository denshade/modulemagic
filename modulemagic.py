__author__ = 'Lieven'

import sys
import csv
import os

if len(sys.argv) != 2:
      print("""\
            Usage: modulemagic <recipe.matrix.csv>
      """)
      sys.exit(2)
inputFile = sys.argv[1]
with open(inputFile, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("running " + row['module'] + " " + row['file'] + "\n")
        os.system(row['module'] + " \"" + row['file']+"\"")


