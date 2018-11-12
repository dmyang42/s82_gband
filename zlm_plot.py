import matplotlib.pyplot as plt

def plot_z(z, s):
    plt.hist(z, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel('z')
    plt.ylabel('num')
    # plt.show()
    plt.savefig('z_' + s + '.png', dpi=1000)

def plot_L(L, s):
    plt.hist(L, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel('L')
    plt.ylabel('num')
    # plt.show()
    plt.savefig('L_' + s + '.png', dpi=1000)

def plot_M(M, s):
    plt.hist(M, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel('M')
    plt.ylabel('num')
    # plt.show()
    plt.savefig('M_' + s + '.png', dpi=1000)