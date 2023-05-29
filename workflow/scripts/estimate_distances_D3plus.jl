using LinearAlgebra
using DelimitedFiles

samplename = ARGS[1]
outfolder = ARGS[2]

samples = readdlm(samplename)
nsteps = size(samples)[2]

sum_nuc_nuc = 0.0
sum_nuc_el = 0.0
sum_el_el = 0.0
for i in 1:nsteps
    D1 = samples[1:3,i]
    D2 = samples[4:6,i]
    e1 = samples[7:9,i]
    e2 = samples[10:12,i]
    global sum_nuc_nuc += (norm(D1)+norm(D2)+norm(D2-D1))/3
    global sum_nuc_el += (norm(e1-D1)+norm(e2-D1)+norm(e1-D2)+norm(e2-D2)+norm(e1)+norm(e2))/6
    global sum_el_el += norm(e2-e1)
end

writedlm("$(outfolder)/rDD_sampling", sum_nuc_nuc/nsteps)
writedlm("$(outfolder)/rDe_sampling", sum_nuc_el/nsteps)
writedlm("$(outfolder)/ree_sampling", sum_el_el/nsteps)
