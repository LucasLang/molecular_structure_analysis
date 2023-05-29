module OutputParser

export parse_output, parse_float, parse_int 

"""
Extract a number from a log file.
You can provide any number of searchstrings.
linenumber is the line containing the number relative to the one where the last search string was found. 0 means that the number is in the same line as the last search string.
wordnumber is the index of the word that represents the number to be parsed. An index of 0 corresponds to the first word in the line.
"""
function parse_output(file::IOStream, searchstrings, linenumber, wordnumber)
    searchstringfound, currentline = read_until_hit(file, searchstrings)
    if searchstringfound
        for line in 1:linenumber
            currentline = readline(file)
        end
        words = split(currentline)
        return words[wordnumber+1]
    end
    error("The combination of search strings was not found in the output file!")
end

"""
This version is used if only one parse is supposed to be done and then the file closed again.
"""
function parse_output(filename, searchstrings, linenumber, wordnumber)
    file = open(filename)
    word = parse_output(file, searchstrings, linenumber, wordnumber)
    close(file)
    return word
end

function read_until_hit(file, searchstrings)
    currentline = ""
    searchstringfound=false
    for searchstring in searchstrings
        searchstringfound=false
        while (!eof(file) && !searchstringfound)
            currentline = readline(file)
            searchstringfound = occursin(searchstring, currentline)
        end
    end
    return searchstringfound, currentline
end

function parse_type(file, searchstrings, linenumber, wordnumber, typ)
    str = parse_output(file, searchstrings, linenumber, wordnumber)
    value = try
        parse(typ, str)
    catch e
        if isa(e, ArgumentError)
            error("The word encountered at the specified location in the output file cannot be interpreted as type $(typ)!")
        else
            throw(e)
        end
    end
    return value
end

parse_float(file, searchstrings, linenumber, wordnumber) = parse_type(file, searchstrings, linenumber, wordnumber, Float64)
parse_int(file, searchstrings, linenumber, wordnumber) = parse_type(file, searchstrings, linenumber, wordnumber, Int64)

end
