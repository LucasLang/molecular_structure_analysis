import sys
import numpy as np
import matplotlib.pyplot as plt

rhofile = sys.argv[1]
nsteps = int(sys.argv[2])
outfile = sys.argv[3]

rhovalues = np.loadtxt(rhofile)

median = np.median(rhovalues)

plt.plot([1,nsteps], [median, median], color='tab:orange') 
plt.plot(rhovalues, color='tab:blue')                     
plt.xlabel("Step")
plt.ylabel(r"$\rho$ / a.u.")
plt.xlim([1,nsteps])
plt.ylim([1e-10, 1e-3])
plt.yscale('log')
plt.savefig(outfile, dpi=300)
