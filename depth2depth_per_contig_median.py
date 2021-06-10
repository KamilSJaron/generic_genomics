#!/usr/bin/env python3

import sys
from statistics import median
import argparse

parser = argparse.ArgumentParser(description="from per base depth (samtools depth) calculate per scf coverage median")
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='depth file (default: stdandard input)')
args = parser.parse_args()

depths = []
last_entry = ''

for depthline in args.infile:
    depth_tab = depthline.split('\t')

    if last_entry == '':
        last_entry = depth_tab[0]

    if(depth_tab[0] != last_entry):
      print(last_entry, median(depths), sep = '\t')
      depths = [int(depth_tab[2])]
    else:
      depths.append(int(depth_tab[2]))

    last_size = int(depth_tab[1])
    last_entry = depth_tab[0]

print(last_entry, median(depths), sep = '\t')
