using MolStructSampling.Analysis
using MolStructSampling.ECWaveFunction

using DelimitedFiles
using NPZ

paramfolder = ARGS[1]
samplefile = ARGS[2]
nclustering = parse(Int64, ARGS[3])
outfile = ARGS[4]

param = WaveFuncParam(paramfolder)

samples_all = readdlm(samplefile)

nsteps = size(samples_all)[2]

samples = [samples_all[:, (nsteps÷nclustering)*i] for i in 1:nclustering]

# important: we assume that the coordinates of all nuclei come before the first non-nucleus!
Nnuc = 3    # there are three nuclei in D3+

RCOM_matrix = Vector{Matrix{Float64}}(undef, nclustering)

for i in 1:nclustering
    Ri_COM = R_COMframe(samples[i], param.masses, Nnuc)
    RCOM_matrix[i] = vecofvec_to_matrix(Ri_COM)
end

distance_matrix = Matrix{Float64}(undef, nclustering, nclustering)

for i in 1:nclustering
    for j in 1:i
        distance_matrix[i,j] = minRMSD(RCOM_matrix[i], RCOM_matrix[j])
        distance_matrix[j,i] = distance_matrix[i,j]
    end
end

npzwrite(outfile, distance_matrix)
