import sys
from Bio import SeqIO

record = SeqIO.parse(sys.argv[1],"genbank")
record.features = [f for f in record.features if f.type == "CDS"]
SeqIO.write(record, sys.argv[2], "fasta")


record = SeqIO.parse("GenDB_Pseudomonas_protegens_S5.gbk","genbank")

for seq in record:
	seq.features = [f for f in seq.features if f.type == "CDS"]
	print(seq.seq)


	for f in seq.features:
		if f.type == 'CDS':
			print(f.seq)