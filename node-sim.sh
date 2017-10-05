#!/bin/bash

# Simulation goes from 1 node to 20 nodes. Each node runs 30 services by default. Default certificate validity is 10000

for i in $(seq $1 $2); do
    for j in {1..20}; do
        python3 simulation.py -n "$i" -nc $(expr 1000 \* $j / 2) -s 30 -cv $(expr 1000 \* $j) -cr 2500 -d 100000 -o full_"$i"_"$j"000.csv
    done
    #python3 simulation.py -n "$i" -nc 4000 -s 30 -cv 10000 -cr 2500 -d 100000 -o node_"$i".csv
done
