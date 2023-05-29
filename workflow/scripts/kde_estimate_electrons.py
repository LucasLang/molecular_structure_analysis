from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import sys

sample_name = sys.argv[1]
medoid_index_name = sys.argv[2]
clusterinterval = int(sys.argv[3])
outfile = sys.argv[4]

bandwidth = 0.1  # KDE bandwidth
d = 0.1   # spacing between voxels
xmin = ymin = -2
xmax = ymax = 2
zmin = -1.5
zmax = 1.5
Nx = int((xmax-xmin)/d + 1)
Ny = int((ymax-ymin)/d + 1)
Nz = int((zmax-zmin)/d + 1)

coords = np.load(sample_name)
nselection = coords.shape[0]   # select all

Nel = 2
eltot_xyz = np.empty((Nel*nselection, 3))    # KDE estimate for ANY electron positions (combining e1 and e2)

for i in range(nselection):
    eltot_xyz[i, :] = coords[i, :3, 3]
    eltot_xyz[nselection+i, :] = coords[i, :3, 4]

xgrid = np.linspace(xmin, xmax, Nx)
ygrid = np.linspace(ymin, ymax, Ny)
zgrid = np.linspace(zmin, zmax, Nz)
X,Y,Z = np.meshgrid(xgrid, ygrid, zgrid, indexing='ij')
XYZ_values = np.vstack((X.flatten(), Y.flatten(), Z.flatten())).transpose()
XYZ_values_parts = []
Nparts = Nx
size_part = Nx*Ny*Nz//Nparts
for i in range(Nparts):
    XYZ_values_parts.append(XYZ_values[i*size_part:i*size_part+size_part, :])

print("Doing KDE fit ...")
kde_electrons = KernelDensity(bandwidth=bandwidth)
kde_electrons.fit(eltot_xyz)
density_electrons_parts = []
print("Evaluating KDE on the grid ...")
for i in tqdm(range(Nparts)):
    log_density_electrons = kde_electrons.score_samples(XYZ_values_parts[i])
    density_electrons_parts.append(Nel*np.exp(log_density_electrons))    # KDE density is normalized to 1, so have to multiply with number of electrons
density_electrons = np.hstack(density_electrons_parts)

medoid_index = np.load(medoid_index_name)[0]
medoid_index = clusterinterval*(medoid_index+1)   # to index ALL samples
coords_medoid = coords[medoid_index,:,:]

### Write cube file
natoms = 3
Z_H = 1    # nuclear charge of hydrogen
print("Writing cube file ...")
with open(outfile, "w") as f:
    f.write("KDE electron density extracted from random samples drawn from the non-BO joint probability density\n\n")
    f.write("{} {} {} {}\n".format(natoms, xmin, ymin, zmin))
    f.write("{} {} {} {}\n".format(Nx, d, 0.0, 0.0))
    f.write("{} {} {} {}\n".format(Ny, 0.0, d, 0.0))
    f.write("{} {} {} {}\n".format(Nz, 0.0, 0.0, d))
    # write medoid positions:
    f.write("{} {} {} {} {}\n".format(Z_H, 0.0, coords_medoid[0, 0], coords_medoid[1, 0], coords_medoid[2, 0]))
    f.write("{} {} {} {} {}\n".format(Z_H, 0.0, coords_medoid[0, 1], coords_medoid[1, 1], coords_medoid[2, 1]))
    f.write("{} {} {} {} {}\n".format(Z_H, 0.0, coords_medoid[0, 2], coords_medoid[1, 2], coords_medoid[2, 2]))
    for i in tqdm(range(Nx*Ny*Nz)):
        f.write("{}\n".format(density_electrons[i]))
