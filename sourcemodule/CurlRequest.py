__author__ = 'Lieven'

import sys
import urllib

if len(sys.argv) != 3:
    print("Usage: CurlRequest <URL> <outputfile.csv>")
    sys.exit(2)

url = sys.argv[1]

testfile = urllib.URLopener()
