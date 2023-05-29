using MolStructSampling.Analysis
using MolStructSampling.ECWaveFunction

using DelimitedFiles

paramfolder = ARGS[1]
samplingfolder = ARGS[2]
nselection = parse(Int64, ARGS[3])
outfolder = ARGS[4]

param = WaveFuncParam(paramfolder)

samples_all = readdlm("$(samplingfolder)/sample")
saved_rho_all = readdlm("$(samplingfolder)/rho")

nsteps = size(samples_all)[2]

samples = [samples_all[:, (nsteps÷nselection)*i] for i in 1:nselection]
saved_rho = [saved_rho_all[(nsteps÷nselection)*i] for i in 1:nselection]

# important: we assume that the coordinates of all nuclei come before the first non-nucleus!
Nnuc = 3    # there are three nuclei in D3+

samples_individualvectors_planebasis = [project_coords_nuclearplane_3particle(r, param.masses, Nnuc) for r in samples]

writedlm("$(outfolder)/saved_rho_selected", saved_rho)
for i in 1:nselection
    writedlm("$(outfolder)/sample$(i)_planebasis", hcat(samples_individualvectors_planebasis[i]...))
end
