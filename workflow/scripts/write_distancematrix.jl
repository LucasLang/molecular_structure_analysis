using MolStructSampling.Analysis
using MolStructSampling.ECWaveFunction
using ProgressBars

using DelimitedFiles
using NPZ

paramfolder = ARGS[1]
samplefile = ARGS[2]
nclustering = parse(Int64, ARGS[3])
offset = parse(Int64, ARGS[4])
outfile = ARGS[5]

param = WaveFuncParam(paramfolder)

samples_all = readdlm(samplefile)

nsteps = size(samples_all)[2]

samples = [samples_all[:, (nsteps÷nclustering)*i + offset] for i in 0:(nclustering-1)]

# important: we assume that the coordinates of all nuclei come before the first non-nucleus!
Nnuc = 3    # there are three nuclei in D3+

RCOM_matrix = Vector{Matrix{Float64}}(undef, nclustering)

for i in 1:nclustering
    Ri_COM = R_nucCOMframe(samples[i], param.masses, Nnuc)[1:Nnuc]
    RCOM_matrix[i] = vecofvec_to_matrix(Ri_COM)
end

distance_matrix = Matrix{Float64}(undef, nclustering, nclustering)

pbar = ProgressBar(total=nclustering*(nclustering+1)÷2)   # number of unique elements of distance matrix
for i in 1:nclustering
    for j in 1:i
        distance_matrix[i,j] = minRMSD(RCOM_matrix[i], RCOM_matrix[j])
        distance_matrix[j,i] = distance_matrix[i,j]
        update(pbar)
    end
end

npzwrite(outfile, distance_matrix)
