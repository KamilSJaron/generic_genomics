import sys
from Bio import SeqIO

lengths = []

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    lengths.append(len(seq_record))

lengths.sort(reverse=True)

if len(sys.argv) == 3:
    tenth_of_genome = int(sys.argv[2]) / 10
else:
    tenth_of_genome = sum(lengths) / 10

if(tenth_of_genome * 8 > sum(lengths)):
    print("80\% of the specified genome length:", tenth_of_genome * 8)
    print("is greater than total sum of sequences in fasta: ", sum(lengths))
    sys.exit()

cumsum = 0
LX = 0

print("Total sum of lengths:\t" + str(sum(lengths)))
print("Number of records:\t" + str(len(lengths)))

# X is just an X / 10 from NX. for X = 1; it computes N10, for X = 2 it computes N20 etc.
X = 1

for seq_len in lengths:
    cumsum += seq_len
    LX += 1
    if cumsum > tenth_of_genome * X:
        print("L" + str(X) + "0 and N" + str(X) + "0 are: " + str(LX) + "\t" + str(seq_len))
        if X == 8:
            break;
        X += 1;
