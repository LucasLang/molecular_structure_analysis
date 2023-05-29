#!/usr/bin/env bash

# to print coefficients, run with argument "coeffs", otherwise, run with argument "orig"
singularity run --bind $(pwd) /home/llang/Dropbox/Postdoc/work/projects/nonBO/software/containers/ocelote/ocelote $1
