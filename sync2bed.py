#!/usr/bin/env python3

import sys
from mimetypes import guess_type
import gzip
from  functools import partial

sync_file = sys.argv[1]

encoding = guess_type(sync_file)[1]
_open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open

with _open(sync_file) as ffile:
    last_scf = ''
    scf_count = 1
    for line in ffile:
        scf = line.split('\t')[0]
        if last_scf == '':
            last_scf = scf
            continue
        if last_scf != scf:
            sys.stdout.write('{}\t{}\n'.format(last_scf, scf_count))
            scf_count = 1
            last_scf = scf
        else:
            scf_count += 1
    sys.stdout.write('{}\t{}\n'.format(scf, scf_count))

