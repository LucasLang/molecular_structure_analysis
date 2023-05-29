import matplotlib.pyplot as plt
import sys
import numpy as np

samplesfile = sys.argv[1]
outfile = sys.argv[2]

xmin = ymin = -1.5
xmax = ymax = 1.5

randangles = [3.230938189452668, 0.6911311486598657, 6.198400566085575, 5.5571267118566965, 1.3296570681242155, 2.013579035210648] # random.random()*2*np.pi


size = 200

# six samples
nselection = 6
Nnuc = 3    # we have three deuterons
colors_samples = ['tab:red', 'tab:green', 'tab:blue', 'tab:olive', 'tab:purple', 'tab:orange']
coords = np.load(samplesfile)
nsteps = coords.shape[0]
for i in range(nselection):
    index = (nsteps//nselection)*(i+1) - 1
    for j in range(Nnuc):    # plot deuterons
        x = np.cos(randangles[i])*coords[index,0,j] + np.sin(randangles[i])*coords[index,1,j]
        y = -np.sin(randangles[i])*coords[index,0,j] + np.cos(randangles[i])*coords[index,1,j]
        plt.scatter(x,y, s=size, c=colors_samples[i])

plt.xlim([xmin,xmax])
plt.ylim([ymin,ymax])
plt.xlabel("x / Bohrs")
plt.ylabel("y / Bohrs")
plt.gca().set(adjustable='box', aspect='equal')

plt.tight_layout()
plt.savefig(outfile, dpi=300)
