This is the Snakemake workflow for reproducing the data analysis of [our paper](https://doi.org/10.26434/chemrxiv-2023-mrxng).

You need to have [Julia](https://julialang.org/) with the [MolStructSampling.jl](https://github.com/LucasLang/MolStructSampling.jl/) package installed and [Snakemake](https://snakemake.readthedocs.io) in your path.

Basic settings for the sampling and analysis can be set in `config/config.yaml`.

Usage:
```bash
cd workflow
snakemake -c1 --use-conda
```
