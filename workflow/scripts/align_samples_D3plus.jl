using MolStructSampling.Analysis
using MolStructSampling.ECWaveFunction

using DelimitedFiles
using NPZ

samples_filename = ARGS[1]
medoid_index_filename = ARGS[2]
nselection = parse(Int64, ARGS[3])
nclustering = parse(Int64, ARGS[4])
out_filename = ARGS[5]

masses = [3670.4829652, 3670.4829652, 3670.4829652, 1.0, 1.0]
N = 5   # number of particles
Nnuc = 3    # there are three nuclei in D3+

samples_all = readdlm(samples_filename)    # this takes some time (not actual disk reading, but CPU processing)

nsteps = size(samples_all)[2]
interval_clustering = nsteps÷nclustering

samples = [samples_all[:, (nsteps÷nselection)*i] for i in 1:nselection]

# important: we assume that the coordinates of all nuclei come before the first non-nucleus!

medoid_index = npzread(medoid_index_filename)[1]            # keep in mind that counting starts at 0 in Python and at 1 in Julia!
medoid_index = interval_clustering*(medoid_index + 1)       # now we have an index with respect to the complete sample
Rnuc_medoid = R_nucCOMframe(samples_all[:, medoid_index], masses, Nnuc)[1:Nnuc]
B = determine_basis_inplane_3particle(Rnuc_medoid)
Rnuc_medoid_planebasis = transform_newbasis(Rnuc_medoid, B)
Rnuc_medoid_matrix = vecofvec_to_matrix(Rnuc_medoid_planebasis)

nxyz = 3
nparticles = 5
Ri_COM_matrices_rotated = Array{Float64}(undef, nselection, nxyz, nparticles)
for i in 1:nselection
    Ri_COM = R_nucCOMframe(samples[i], masses, Nnuc)
    Ri_COM_planebasis = transform_newbasis(Ri_COM, B)
    Ri_COM_matrix = vecofvec_to_matrix(Ri_COM_planebasis)
    Uopt = optimal_rotation(Rnuc_medoid_matrix, Ri_COM_matrix[1:Nnuc, :])
    Ri_COM_matrices_rotated[i,:,:] = Uopt*Ri_COM_matrix'
end

npzwrite(out_filename, Ri_COM_matrices_rotated)
