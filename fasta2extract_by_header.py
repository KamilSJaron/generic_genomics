#!/usr/bin/env python3

import sys
from Bio import SeqIO
import gzip

fasta_file = sys.argv[1]
Cname = sys.argv[2]

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fasta")
else :
    ffile = SeqIO.parse(fasta_file, "fasta")

for seq_record in ffile:
    if(seq_record.name == Cname):
        print(seq_record.format("fasta"))
        sys.exit()
print('Did not found sequence of input name');
