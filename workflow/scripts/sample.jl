using MolStructSampling.ECWaveFunction
using MolStructSampling.MCSampling
using DelimitedFiles

params_folder = ARGS[1]
nsteps = parse(Int64, ARGS[2])
outfolder = ARGS[3]

param_processed = ECWaveFunction.WaveFuncParamProcessed(params_folder)
prob_dens(r) = ECWaveFunction.calc_probability_density(r, param_processed)

D2 = [0.0, 0.0, 2.30]
D3 = [0.85, 0.0, 0.85]
e1 = 0.5 .* D2
e2 = 0.5 .* D3
r_start = [D2; D3; e1; e2]

widths = [0.7, 0.7, 2.2, 2.2]      # jumping widths that give roughly 50% acceptance ratio

sample, saved_rho, accepted_rejected = MCrun(prob_dens, param_processed.n, nsteps, r_start, widths)
writedlm("$(outfolder)/sample", sample)
writedlm("$(outfolder)/rho", saved_rho)
writedlm("$(outfolder)/accepted_rejected", accepted_rejected)

