import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import matplotlib
import sys

outfolder = sys.argv[1]

matplotlib.rc('font', size=8)

def mantissa_exp(x):
    (sign, digits, exponent) = Decimal(x).as_tuple()  # this is the exponent required to move the decimal point from after the last digit to the correct position
    exponent = len(digits) + exponent - 1
    mantissa = round(x/(10**exponent), ndigits=1)
    return mantissa, exponent

def nicestring(x):
    mantissa, exponent = mantissa_exp(x)
    mantissa = str(mantissa)
    exponent = str(exponent)
    return r"$\rho = "+mantissa+r"\times"+"10^{"+exponent+"}$"

saved_rho = np.loadtxt(f"{outfolder}/saved_rho_selected")

coords = []
for i in range(1,6+1):
    coords.append(np.loadtxt(f"{outfolder}/sample{i}_planebasis"))

fig, axes = plt.subplots(2, 3, figsize=(4, 3), sharex=True, sharey=True)    # create 2 rows with 3 plots each

size_deuteron = 80
size_electron = 20
value_range = [-2, 2]

counter = 0
for row in range(2):
    for col in range(3):
        axes[row,col].set_xlim(value_range)
        axes[row,col].set_ylim(value_range)
        if (row==1):
            axes[row,col].set_xlabel("x / Bohrs")
        if (col==0):
            axes[row,col].set_ylabel("y / Bohrs")
        axes[row,col].set(adjustable='box', aspect='equal')    # this ensures that the subplots are square
        axes[row,col].set_xticks([-2,0,2])
        for i in range(3):    # plot deuterons
            axes[row,col].scatter(coords[counter][0,i], coords[counter][1,i], s=size_deuteron, c='tab:blue')
        for i in range(3,5):  # plot electrons
            axes[row,col].scatter(coords[counter][0,i], coords[counter][1,i], s=size_electron, c='tab:red')
        axes[row,col].text(0, -1.5, str(nicestring(saved_rho[counter])), horizontalalignment='center', verticalalignment='center')
        counter += 1

plt.savefig(f"{outfolder}/D3plus_randomsamples.png", dpi=300)


