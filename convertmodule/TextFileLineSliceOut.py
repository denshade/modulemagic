__author__ = 'lveeckha'

import sys
import csv


def execute(row):
    SourceFile = row["SourceFile"]
    RowNumbers = row["RowNumbers"]
    Outputfile = row["OutputFile"]
    write_file = open(Outputfile, 'w')
    read_file = open(SourceFile, 'r')
    counter = 1
    numbers = RowNumbers.split(";")
    numbers = list(map(int, numbers))
    for line in read_file:
        if counter in numbers:
            counter += 1
            continue
        write_file.write(line)
        counter += 1


def show_params():
    return "SourceFile;RowNumbers;OutputFile\nThe text file to slice data out of.;semicolon separated lines to slice out.;The file to write to."


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

