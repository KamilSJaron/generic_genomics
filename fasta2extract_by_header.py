import sys
from Bio import SeqIO

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

ffile = SeqIO.parse(sys.argv[1], "fasta")
Cname = sys.argv[2]

for seq_record in ffile:
    if(seq_record.name == Cname):
	print(seq_record.format("fasta"))
        sys.exit()
print('Did not found sequence of input name');
