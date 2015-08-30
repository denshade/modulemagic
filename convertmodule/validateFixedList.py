__author__ = 'lveeckha'
import sys
import csv

def show_params():
    return "ValidationList;FileToProcess;ResultFile\nFile that contains the correct validation options.;The file to process;The file to output to with the following header: row number;offending column;offending value"

def validate(temp):
    return True

def execute(row):
    validationListFile = row["ValidationList"]
    file_to_process = row["FileToProcess"]
    file_to_write = row["ResultFile"]
    allowedValues = getAllowedValues(validationListFile)

    errorMatrix = open(file_to_write,"w")

    with open(file_to_process) as csvfile:
        reader = csv.DictReader(csvfile)
        rowNr = 1
        errorMatrix.write("row number,offending column,offending value\n")
        for row in reader:
            for key, value in row.items():
                if key in allowedValues and not value.strip() in allowedValues[key] and not value == '':
                    errorMatrix.write(str(rowNr) + "," + key + "," + value + "\n")
            rowNr += 1


def getAllowedValues(validationListFile):
    allowedValues = {}
    with open(validationListFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key == '' or key is None:
                    continue
                if value == '' or value is None:
                    continue
                if key in allowedValues:
                    allowedValues[key].append(value.strip())
                else:
                    allowedValues[key] = [value.strip()]
    return allowedValues

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print(sys.argv)
    print(show_params())
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass

input_file = sys.argv[1]


with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)