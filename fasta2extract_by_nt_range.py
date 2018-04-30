#!/usr/bin/env python3

import sys
from Bio import SeqIO
import gzip

fasta_file = sys.argv[1]

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fasta")
else :
    ffile = SeqIO.parse(fasta_file, "fasta")

#for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
total_length = 0;
order = 0;
fromNK = int(sys.argv[2])
toNK = int(sys.argv[3])

for seq_record in ffile:
    order += 1;
    seqlen = len(seq_record)
    if(seqlen + total_length > fromNK):
        printNkBeg = int(max((fromNK - total_length) - 1, 0))
        printNkEnd = int(min((toNK - total_length), seqlen - 1))
        print(">",seq_record.name,"_contig_",order, "_len_", len(seq_record),"_from_",printNkBeg+1,"_to_",printNkEnd+1,sep='')
        print(seq_record.seq[printNkBeg:printNkEnd])
    total_length += seqlen;
    if(total_length >= toNK):
        break;