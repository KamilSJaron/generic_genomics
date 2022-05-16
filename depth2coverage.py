#!/usr/bin/env python3

import sys
from statistics import median
from pysam import AlignmentFile
from sys import stdout
from math import floor
from math import ceil
import argparse

def mean(lst):
    return sum(lst) / len(lst)

def dynamic_window_size(scf_len, target_window_size):
    fewer_windows = floor(scf_len / target_window_size)
    more_windows = ceil(scf_len / target_window_size)
    if fewer_windows > 0 and abs((scf2len[scf] / fewer_windows) - target_window_size) < - abs(scf_len / more_windows - target_window_size):
        window = ceil(scf_len / fewer_windows)
    else:
        window = ceil(scf_len / more_windows)
    return window

parser = argparse.ArgumentParser(description="from per base depth (samtools depth -aa file1.bam file2.bam ...) calculate per window coverages")
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='depth file (default: stdandard input)')
parser.add_argument('-b', help="Corresponding Bam file to get the header.", default = '')
parser.add_argument("-w", "-window", help="Length of a window (default = 0; 0 will calculate per-scaffold coverage)", type = int, default = 0)
parser.add_argument("--dynamic-window-size", help="Adjust the number of windows and window size for each scaffold so the mean window size is closest to parameter -w", action='store_const', dest='dynamic', const=True, default=False)
parser.add_argument("--median", help="Report medians instead of means", action='store_const', const=True, default=False)
args = parser.parse_args()

if args.b != '':
    bam_file = AlignmentFile(args.b, mode='rb')
    reference_names = list(bam_file.references)
    reference_lengths = list(bam_file.lengths)
    scf2len = dict()
    for i, scf in enumerate(reference_names):
        scf2len[scf] = reference_lengths[i]

if args.b == '' and args.dynamic:
    raise ValueError('You must specify a valid bam file (argument -b <file.bam>) for --dynamic-window-size flag to work.')

if args.w == 0 and args.dynamic:
    raise ValueError('Window size can not be the scaffold size (0; default) for --dynamic-window-size flag to work.')

depths = []
last_scf = ''
start = 1
end = 0
window = args.w

for depthline in args.infile:
    depth_tab = depthline.split('\t')
    scf = depth_tab[0]
    scf_len = scf2len[scf]

    if args.w == 0:
        window = scf_len

    if last_scf == '':
        last_scf = scf
        if args.dynamic:
            window = dynamic_window_size(scf_len, args.w)
            end = window

    if(scf != last_scf):
        if args.median:
            cov = median(depths)
        else:
            cov = mean(depths)
        stdout.write('{}\t{}\t{}\t{}\n'.format(last_scf, start, end, cov))

        if args.dynamic:
            window = dynamic_window_size(scf_len, args.w)
        depths = [int(depth_tab[2])]
        start = 1
        end = min(window, scf_len)

    else:
        if len(depths) == window:
            print(len(depths))
            if args.median:
                cov = median(depths)
            else:
                cov = mean(depths)
            stdout.write('{}\t{}\t{}\t{}\n'.format(last_scf, start, end, cov))
            start = end + 1
            end = min(end + window, scf_len)
            depths = [int(depth_tab[2])]
        else:
            depths.append(int(depth_tab[2]))

    last_scf = depth_tab[0]

if args.median:
    cov = median(depths)
else:
    cov = mean(depths)

stdout.write('{}\t{}\t{}\t{}\n'.format(last_scf, start, scf_len, cov))
