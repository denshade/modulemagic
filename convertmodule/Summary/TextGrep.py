__author__ = 'lveeckha'

import sys
import csv
import re

def execute(row):
    TextFile = row["TextFile"]
    Regex = row["Regex"]
    OutFile = row["OutFile"]
    createGrepFile(TextFile, Regex, OutFile)

def show_params():
    return "TextFile,Regex,OutFile\nTextFile,Regex,OutFile with all matches of the regex"


def createGrepFile(TextFile, Regex, OutFile):
    with open(OutFile, 'w', encoding="utf8") as outfile:
        with open(TextFile, 'r', encoding="utf8") as textfile:
            for word in re.findall(Regex, textfile.read()):
                outfile.write(word + "\n")


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