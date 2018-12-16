__author__ = 'lveeckha'

import sys
import csv
import os.path
import re

def execute(row):
    TextFile = row["TextFile"]
    DictFile = row["DictFile"]
    IndexFile = row["IndexFile"]
    createCountFile(TextFile, DictFile, IndexFile)

def show_params():
    return "TextFile,DictFile,IndexFile\nSource Text file.,The Dictionary file with the indexes., The Index File that only contains numbers(indexes)"


def createCountFile(TextFile, DictFile, IndexFile):
    dictionary = []
    if os.path.isfile(DictFile):
        with open(DictFile, 'r', encoding="utf8") as dictfile:
             dictionary = dictfile.read().lower().splitlines()

    numbers = []
    with open(IndexFile, 'w', encoding="utf8") as indexfile:
        with open(TextFile, 'r', encoding="utf8") as textfile:
            textline = re.split('\W+',textfile.read().lower())
            for tokval in textline:
                if tokval not in dictionary:
                    dictionary.append(tokval)
                number = dictionary.index(tokval)
                numbers.append(str(number))
                if len(numbers) > 100:
                    indexfile.write(",".join(numbers) + "\n")
                    numbers = []

        indexfile.write(",".join(numbers) + "\n")

    with open(DictFile, 'w', encoding="utf-8") as dictfile:
        for tokval in dictionary:
            dictfile.write(tokval + "\n")

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