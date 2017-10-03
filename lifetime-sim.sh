#!/bin/bash

# Simulation goes from certificate validity 1000 (16 minutes) to 20000 (330 minutes = 5.5 hours)

for i in {1..20}; do
    python3 simulation.py -n 20 -nc $(expr 1000 \* $i / 2) -s 30 -cv $(expr 1000 \* $i) -cr 2500 -d 100000 -o lifetime_"$i"000.csv
done
