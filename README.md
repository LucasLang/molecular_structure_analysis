This is the Snakemake workflow for reproducing the data analysis of [our paper on a quantum definition of molecular structure](https://doi.org/10.26434/chemrxiv-2023-mrxng).

In order to execute the workflow, you need to have [Julia](https://julialang.org/) with the [MolStructSampling.jl](https://github.com/LucasLang/MolStructSampling.jl/), [NPZ.jl](https://www.juliapackages.com/p/npz), and [ProgressBars.jl](https://www.juliapackages.com/p/progressbars) packages installed and [Snakemake](https://snakemake.readthedocs.io) in your path.

Once you have Julia, you can install the required packages via starting the Julia REPL by typing `julia` in a terminal, then entering Pkg mode by pressing the `]` key and entering the following commands:
- `add https://github.com/LucasLang/MolStructSampling.jl.git`
- `add ProgressBars`
- `add NPZ`

In order to install Snakemake, you can e.g. enter the following commands (requires conda, e.g. through a [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/free/anaconda/install/) installation):
```bash
conda create --name snakemake python=3.11
conda activate snakemake
conda install -c conda-forge -c bioconda snakemake
```

Basic settings for the sampling and analysis can be set in `config/config.yaml`.

Usage:
```bash
cd workflow
snakemake -c1 --use-conda
```
