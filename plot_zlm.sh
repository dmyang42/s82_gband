#!/bin/zsh
s=$1
python s82_gband.py $s > s82_$s
python z_plot.py $s
python M_plot.py $s
python L_plot.py $s