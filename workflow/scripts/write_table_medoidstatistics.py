import sys
import numpy as np

offsetinterval = int(sys.argv[1])
nstatistics = int(sys.argv[2])
path = sys.argv[3]

all_sidelengths = []
all_average_sidelengths = []
all_maxminratios = []
for i in range(nstatistics):
    foldername = f"{path}/offset{(i+1)*offsetinterval}"
    sidelengths = np.loadtxt(f"{foldername}/sidelengths")
    average_sidelength = np.mean(sidelengths)
    maxminratio = np.max(sidelengths)/np.min(sidelengths)
    all_sidelengths.append(sidelengths)
    all_average_sidelengths.append(average_sidelength)
    all_maxminratios.append(maxminratio)
mu_average = np.mean(all_average_sidelengths)
sigma_average = np.std(all_average_sidelengths, ddof = 1)   # ddof = 1 for less biased estimator of population std
mu_maxmin = np.mean(all_maxminratios)
sigma_maxmin = np.std(all_maxminratios, ddof = 1)

# all_sidelengths = np.round(all_sidelengths, decimals = 3)
# all_average_sidelengths = np.round(all_average_sidelengths, decimals = 3)
# all_maxminratios = np.round(all_maxminratios, decimals = 3)
# 
# mu_average = np.round(mu_average, decimals = 3)
# sigma_average = np.round(sigma_average, decimals = 3)
# mu_maxmin = np.round(mu_maxmin, decimals = 3)
# sigma_maxmin = np.round(sigma_maxmin, decimals = 3)

table = fr"""\begin{{tabular}}{{lccccc}}
\hline \hline
$n$ & $r_{{\text{{D}}_1\text{{D}}_2}}$ & $r_{{\text{{D}}_1\text{{D}}_3}}$ & $r_{{\text{{D}}_2\text{{D}}_3}}$ & $\bar{{r}}_\text{{DD}}$ & $r_\text{{DD}}^\text{{max}} / r_\text{{DD}}^\text{{min}}$ \\ \hline"""

table += "\n"

for n in range(nstatistics):
    table += fr"{n+1} & {all_sidelengths[n][0]:5.3f} & {all_sidelengths[n][1]:5.3f} & {all_sidelengths[n][2]:5.3f} & {all_average_sidelengths[n]:5.3f} & {all_maxminratios[n]:5.3f}"
    if n < (nstatistics-1):
        table += r"\\ "+"\n"
table += r"\\ \hline" + "\n"
table += fr"$\mu$ & & & & {mu_average:5.3f} & {mu_maxmin:5.3f} \\ " + "\n"
table += fr"$\sigma$ & & & & {sigma_average:5.3f} & {sigma_maxmin:5.3f} \\ \hline \hline" + "\n"
table += r"\end{tabular}"

with open(f"{path}/medoid_statistics.tex", "w") as outfile:
    print(table, file=outfile)

x="""
Analytical: & ${Etot_analytical}$ & ${rDD_analytical}$ & ${rDe_analytical}$ & ${ree_analytical}$ \\
Sample: & ${Etot_sampling}$ & ${rDD_sampling}$ & ${rDe_sampling}$ & ${ree_sampling}$ \\ \hline\hline
\end{{tabular}}"""

