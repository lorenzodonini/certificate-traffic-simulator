#!/bin/bash

# Simulation goes from 1 node to 20 nodes. Each node runs 30 services by default. Default certificate validity is 10000

for i in $(seq $1 $2); do
    for j in {1..20}; do
        #python3 simulation.py -n "$i" -nc 2500 -s 30 -cv $(expr 1000 \* $j) -cr $(expr 250 \* $j) -d 100000 -o simr_"$i"n_"$j"000cv.csv
        python3 simulation.py -n "$i" -nc 2500 -s 30 -si 1 -cv $(expr 1000 \* $j) -cr 0 -d 100000 -o simf_"$i"n_"$j"000cv.csv
        #python3 simulation.py -n "$i" -nc $(expr 1000 \* $j / 2) -s 30 -cv $(expr 1000 \* $j) -cr $(expr 250 \* $j) -d 100000 -o full_"$i"_"$j"000.csv
    done
done
