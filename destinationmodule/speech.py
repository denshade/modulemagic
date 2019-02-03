import csv

import pyttsx3
import sys

if len(sys.argv) != 2:
      print("""\
            Usage: Speech <source.csv> 
      """)
      sys.exit(2)

def execute(row):
    Text = row["Text"]
    engine = pyttsx3.init()
    engine.say(Text)
    engine.runAndWait()

input_file = sys.argv[1]

with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        execute(row)

