import sys
import csv
import os
import subprocess

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
        module_path = row['module']
        if not os.path.isfile(module_path):
            module_path = working_dir + "\\" + module_path

        recipe_path = row['file']
        if not os.path.isfile(recipe_path):
            recipe_path = working_dir + "\\" + recipe_path

        if not os.path.isfile(recipe_path):
            print("file not found " + row['file'])
            exit(1)
        command = [sys.executable, module_path, recipe_path]
        print("running " + ' '.join(command))
        if subprocess.call(command) != 0:
            print("Running command failed " + ' '.join(command))
            break
