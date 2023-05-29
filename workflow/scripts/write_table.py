import sys
import numpy as np

folder = sys.argv[1]

Etot_sampling = round(np.loadtxt(f"{folder}/Etot_sampling").item(), 3)
Etot_analytical = round(np.loadtxt(f"{folder}/Etot_analytical").item(), 3)
rDD_sampling = round(np.loadtxt(f"{folder}/rDD_sampling").item(), 3)
rDD_analytical = round(np.loadtxt(f"{folder}/rDD_analytical").item(), 3)
rDe_sampling = round(np.loadtxt(f"{folder}/rDe_sampling").item(), 3)
rDe_analytical = round(np.loadtxt(f"{folder}/rDe_analytical").item(), 3)
ree_sampling = round(np.loadtxt(f"{folder}/ree_sampling").item(), 3)
ree_analytical = round(np.loadtxt(f"{folder}/ree_analytical").item(), 3)


table = fr"""\begin{{tabular}}{{lcccc}}
\hline \hline
& $\langle E_\text{{tot}} \rangle $ & $\langle r_\text{{DD}} \rangle $ & $\langle r_\text{{De}} \rangle$ & $\langle r_\text{{ee}} \rangle$ \\ \hline
Analytical: & ${Etot_analytical}$ & ${rDD_analytical}$ & ${rDe_analytical}$ & ${ree_analytical}$ \\
Sample: & ${Etot_sampling}$ & ${rDD_sampling}$ & ${rDe_sampling}$ & ${ree_sampling}$ \\ \hline\hline
\end{{tabular}}"""

with open(f"{folder}/table.tex", "w") as outfile:
    print(table, file=outfile)
