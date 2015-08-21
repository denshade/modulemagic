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
working_dir = os.path.dirname(os.path.realpath(__file__))
with open(inputFile, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("running " + row['module'] + " " + row['file'] + "\n")
        os.system(working_dir+"\\"+row['module'] + " \"" + row['file']+"\"")


