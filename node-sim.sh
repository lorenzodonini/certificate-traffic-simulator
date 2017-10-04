#!/bin/bash

# Simulation goes from 1 node to 20 nodes. Each node runs 30 services by default. Default certificate validity is 10000

for i in {1..20}; do
    python3 simulation.py -n "$i" -nc 4000 -s 30 -cv 10000 -cr 2500 -d 100000 -o node_"$i".csv
done

#python3 simulation.py -n 20 -nc 5000 -s 30 -cv 5000 -cr 2500 -d 100000 -o lifetime_5000.csv
