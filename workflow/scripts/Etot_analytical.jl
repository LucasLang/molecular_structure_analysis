include("OutputParser.jl")
using Main.OutputParser
using DelimitedFiles

input = ARGS[1]
outfile = ARGS[2]

Etot = parse_output(input, ["CURRENT_ENERGY"], 0, 1)
Etot = replace(Etot, "D"=>"E")
Etot = parse(Float64, Etot)

writedlm(outfile, Etot)
