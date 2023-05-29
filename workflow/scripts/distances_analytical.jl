include("OutputParser.jl")
using Main.OutputParser
using DelimitedFiles

input = ARGS[1]
outfolder = ARGS[2]

rDD = parse_output(input, ["Properly symmetrized expectation", " r_1 "], 0, 6)
rDD = replace(rDD, "D"=>"E")
rDD = parse(Float64, rDD)

rDe = parse_output(input, ["Properly symmetrized expectation", " r_13 "], 0, 12)
rDe = replace(rDe, "D"=>"E")
rDe = parse(Float64, rDe)

ree = parse_output(input, ["Properly symmetrized expectation", " r_34 "], 0, 2)
ree = replace(ree, "D"=>"E")
ree = parse(Float64, ree)

writedlm("$(outfolder)/rDD_analytical", rDD)
writedlm("$(outfolder)/rDe_analytical", rDe)
writedlm("$(outfolder)/ree_analytical", ree)

