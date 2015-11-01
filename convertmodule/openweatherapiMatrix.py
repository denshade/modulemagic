__author__ = 'Lieven'

import sys
import json
import time
import csv


def show_params():
    return "InputFile,DestinationFile"


def execute(row):
    input_file = row["InputFile"]
    destination_file = row["DestinationFile"]
    text = open(input_file, "r").read()

    f = open(destination_file, 'w')
    map = json.loads(text)
    f.write("time,temperature,isRain\n")
    for weather in map['list']:
        tempInCelc = weather['main']['temp'] - 273.15
        if 'rain' in weather:
            rain = len(weather['rain'])
        else:
            rain = 0
        line = time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(weather['dt'])) + "," + str(tempInCelc) + ',' + str(
            rain) + "\n"
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
