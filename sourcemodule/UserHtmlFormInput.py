import os

__author__ = 'lveeckha'

import sys
import csv


def show_params():
    print(
        "FormName,DefinitionMatrixFile,DestinationFile\nThe file with the definition of fields. It's a matrix with two colums: field/value., The file where to write to.")


def getDefinitions(definitionMatrixFile):
    answer = []
    with open(definitionMatrixFile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            answer.append(row)
    return answer



def execute(row):
    definitionMatrixFile = row['DefinitionMatrixFile']
    destinationFile = row['DestinationFile']
    fileData = "<html>"
    fileData = "<head>"
    fileData = "</head>"

    fileData += "<body><form>"
    fileData += "<table width=\"100%\">"
    fileData += "<thead>"
    fileData += "<tr>"
    definitions = getDefinitions(definitionMatrixFile)
    for row in definitions:
        fileData += "<th>"+row["Field"]+"</th>"
    fileData += "</tr>"
    fileData += "</thead>"
    fileData += "<tbody>"

    fileData += "<tr>"
    for row in definitions:
        fileData += "<td>"
        fileData += row["Value"]
        fileData += "</td>"
    fileData += "</tr>"

    for i in range(1, 10):
        fileData += "<tr>"
        for row in definitions:
            fileData += "<td>"
            fileData += "<input style=\"width:100%;\" type=\"text\" id=\"" + row["Field"] + "_" + str(i) + "\" />"
            fileData += "</td>"
        fileData += "</tr>"
    fileData += "</tbody>"
    fileData += "</table>"
    fileData += "<input type=\"submit\" value=\"Store as matrix\">"
    fileData += "</form></body>"
    fileData += "</html>"
    with open("input.html", 'w') as f:
        f.write(fileData)
    os.system("start input.html")

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    show_params()
    sys.exit(2)
#if sys.argv[1] == "--validate":
    #validate(sys.argv[2])

input_file = sys.argv[1]

with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)

