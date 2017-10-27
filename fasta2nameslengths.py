#!/usr/bin/env python3

import sys
from Bio import SeqIO

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    print(seq_record.name, len(seq_record), sep = '\t')
