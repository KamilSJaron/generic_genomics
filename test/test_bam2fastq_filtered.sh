#!/bin/bash

mkdir playground && cd playground

echo "1_Tdi_b3v04_scaf000004" > list_to_test
echo "1_Tdi_b3v04_scaf000005" >> list_to_test

../bam2fastq_filtered.py ../test/data/ten_reads_map.bam list_to_test filt_one
../bam2fastq_filtered.py --both ../test/data/ten_reads_map.bam list_to_test filt_both
../bam2fastq_filtered.py --keep ../test/data/ten_reads_map.bam list_to_test keep_one
../bam2fastq_filtered.py --keep --both ../test/data/ten_reads_map.bam list_to_test keep_both

if [[ $(zcat filt_one_R1.fastq.gz | wc -l) -eq 24 ]]; then
   echo "filter one works";
fi

if [[ $(zcat filt_both_R1.fastq.gz | wc -l) -eq 28 ]]; then
   echo "filter one works";
fi

if [[ $(keep_one_R1.fastq.gz | wc -l) -eq 16 ]]; then
   echo "filter one works";
fi

if [[ $(zcat keep_both_R1.fastq.gz | wc -l) -eq 12 ]]; then
   echo "filter one works";
fi

# cd ..
# rm -r playground