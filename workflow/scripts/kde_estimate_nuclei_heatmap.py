from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.gridspec import GridSpec
import sys

samples_aligned_name = sys.argv[1]
medoid_index_name = sys.argv[2]
nselection_clustering = int(sys.argv[3])
nselection_samples = int(sys.argv[4])
outfile_name = sys.argv[5]

bandwidth = 0.05
xmin = ymin = -1.5
xmax = ymax = 1.5
Nx = Ny = 50

mycmap_blue = LinearSegmentedColormap.from_list('mycmap_blue', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765,0), (0.12156862745098039, 0.4666666666666667, 0.7058823529411765,1)])    # interpolate alpha value from 0 to 1 for tab:blue

coords_all = np.load(samples_aligned_name)
nsteps = coords_all.shape[0]

interval_clustering = nsteps//nselection_clustering
D1_xy = np.empty((3*nselection_clustering, 2))          # only x,y since z coordinate is always very close to zero and therefore not interesting.

for i in range(nselection_clustering):
    index = interval_clustering*(i+1) - 1
    D1_xy[i, :] = coords_all[index, :2, 0]
    D1_xy[nselection_clustering+i, :] = coords_all[index, :2, 1]
    D1_xy[2*nselection_clustering+i, :] = coords_all[index, :2, 2]

xgrid = np.linspace(xmin, xmax, Nx)
ygrid = np.linspace(ymin, ymax, Ny)
X,Y = np.meshgrid(xgrid, ygrid)
XY_values = np.vstack((X.flatten(), Y.flatten())).transpose()

kde_D1 = KernelDensity(bandwidth=bandwidth)
kde_D1.fit(D1_xy)
log_density_D1 = kde_D1.score_samples(XY_values)
density_D1 = np.exp(log_density_D1)
Z_D1 = 3*np.flip(density_D1.reshape((Nx, Ny)), axis=0)     # flip reverses the rows. This is important for plotting with imshow. times 3 such that it is normalized to number of deuterons.

fig = plt.figure(figsize=(4, 2))
gs = GridSpec(1, 2, width_ratios=[4,5], height_ratios=[1])    # choose right axis 20% larger such that colorbar also fits in (otherwise the plot will shrink to make space for the colorbar).
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

# Left plot: medoid structure and six samples
interval_samples = nsteps//nselection_samples
Nnuc = 3    # we have three deuterons
colors_samples = ['tab:red', 'tab:green', 'tab:blue', 'tab:olive', 'tab:purple', 'tab:orange']
medoid_index = np.load(medoid_index_name)[0]
medoid_coords = coords_all[interval_clustering*(medoid_index+1) - 1]
for i in range(nselection_samples):
    index = interval_samples*(i+1) - 1
    for j in range(Nnuc):    # plot deuterons
        ax1.scatter(coords_all[index, 0,j], coords_all[index, 1,j], s=10, c=colors_samples[i])
for j in range(Nnuc):    # plot deuterons
    ax1.scatter(medoid_coords[0,j], medoid_coords[1,j], s=10, c='k')

ax1.set_xlim([xmin,xmax])
ax1.set_ylim([ymin,ymax])
ax1.set_xlabel("x / Bohrs")
ax1.set_ylabel("y / Bohrs")
ax1.set(adjustable='box', aspect='equal')

# Right plot: Heatplot of KDE
fig_D1 = ax2.imshow(Z_D1, extent = (xmin, xmax, ymin, ymax), cmap = mycmap_blue, interpolation = 'bicubic')
ax2.set_xlabel("x / Bohrs")
ax2.set_ylabel("y / Bohrs")
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="10%", pad="15%")
plt.colorbar(fig_D1, cax = cax)
plt.tight_layout()
plt.savefig(outfile_name, dpi=300)
