#!/usr/bin/env python3

import sys
from Bio import SeqIO
import gzip

fasta_file = sys.argv[1]

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fasta")
else :
    ffile = SeqIO.parse(fasta_file, "fasta")

for seq_record in ffile:
    seq_record.seq = seq_record.seq.upper()
    print(seq_record.format("fasta"))

