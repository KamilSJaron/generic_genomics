import sys
from Bio import SeqIO 

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    print(len(seq_record))
