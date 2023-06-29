import sys
import numpy as np

folder = sys.argv[1]

r = np.loadtxt(f"{folder}/startconfig_ppcoord")
r_COM = np.round(np.loadtxt(f"{folder}/startconfig_COM"), decimals = 4)

table_pp = fr"""\begin{{tabular}}{{cccc}}
\hline\hline
 & $x$ & $y$ & $z$ \\ \hline
 $r_{{\text{{D}}_1\text{{D}}_2}}$ & ${r[0]}$ & ${r[1]}$ & ${r[2]}$ \\
 $r_{{\text{{D}}_1\text{{D}}_3}}$ & ${r[3]}$ & ${r[4]}$ & ${r[5]}$ \\
 $r_{{\text{{D}}_1\text{{e}}_1}}$ & ${r[6]}$ & ${r[7]}$ & ${r[8]}$ \\
 $r_{{\text{{D}}_1\text{{e}}_2}}$ & ${r[9]}$ & ${r[10]}$ & ${r[11]}$ \\ \hline\hline
\end{{tabular}}"""  # literal curly braces in the string must be repeated!

table_COM = fr"""\begin{{tabular}}{{cccc}}
\hline\hline
 & $x$ & $y$ & $z$ \\ \hline
 $R^\text{{COM}}_{{\text{{D}}_1}}$ & ${r_COM[0,0]}$ & ${r_COM[1,0]}$ & ${r_COM[2,0]}$ \\
 $R^\text{{COM}}_{{\text{{D}}_2}}$ & ${r_COM[0,1]}$ & ${r_COM[1,1]}$ & ${r_COM[2,1]}$ \\
 $R^\text{{COM}}_{{\text{{D}}_3}}$ & ${r_COM[0,2]}$ & ${r_COM[1,2]}$ & ${r_COM[2,2]}$ \\
 $R^\text{{COM}}_{{\text{{e}}_1}}$ & ${r_COM[0,3]}$ & ${r_COM[1,3]}$ & ${r_COM[2,3]}$ \\
 $R^\text{{COM}}_{{\text{{e}}_2}}$ & ${r_COM[0,4]}$ & ${r_COM[1,4]}$ & ${r_COM[2,4]}$ \\ \hline\hline
\end{{tabular}}"""  # literal curly braces in the string must be repeated!

with open(f"{folder}/table_pp.tex", "w") as outfile:
    print(table_pp, file=outfile)

with open(f"{folder}/table_COM.tex", "w") as outfile:
    print(table_COM, file=outfile)
