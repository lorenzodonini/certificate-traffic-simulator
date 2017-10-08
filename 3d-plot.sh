#!/bin/bash

OUT=full.png

#TITLE="Certificate Renewal Traffic"
#if [ "$2" == "-r" ]; then
#    TITLE="Certificate Renewal Traffic (random backoff)"
#fi


gnuplot << eor
set terminal png size 1920,1080
set output "$OUT"
#set style data linespoints
set datafile separator ","
set ylabel "Time (seconds)"
set zlabel "Total services"
set zlabel "Traffic (bytes)"
#plot "$1" using 1:3:4 title "$TITLE"
splot 'full_sim/full_1_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow1", \
    'full_sim/full_2_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow2", \
    'full_sim/full_3_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow3", \
    'full_sim/full_4_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow4", \
    'full_sim/full_5_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow5", \
    'full_sim/full_6_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow6", \
    'full_sim/full_7_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow7", \
    'full_sim/full_8_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow8", \
    'full_sim/full_9_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow9", \
    'full_sim/full_10_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow10", \
    'full_sim/full_11_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow11", \
    'full_sim/full_12_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow12", \
    'full_sim/full_13_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow13", \
    'full_sim/full_14_5000.csv' using 3:1:4 with points palette pointsize 1 pointtype 5 title "Flow14"
eor