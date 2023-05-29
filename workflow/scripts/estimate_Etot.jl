using MolStructSampling.ECWaveFunction
using MolStructSampling.MCSampling
using MolStructSampling.Analysis
using Statistics
using DelimitedFiles

samplefile = ARGS[1]
paramfolder = ARGS[2]
outfile = ARGS[3]

param_processed = ECWaveFunction.WaveFuncParamProcessed(paramfolder)

samples =  readdlm(samplefile)
nsteps = size(samples)[2]

E_pot_samples = [calc_potential_energy(samples[:,step], param_processed.charges) for step in 1:nsteps]
E_pot_average = mean(E_pot_samples)
E_tot_estimate =  0.5*E_pot_average   # from virial theorem for Coulomb potential (exponent -1)
writedlm(outfile, E_tot_estimate)

