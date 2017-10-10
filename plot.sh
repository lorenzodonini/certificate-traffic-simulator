#!/bin/bash

OUT="$1".pdf

TITLE="Certificate Renewal Traffic"
if [ "$2" == "-r" ]; then
    TITLE="Certificate Renewal Traffic (random backoff)"
fi


gnuplot << eor
set terminal pdf
set output "$OUT"
#set style data linespoints
set datafile separator ","
set pointsize 0.5
set xlabel "Time (seconds)" font 'Helvetica, 18'
set ylabel "Traffic (Bytes)" font 'Helvetica, 18'
set lmargin 12
set rmargin 5
set bmargin 5
set yrange [0:35000]
set tics font 'Helvetica, 14'
plot "$1" using 1:4 notitle
#plot "$1" using 1:4 title "$TITLE"
eor