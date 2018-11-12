import sys
from zlm_plot import plot_M

s = sys.argv[1]
filename = 's82_' + s

M = []
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        M.append(float(line[4]))

plot_M(M, s)