import sys
import csv

def show_params():
    return "From,epoch,Tweet"

def execute(row):
    source = row["From"]
    epoch = row["DestinationFile"]
    tweet  = row["tweet"]



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