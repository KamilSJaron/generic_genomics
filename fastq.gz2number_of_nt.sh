#!/bin/bash

# 1st argument is path to gz fastq file
# print filename and its number of nucleotides

echo -e $1'\t'$(gunzip -c $1 | sed -n '2~4p' | tr -d "\n" | wc -c)
