#!/bin/bash

gnuplot << eor
set terminal pdf
set datafile separator ","
set output "$1.pdf"
set xlabel "Amount of Services" font 'Helvetica, 18'
set ylabel "Traffic (B/s)" font 'Helvetica, 18'
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
set yrange [0:35000]
set tics font 'Helvetica, 14'

plot "$1_1_5000.csv" using 3:4 notitle, \
    "$1_2_5000.csv" using 3:4 notitle, \
    "$1_3_5000.csv" using 3:4 notitle, \
    "$1_4_5000.csv" using 3:4 notitle, \
    "$1_5_5000.csv" using 3:4 notitle, \
    "$1_6_5000.csv" using 3:4 notitle, \
    "$1_7_5000.csv" using 3:4 notitle, \
    "$1_8_5000.csv" using 3:4 notitle, \
    "$1_9_5000.csv" using 3:4 notitle, \
    "$1_10_5000.csv" using 3:4 notitle, \
    "$1_11_5000.csv" using 3:4 notitle, \
    "$1_12_5000.csv" using 3:4 notitle, \
    "$1_13_5000.csv" using 3:4 notitle, \
    "$1_14_5000.csv" using 3:4 notitle, \
    "$1_15_5000.csv" using 3:4 notitle, \
    "$1_16_5000.csv" using 3:4 notitle, \
    "$1_17_5000.csv" using 3:4 notitle, \
    "$1_18_5000.csv" using 3:4 notitle, \
    "$1_19_5000.csv" using 3:4 notitle, \
    "$1_20_5000.csv" using 3:4 notitle
eor