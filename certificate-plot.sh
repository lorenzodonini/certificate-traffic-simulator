#!/bin/bash

gnuplot << eor
set terminal pdf
set output "output/full_certificate_lifetime.pdf"
set style data linespoints
set datafile separator ","
set xlabel "Certificate Lifetime (seconds)" font 'Helvetica, 18'
set ylabel "Average Traffic (B/s)" font 'Helvetica, 18'
set tics font 'Helvetica, 14'
set lmargin 10
set rmargin 5
set bmargin 5
plot "output/full_certificate_lifetime.csv" using 2:1 notitle
eor