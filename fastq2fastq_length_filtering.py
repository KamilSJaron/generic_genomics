#!/usr/bin/env python3

import sys
from Bio import SeqIO
import gzip

fasta_file = sys.argv[1]
treshold = int(sys.argv[2])

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fastq")
else :
    ffile = SeqIO.parse(fasta_file, "fastq")

for seq_record in ffile:
    if(len(seq_record) > treshold):
        print(seq_record.format("fastq"), end='')
