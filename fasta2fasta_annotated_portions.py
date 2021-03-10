
import argparse
import sys
from Bio import SeqIO

if __name__ == "__main__":
    args = None
    if len(sys.argv) == 1:
        args = ["--help"]

    parser = argparse.ArgumentParser(description="Subset a genome that contains annotated genes.")
    parser.add_argument('-g', '-genome', help='genome file (.fasta, can be gzipped)')
    parser.add_argument('-a', '-annotayion', help="annotation file (.gff3, can be gzipped)")
    parser.add_argument('-f', '-feature', help='feature used for filtering (default: "any")', default='any')

    args = parser.parse_args(args)

    sys.stderr.write("processing {} annotation file\n".format(args.a))
    with open(args.a, 'r') as annot:
        if args.f == 'any':
            scf_set = set(line.split()[0] for line in annot)
        else:
            scf_set = set(line.split()[0] for line in annot if line.split()[2] == args.f)
        sys.stderr.write('loaded {} scaffolds with feature: {}\n'.format(len(scf_set), args.f))

    sys.stderr.write("filtering {} fasta file\n".format(args.g))
    if args.g[-2:] == "gz":
        ffile = SeqIO.parse(gzip.open(args.g, "rt"), "fasta")
    else :
        ffile = SeqIO.parse(args.g, "fasta")

    for seq_record in ffile:
        try:
            scf_set.remove(seq_record.name)
            sys.stdout.write(seq_record.format("fasta"))
        except KeyError:
            continue
    if len(scf_set) != 0:
        sys.stderr.write('{} annotated sequences were not found in the input fasta.'.format(len(scf_set)))

    sys.stderr.write('Done.')
