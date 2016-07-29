# generic_genomics

small scripts, functions or bits of code for parsing genomics data. I am not entirely sure about origin of all the scripts and some of them are very likely to contains bits of StackOverflow or code of my labmates, namely Andrea.

## Content

all excutible scripts are freely in the folder with description in this README. R functions are saved one per file in folder R_scripts.

### executible scripts

- bam_depth2scaffold_coverages.py
- count-errors.py
- seq_length_extraction.py
- seq_name_length_extraction.py
- cds_extraction_gtk.py
- seq_index_extraction.py
- seq_name_extraction.py

### R functions

- getNX(x, NX, genome_size) where x is vector of contig / scaffold lengths, NX is a X to be computed (or vector of NXs). If genome size is not provided it is computed as sum of all lengths
