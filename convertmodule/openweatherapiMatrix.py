__author__ = 'Lieven'


import sys
import json
import time
import csv


def show_params():
    return "InputFile,DestinationFile"

def execute(row):
    text = open(sys.argv[1], "r").read()

    f = open(sys.argv[2], 'w')
    map = json.loads(text)
    f.write("time;temperature;isRain\n")
    for weather in map['list']:
        tempInCelc = weather['main']['temp'] - 273.15
        rain = len(weather['rain'])
        line = time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(weather['dt'])) + ";" + str(tempInCelc) + ';' + str(rain) + "\n"
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
