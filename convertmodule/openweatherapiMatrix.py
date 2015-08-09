__author__ = 'Lieven'


import sys
import json
import time

if len(sys.argv) != 3:
      print("Usage: openweatherapiMatrix <file.json> <file.csv>")
      sys.exit(2)

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