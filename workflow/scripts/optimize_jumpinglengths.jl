using MolStructSampling.ECWaveFunction
using MolStructSampling.MCSampling
using DelimitedFiles

paramfolder = ARGS[1]
nsteps = parse(Int64, ARGS[2])
outfile = ARGS[3]

param_processed = ECWaveFunction.WaveFuncParamProcessed(paramfolder)
prob_dens(r) = ECWaveFunction.calc_probability_density(r, param_processed)

dist_avg = 1.72   # from Cafiero, Adamowicz 2004
D2 = [0.0, 0.0, dist_avg]
D3 = [(sqrt(3)/2)*dist_avg, 0.0, 0.5*dist_avg]
e1 = 0.5 .* D2
e2 = 0.5 .* D3
r_start = [D2; D3; e1; e2]

finished=false
widths = [0.5, 0.5, 0.5, 0.5]
deltas = [0.5, 0.5, 0.5, 0.5]
nturns = [0,0,0,0]    # number of times that the direction of changes to the widths has been changed


println("Widths: ", widths)
samples, saved_P, accepted_rejected = MCrun(prob_dens, param_processed.n, nsteps, r_start, widths)
acceptance_ratios = [accepted_rejected[pp,1]/(accepted_rejected[pp,1]+accepted_rejected[pp,2]) for pp in 1:param_processed.n]
println("Acceptance ratios: ", acceptance_ratios, "\n")
bigger_onehalf = [acceptance_ratios[pp]>0.5 for pp in 1:param_processed.n]
optwidths = deepcopy(widths)
optratios = deepcopy(acceptance_ratios)

while !finished
    for pp in 1:param_processed.n
        if bigger_onehalf[pp]
            widths[pp]+=deltas[pp]
        else
            widths[pp]-=deltas[pp]
        end
    end
    println("Widths: ", widths)
    global samples, saved_P, accepted_rejected = MCrun(prob_dens, param_processed.n, nsteps, r_start, widths)
    global acceptance_ratios = [accepted_rejected[pp,1]/(accepted_rejected[pp,1]+accepted_rejected[pp,2]) for pp in 1:param_processed.n]
    println("Acceptance ratios: ", acceptance_ratios, "\n")
    bigger_onehalf_new = [acceptance_ratios[pp]>0.5 for pp in 1:param_processed.n]
    for pp in 1:param_processed.n
        if bigger_onehalf_new[pp] != bigger_onehalf[pp]
            nturns[pp] += 1
            if nturns[pp] == 1
                deltas[pp] = 0.1
            end
        end
        if abs(acceptance_ratios[pp]-0.5)<abs(optratios[pp]-0.5)
            optratios[pp] = acceptance_ratios[pp]
            optwidths[pp] = widths[pp]
        end
    end
    global bigger_onehalf = bigger_onehalf_new
    if (nturns[1]>1) && (nturns[2]>1) && (nturns[3]>1) && (nturns[4]>1)
        global finished=true
    end
    
end
println("Optimum widths: ", optwidths)
println("Optimum acceptance ratios: ", optratios)
writedlm(outfile, optwidths)
