#!/bin/bash

### INPUT ###
# bam file
# list of scaffolds to filter
# R1 / R2.fq.gz reads
#############

# bam=ten_reads_map.bam
# list=list_of_scaffolds_to_filter
# R1=ten_reads_R1.fq
# R2=ten_reads_R2.fq

keep=list_of_reads_to_keep

bam=$1
list=$2
R1=$3
R2=$4

# get list of reads
samtools view $bam | grep -vf $list | cut -f 1 | uniq > $keep

grep -A 3 -f $keep $R1 > $(basename $R1 .fq)_filtered_bash.fq
grep -A 3 -f $keep $R2 > $(basename $R2 .fq)_filtered_bash.fq

rm $keep
