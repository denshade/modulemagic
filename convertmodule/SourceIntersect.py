__author__ = 'Lieven'


import sys

if len(sys.argv) != 4:
      print("""\
            Usage: SourceIntersect <a.csv> <b.csv> <target.csv>
      """)
      sys.exit(2)

sourceA = sys.argv[1]
sourceB = sys.argv[2]
dest = sys.argv[3]

textA = open(sourceA, "r").read()
textB = open(sourceB, "r").read()

textA = set(textA.split("\n"))
textB = set(textB.split("\n"))

f = open(sys.argv[2], 'w')

textC = textA.intersection(textB)
f.write(textC);
