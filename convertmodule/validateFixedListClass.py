__author__ = 'lveeckha'

import csv

def show_params():
    return "ValidationList;FileToProcess\nFile that contains the correct validation options.;The file to process"

def validate(temp):
    return True

def execute(row):
    validationListFile = row["ValidationList"]
    file_to_process = row["FileToProcess"]

    allowedValues = {}
    with open(validationListFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key == '' or key is None:
                    continue
                if value == '':
                    continue
                if key in allowedValues:
                    allowedValues[key].append(value.strip())
                else:
                    allowedValues[key] = [value.strip()]


    with open(file_to_process) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key in allowedValues and not value.strip() in allowedValues[key] and not value == '':
                    print("watch it " + value + " for " + key)