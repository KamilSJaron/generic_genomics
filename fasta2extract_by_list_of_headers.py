from Bio import SeqIO
import sys

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

ffile = SeqIO.parse(sys.argv[1], "fasta")
header_set = set(line.strip() for line in open(sys.argv[2]))

for seq_record in ffile:
    try: 
        header_set.remove(seq_record.name)
        print(">",seq_record.name,sep='')
        print(seq_record.seq)
    except KeyError:
        continue
if len(header_set) != 0:
    print(len(header_set),'headers from list were not identified in the input fasta.', file=sys.stderr)
