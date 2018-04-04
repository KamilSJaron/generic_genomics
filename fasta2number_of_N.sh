#!/bin/bash

# 1st argument is path to fasta file
# print filename and its number of nucleotides

echo -e $1'\t'$(zcat $1 | grep -v ">" | tr -cd N | wc -c)
