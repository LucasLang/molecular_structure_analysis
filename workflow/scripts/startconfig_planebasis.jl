using MolStructSampling.Analysis
using MolStructSampling.ECWaveFunction
using DelimitedFiles

paramfolder = ARGS[1]
outfolder = ARGS[2]

param = WaveFuncParam(paramfolder)


Nnuc = 3    # there are three nuclei in D3+

r = [0, 0, 2.3, 0.85, 0, 0.85, 0, 0, 2.3/2, 0.85/2, 0, 0.85/2]
r_COM = R_nucCOMframe(r, param.masses, Nnuc)

writedlm("$(outfolder)/startconfig_ppcoord", r)
writedlm("$(outfolder)/startconfig_COM", hcat(r_COM...))


