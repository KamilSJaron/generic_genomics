#!/usr/bin/env python3

import sys
from Bio import SeqIO
from mimetypes import guess_type
import gzip

fasta_file = sys.argv[1]
Cname = sys.argv[2]

encoding = guess_type(fasta_file)[1]
_open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open

with _open(fasta_file) as ffile:
    for seq_record in SeqIO.parse(ffile, 'fasta'):
        if(seq_record.name == Cname):
    	print(seq_record.format("fasta"))
            sys.exit()
    print('Did not found sequence of input name');

