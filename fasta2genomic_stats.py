import sys
from Bio import SeqIO 

lengths = []

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    lengths.append(len(seq_record))

lengths.sort(reverse=True)

if len(sys.argv) == 3:
    half_of_genome = int(sys.argv[2]) / 2
else:
    half_of_genome = sum(lengths) / 2

if(half_of_genome > sum(lengths)):
    print("Half of the specified genome length:", half_of_genome)
    print("is greater than total sum of sequences in fasta: ", sum(lengths))
    sys.exit()

cumsum = 0
L50 = 0

for seq_len in lengths:
    cumsum += seq_len
    L50 += 1
    if cumsum > half_of_genome:
        print("Total sum of lengths: ", sum(lengths))
        print("Number of records: ", len(lengths))
        print("N50 is: ", seq_len)
        print("L50 is: ", L50)
        break;
