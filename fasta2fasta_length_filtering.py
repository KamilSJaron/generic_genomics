#!/usr/bin/env python3

import sys
import gzip

fasta_file = sys.argv[1]

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fasta")
else :
    ffile = SeqIO.parse(fasta_file, "fasta")

treshold = int(sys.argv[2])

for seq_record in ffile:
    if(len(seq_record) > treshold):
        print(seq_record.format("fasta"))

