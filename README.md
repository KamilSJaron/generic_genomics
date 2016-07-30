# generic_genomics

small scripts, functions or bits of code for parsing genomics data. I am not entirely sure about origin of all the scripts and some of them are very likely to contains bits of StackOverflow or code of my labmates, namely Andrea.

## Content

all excutible scripts are freely in the folder with description in this README. R functions are saved one per file in folder R_scripts.

### executible scripts

- `bam_depth2scaffold_coverages.py <file.depth>` - converts depth computed by samtools depth
- `fasta2extracted_seq_N.py <file.fasta> <seqname>` - exrect a sequence of <seqname> name from fasta file
- `fasta2lengths.py <file.fasta>` - computes lengths of seqeunces in fasta file`
- `gtk2cds.py <file.gtk> <file.fasta>` - extract coding seqeunces written in gtk file from fasta file (kallisto)
- `fasta2extracted_seq_SE.py <file.fasta> <start> <end>` - extract a subsequence starting by nucleotide position  <start> ending by <end> from simple fasta file
- `fasta2nameslengths.py` - computes lengths of seqeunces in fasta file returned togheder with sequence headers` 

- `count-errors.py` - under construction

### R functions

- getNX(x, NX, genome_size) where x is vector of contig / scaffold lengths, NX is a X to be computed (or vector of NXs). If genome size is not provided it is computed as sum of all lengths
