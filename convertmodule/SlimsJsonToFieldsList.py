__author__ = 'Lieven'

import sys
import json
import time
import csv


def show_params():
    return "InputFile,DestinationFile"

def xstr(s):
    if s is None:
        return ''
    return str(s)

def execute(row):
    input_file = row["InputFile"]
    destination_file = row["DestinationFile"]
    text = open(input_file, "r").read()

    f = open(destination_file, 'w')
    map = json.loads(text)
    f.write("interne naam;label;omschrijving;help\n")
    for entity in map['entities']:
        if entity['tableName'] == "Field":
            fieldname = "unknown"
            fieldlabel = "unknown"
            fielddescription = "unknown"
            fieldhelp = "unknown"
            for column in entity['columns']:
                value = column['value']
                name = column['name']
                if name == "tbfl_name":
                    fieldname = xstr(value)
                if name == "tbfl_label":
                    fieldlabel = xstr(value)
                if name == "tbfl_description":
                    fielddescription = xstr(value)
                if name == "tbfl_help":
                    fieldhelp = xstr(value)

            line = "\""+ fieldname + "\";\"" + fieldlabel + "\";\"" + fielddescription + "\";\"" + fieldhelp + "\"" + "\n"
            print(line)
            f.write(line)
    f.close()


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
