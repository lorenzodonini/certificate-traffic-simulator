#!/bin/bash

OUT="$1".png

TITLE="Certificate Renewal Traffic"
if [ "$2" == "-r" ]; then
    TITLE="Certificate Renewal Traffic (random backoff)"
fi


gnuplot << eor
set terminal png size 1920,1080
set output "$OUT"
#set style data linespoints
set datafile separator ","
set xlabel "Time (seconds)"
set ylabel "Traffic (bytes)"
plot "$1" using 1:4 title "$TITLE"
eor