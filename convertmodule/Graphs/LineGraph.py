import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

__author__ = 'lveeckha'

if len(sys.argv) != 2 or sys.argv[1] == "--inputparameters":
    print("Input file. Expected is the first column as the label, the other columns are y values.")
    sys.exit(2)
if sys.argv[1] == "--validate":
    pass
    #validate(sys.argv[2])



input_file = sys.argv[1]

tick = 0
y_array = []
my_xticks = []
with open(input_file) as f:
    lines = f.readlines()
    for line in lines[1:]:
        y_array.append(float(line.split(",")[1]))
        if tick % ((len(lines) - 1) / 4) == 0:
            my_xticks.append(line.split(",")[0])
        tick += 1



x = np.array(range(1, len(lines)))
y = np.array(y_array)
plt.xticks(x, my_xticks)
plt.locator_params(nbins=4)
plt.plot(x, y)
plt.show()

