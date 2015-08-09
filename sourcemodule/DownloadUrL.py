__author__ = 'Lieven'

import sys
import wget

if len(sys.argv) != 3:
    print("Usage: DownloadUrl <URL> <outputfile.csv>")
    sys.exit(2)

url = sys.argv[1]
outputfile = sys.argv[2]

wget.download(url, outputfile)
