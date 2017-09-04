#!/usr/bin/env python3

import os
import sys
import pysam
from Bio import SeqIO, Seq, SeqRecord

#sam_filename = 'ten_reads_map.bam'
#samfile = pysam.AlignmentFile(sam_filename, "rb")
samfile = pysam.AlignmentFile(sys.argv[1], "rb")

# header_list_filename = 'list_of_scaffolds_to_filter'
# header_set = set(line.strip() for line in open(header_list_filename))
header_set = set(line.strip() for line in open(sys.argv[2]))

base = sys.argv[3]
out_R1 = base + 'R1_filtered.fq'
out_R2 = base + 'R2_filtered.fq'

with open(out_R1, mode='w') as R1, open(out_R2, mode='w') as R2:
	for entry in samfile:
		if entry.is_read1 and not entry.reference_name in header_set:
			# pait pair
			entry_R2 = samfile.mate(entry)
			# do some sequence gymnastics with R1
			seq_R1 = Seq.Seq(entry.seq)
			if entry.is_reverse :
				seq_R1 = seq_R1.reverse_complement()
			# do some sequence gymnastics with R2
			seq_R2 = Seq.Seq(entry_R2.seq)
			if entry_R2.is_reverse :
				seq_R2 = seq_R2.reverse_complement()
			R1.write('@' + entry.qname + '\n' + str(seq_R1) + '\n+\n' + entry.qqual + '\n')
			R2.write('@' + entry_R2.qname + '\n' + str(seq_R2) + '\n+\n' + entry_R2.qqual + '\n')


samfile.close()
