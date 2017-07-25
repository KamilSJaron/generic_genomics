#!/usr/bin/env python3

import os
import sys
import pysam
from Bio import SeqIO, Seq, SeqRecord

#sam_filename = 'ten_reads_map.bam'
#samfile = pysam.AlignmentFile(sam_filename, "rb")-
samfile = pysam.AlignmentFile(sys.argv[1], "rb")

######
# SORT SAM BY NAME FIRST
######

# header_list_filename = 'list_of_scaffolds_to_filter'
# header_set = set(line.strip() for line in open(header_list_filename))
header_set = set(line.strip() for line in open(sys.argv[2]))

base = sys.argv[3]
out_R1 = base + 'R1_filtered.fq'
out_R2 = base + 'R2_filtered.fq'

with open(out_R1, mode='w') as R1, open(out_R2, mode='w') as R2:
	for entry in samfile:
		if not entry.reference_name in header_set:
			seq = Seq.Seq(entry.seq)
			if entry.is_reverse :
				seq = seq.reverse_complement()
			if entry.is_read1:
				R1.write(entry.qname + '\n' + str(seq) + '\n+\n' + entry.qqual + '\n')
			else:
				R2.write(entry.qname + '\n' + str(seq) + '\n+\n' + entry.qqual + '\n')

samfile.close()
