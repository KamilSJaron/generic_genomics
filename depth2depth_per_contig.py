#!/usr/bin/env python3

import sys

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

first_line = next(open(sys.argv[1], "r")).split('\t')
depth = 0
last_entry = first_line[0]

for depthline in open(sys.argv[1], "r"):
    depth_tab = depthline.split('\t')

    if(depth_tab[0] != last_entry):
      print(last_entry, depth, sep = '\t')
      depth = int(depth_tab[2])
    else:
      depth += int(depth_tab[2])

    last_size = int(depth_tab[1])
    last_entry = depth_tab[0]

print(last_entry, depth, sep = '\t')
