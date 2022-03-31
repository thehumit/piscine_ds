#!/bin/sh

head -1 < hh.csv > hh_sorted.csv
tail -20 < hh.csv | sort -k2,2 -k1,1 >> hh_sorted.csv