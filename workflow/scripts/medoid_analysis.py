import numpy as np
import sys

samples_name = sys.argv[1]
medoid_index_name = sys.argv[2]
nselection_clustering = int(sys.argv[3])
offset = int(sys.argv[4])
outfile_name = sys.argv[5]

coords_all = np.loadtxt(samples_name)
nsteps = coords_all.shape[1]

interval_clustering = nsteps//nselection_clustering

medoid_index = np.load(medoid_index_name)[0]
medoid_coords = coords_all[:, interval_clustering*medoid_index + offset - 1]

R1 = np.array([0.0, 0.0, 0.0])
R2 = medoid_coords[0:3]
R3 = medoid_coords[3:6]

DD1 = np.linalg.norm(R2-R1)
DD2 = np.linalg.norm(R3-R1)
DD3 = np.linalg.norm(R3-R2)

np.savetxt(outfile_name, np.array([DD1, DD2, DD3]))
