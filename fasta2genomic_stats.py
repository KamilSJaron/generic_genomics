#!/usr/bin/env python3

import sys
from Bio import SeqIO
import gzip

lengths = []
filename = sys.argv[1]

if filename[-2:] == 'gz' :
	handle = gzip.open(filename, "rt")
else :
	handle = open(filename, 'r')

for seq_record in SeqIO.parse(handle, "fasta"):
    lengths.append(len(seq_record))

total_sum = sum(lengths)
numer_of_records = len(lengths)
tenth_of_sequences = total_sum / 10

if len(sys.argv) >= 3:
    half_of_genome = int(sys.argv[2]) / 2
else:
    half_of_genome = total_sum / 2

lengths.sort(reverse=True)

print("Total sum of lengths:\t" + str(total_sum))
print("Number of records:\t" + str(numer_of_records))

# X is just an X / 10 from NX. for X = 1; it computes N10, for X = 2 it computes N20 etc.
X = 1
cumsum = 0
LX = 0
NG50 = 0
LG50 = 0

for seq_len in lengths:
    cumsum += seq_len
    LX += 1
    if cumsum > half_of_genome and NG50 == 0:
        NG50 = seq_len
        LG50 = LX
    if cumsum > tenth_of_sequences * X:
        if X <= 8:
            print("L" + str(X) + "0 and N" + str(X) + "0 are: " + str(LX) + "\t" + str(seq_len))
        if X >= 8 and NG50 != 0:
            break;
        X += 1;

print("LG50 and NG50 are:\t" + str(LG50) + "\t" + str(NG50))
