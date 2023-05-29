from sklearn_extra.cluster import KMedoids
import numpy as np
import sys

dmfile = sys.argv[1]
outfolder = sys.argv[2]


distance_matrix = np.load(dmfile)

kmedoids1 = KMedoids(n_clusters=1, metric='precomputed').fit(distance_matrix)
np.save(f'{outfolder}/nclusters1_medoid_indices', kmedoids1.medoid_indices_)
np.save(f'{outfolder}/nclusters1_labels', kmedoids1.labels_)
print(kmedoids1.medoid_indices_)
print(kmedoids1.labels_)
