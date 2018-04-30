#!/usr/bin/env python3

from Bio import SeqIO
import sys
import gzip

fasta_file = sys.argv[1]

if fasta_file[-2:] == "gz":
    ffile = SeqIO.parse(gzip.open(fasta_file, "rt"), "fasta")
else :
    ffile = SeqIO.parse(fasta_file, "fasta")

header_set = set(line.strip() for line in open(sys.argv[2]))

for seq_record in ffile:
    try:
        header_set.remove(seq_record.name)
        print(seq_record.format("fasta"))
    except KeyError:
        continue
if len(header_set) != 0:
    print(len(header_set),'headers from list were not identified in the input fasta.', file=sys.stderr)
