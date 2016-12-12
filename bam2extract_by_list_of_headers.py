#!/usr/bin/env python3

import sys
import pysam

# funky_scafolds.list
# ../contig_filtering/Tge_pe_700.bam
samfile = pysam.AlignmentFile(sys.argv[1], "rb")
# header set
header_set = set(line.strip() for line in open(sys.argv[2]))
original_headers = samfile.header

# headers
# @HD line
head = original_headers['HD']
print('@HD\tVN:{:s}\tSO:{:s}'.format(head['VN'], head['SO']))

# @SQ lines
for reference in original_headers['SQ']:
	if reference['SN'] in header_set:
		print('@SQ\tSN:{:s}\tLN:{:s}'.format(reference['SN'], str(reference['LN'])))

# @PG line
program = original_headers['PG'][0]
print('@PG\tVN:{:s}\tID:{:s}\tCL:{:s}'.format(program['VN'], program['ID'], program['CL']))

# print entries in list
for entry in samfile:
	try:
		if entry.reference_name in header_set:
			print( str(entry))
	except (ValueError, TypeError) as e:
		continue;

samfile.close()
