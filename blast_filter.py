#!/usr/bin/env python3

# this script is supposed to do what people think blast argument max_target_seqs does
# parameters

import argparse
import sys

if __name__ == "__main__":
    args = None
    if len(sys.argv) == 1:
        args = ["--help"]

    parser = argparse.ArgumentParser(description="Filter out blast outfmt 6 output by specific criteria")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='The blast output file to parse [stdin]')
    parser.add_argument("n", help="The maximal number of reported alignments per query (sorted by evalue)", type=int)
    parser.add_argument("-m", "-max_target_seqs", help="The parameter max_target_seqs you gave to blast (to warn you about potentially suboptimal alignments)", type=int, default=500)
    args = parser.parse_args(args)

    query_strings = [args.infile.readline()];
    query_name = query_strings[0].split('\t')[0];

    for aln in args.infile:
        if aln.split('\t')[0] == query_name:
            query_strings.append(aln);
        else:
            if len(query_strings) >= args.m:
                sys.stderr.write("# WARNING: query " + query_name + " have reached max_target_seqs. There is no guarantee of the best alignment found.\n")
            sys.stdout.write("".join(query_strings[0:min(args.n, len(query_strings))]))
            query_strings = [aln]
            query_name = aln.split('\t')[0]