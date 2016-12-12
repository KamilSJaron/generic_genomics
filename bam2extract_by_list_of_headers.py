#!/usr/bin/env python3

import sys
import pysam

# funky_scafolds.list
# ../contig_filtering/Tge_pe_700.bam
samfile = pysam.AlignmentFile(sys.argv[1], "rb")
filtered = pysam.AlignmentFile(sys.argv[3], "wb", template=samfile)
# header set
header_set = set(line.strip() for line in open(sys.argv[2]))
original_headers = samfile.header
#new_headers = dict()

# headers
# @HD line
#new_headers['HD'] = original_headers['HD']
# @SQ lines
#new_headers['SQ'] = list()
#for reference in original_headers['SQ']:
#	if reference['SN'] in header_set:
#		new_headers['SQ'].append(reference)
# @PG line
#new_headers['PG'] = original_headers['PG']

# filtered = pysam.AlignmentFile(sys.argv[3], "wb", header=new_headers)

# print entries in list
for entry in samfile:
	try:
		if entry.reference_name in header_set:
			filtered.write(entry)
	except (ValueError, TypeError):
		continue;

samfile.close()
