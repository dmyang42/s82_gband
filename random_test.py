from scipy.stats import ks_2samp

z_all, M_all, L_all = [], [], []

with open('s82_all') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        z_all.append(float(line[2]))
        L_all.append(float(line[3]))
        M_all.append(float(line[4]))
        

z_rnd, M_rnd, L_rnd = [], [], []

with open('s82_rnd') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        z_rnd.append(float(line[2]))
        L_rnd.append(float(line[3]))
        M_rnd.append(float(line[4]))

print('\n')
print(ks_2samp(z_all, z_rnd))
print(ks_2samp(L_all, L_rnd))
print(ks_2samp(M_all, M_rnd))