import numpy as np
import sys
import matplotlib.pyplot as plt
from decimal import Decimal
import matplotlib

startconfig_file = sys.argv[1]
outfile = sys.argv[2]

startconfig = np.loadtxt(startconfig_file)


size_deuteron = 80
size_electron = 20
value_range = [-2, 2]

plt.xlim(value_range)
plt.ylim(value_range)

plt.xlabel("x / Bohrs")
plt.ylabel("z / Bohrs")
plt.gca().set(adjustable='box', aspect='equal')    # this ensures that the subplots are square
for i in range(3):    # plot deuterons
    plt.scatter(startconfig[1,i], startconfig[0,i], s=size_deuteron, c='tab:blue')
for i in range(3,5):  # plot electrons
    plt.scatter(startconfig[1,i], startconfig[0,i], s=size_electron, c='tab:red')

plt.savefig(outfile, dpi=300)


