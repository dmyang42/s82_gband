import sys
from zlm_plot import plot_L

s = sys.argv[1]
filename = 's82_' + s

L = []
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        L.append(float(line[3]))

plot_L(L, s)