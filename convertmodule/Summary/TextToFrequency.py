__author__ = 'lveeckha'

import sys
import csv
from collections import Counter

def execute(row):
    TextFile = row["TextFile"]
    CsvFile = row["CsvFile"]
    createCountFile(TextFile, CsvFile)

def show_params():
    return "TextFile,CsvFile\nSource Text file.,The destination csv file."


def createCountFile(TextFile, CsvFile):
    data = ""
    with open(TextFile, 'r', encoding="utf8") as myfile:
        data += myfile.read().lower()
    c = Counter()
    for line in data.splitlines():
        c.update(line.split())
    mostCommon = dict(c.most_common(100))
    f = open(CsvFile, 'w', encoding="utf8")
    w = csv.DictWriter(f, mostCommon.keys())
    w.writeheader()
    w.writerow(mostCommon)
    f.close()


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