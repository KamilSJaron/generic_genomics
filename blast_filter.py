#!/usr/bin/env python3

# this script is supposed to do what people think blast argument max_target_seqs does
# parameters:
# -evalue           -> filter by evalue
# -num_alignments   -> filter by number of alignments per query?

# -> set up the filters
# -> input stream of blast hits
# -> while reading
#   -> just read until the first column is the same
#   -> print by the filter

import argparse
import sys
from operator import itemgetter

if __name__ == "__main__":
    args = None
    if len(sys.argv) == 1:
        args = ["--help"]

    parser = argparse.ArgumentParser(description="Filter out blast outfmt 6 output by specific criteria")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='The blast output file to parse [stdin]')
    # parser.add_argument("-evalue", default = 1e-10, help="The evalue threshold for alignment to be kept")
    parser.add_argument("n", help="The maximal number of reported alignments per query (sorted by evalue)", type=int)
    args = parser.parse_args(args)

    query_strings = [args.infile.readline()];
    query_name = query_strings[0].split('\t')[0];

    for aln in args.infile:
        aln = aln;
        if aln.split('\t')[0] == query_name:
            query_strings.append(aln);
        else:
            print(min(args.n, len(query_strings)))
            for line_to_print in query_strings[0:min(args.n, len(query_strings))]:
                sys.stdout.write(line_to_print)
            query_strings = [aln]
            query_name = aln.split('\t')[0]