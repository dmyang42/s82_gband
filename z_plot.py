import sys
from zlm_plot import plot_z

s = sys.argv[1]
filename = 's82_' + s

z = []
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        z.append(float(line[2]))

plot_z(z, s)