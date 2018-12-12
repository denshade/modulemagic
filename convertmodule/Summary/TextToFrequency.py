__author__ = 'lveeckha'

import sys
import csv
import re
from collections import Counter

def execute(row):
    TextFile = row["TextFile"]
    CsvFile = row["CsvFile"]
    createCountFile(TextFile, CsvFile)

def show_params():
    return "TextFile,CsvFile\nSource Text file.,The destination csv file."


def Excluded(word):
    pattern = re.compile("^([a-zA-Z]+)+$")
    if not pattern.match(word):
        return True
    excludedWords = ["-", "patiënten","patiënt", "lieven","gegevens", "criteria","protocol", "populatie", "klinische","software","databronnen", "tool", "clinical", "inclusie","exclusie","specific",
                     "i2b2","custodix","datatekortkomingen","validatie", "databron","recruitment","feasibility", "probleem", "data", "beschikbaar",
                     "waarden", "getallen", "figuur", "waarde", "transformer", "container", "coderen", "getal", "hand", "tunnel", "n", "gebruiken", "bits", "gebruikt", "grootte", "slaan", "xml",
                     "codering", "opgeslagen", "tunnelen", "compressie", "aantal", "kiezen", "basis", "bsdl",
                     "optimale", "gebruik", "containers", "transformers", "vorige", "symbool", "parameters", "opslaan"]
    return word in excludedWords


def createCountFile(TextFile, CsvFile):
    data = ""
    with open(TextFile, 'r', encoding="utf8") as myfile:
        data += myfile.read().lower()
    c = Counter()
    for line in data.splitlines():
        relevantWords = []
        for word in line.split():
            if not Excluded(word):
                relevantWords.append(word)

        c.update(relevantWords)
    mostCommon = dict(c.most_common(50))
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