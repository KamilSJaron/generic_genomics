import sys
from Bio import SeqIO

ffile = SeqIO.parse(sys.argv[1], "fastq")
treshold = int(sys.argv[2])

for seq_record in ffile:
    if(len(seq_record) > treshold):
        print(">"+seq_record.name)
        print(seq_record.seq)

