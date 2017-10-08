#!/bin/bash

gnuplot << eor
set terminal pdf
set datafile separator ","
set output "full_services.pdf"
set xlabel "Amount of Services" font 'Helvetica, 18'
set ylabel "Generated Traffic (Bytes)" font 'Helvetica, 18'
#set style fill solid 0.25
#set boxwidth 2
#set pointsize 0.5
set style fill solid 0.5 border -1
set style boxplot outliers pointtype 1
set style data boxplot
set boxwidth  25.0
set pointsize 0.5
set lmargin 10
set rmargin 5
set bmargin 5
set xrange [0:620]
set yrange [0:55000]
set tics font 'Helvetica, 14'

plot "$1/full_1_5000.csv" using 3:4 notitle, \
    "$1/full_2_5000.csv" using 3:4 notitle, \
    "$1/full_3_5000.csv" using 3:4 notitle, \
    "$1/full_4_5000.csv" using 3:4 notitle, \
    "$1/full_5_5000.csv" using 3:4 notitle, \
    "$1/full_6_5000.csv" using 3:4 notitle, \
    "$1/full_7_5000.csv" using 3:4 notitle, \
    "$1/full_8_5000.csv" using 3:4 notitle, \
    "$1/full_9_5000.csv" using 3:4 notitle, \
    "$1/full_10_5000.csv" using 3:4 notitle, \
    "$1/full_11_5000.csv" using 3:4 notitle, \
    "$1/full_12_5000.csv" using 3:4 notitle, \
    "$1/full_13_5000.csv" using 3:4 notitle, \
    "$1/full_14_5000.csv" using 3:4 notitle, \
    "$1/full_15_5000.csv" using 3:4 notitle, \
    "$1/full_16_5000.csv" using 3:4 notitle, \
    "$1/full_17_5000.csv" using 3:4 notitle, \
    "$1/full_18_5000.csv" using 3:4 notitle, \
    "$1/full_19_5000.csv" using 3:4 notitle, \
    "$1/full_20_5000.csv" using 3:4 notitle
eor