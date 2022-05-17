# generic_genomics

small scripts, functions, tiny testing dataset or bits of code for parsing genomics data. I am not entirely sure about origin of all the scripts and some of them are very likely to contains bits of StackOverflow or code of my labmates, namely Andrea.

## Content

all excutible scripts are freely in the folder with description in this README. R functions are saved one per file in folder `R_scripts`.

### executible scripts

- `bam2extract_by_list_of_headers.py` - prints a subset (sam) of headers from bam; usually used with `... | samtools -bh - >`
- `depth2depth_per_contig.py <file.depth>` - converts depth computed by samtools depth
- `depth2depth_per_contig.awk` - does completely same thing, I just forgot that I wrote python script already, need to do a speed test to chose which one to keep
- `depth2bed_coverage.py` - converts depth computed by samtools depth in coverages - per scaffold (default) or per window (fixed, or dynamically set). See `-h` for all the options. Example use: `samtools depth -aa test/data/ten_reads_map.bam | python depth2coverage.py -b test/data/ten_reads_map.bam --dynamic-window-size -w 100000 > test/data/coverages.bed`
- `fasta2extract_by_header.py <file.fasta> <seqname>` - exrect a sequence of <seqname> name from fasta file
- `fasta2lengths.py <file.fasta>` - computes lengths of seqeunces in fasta file
- `gtk2cds.py <file.gtk> <file.fasta>` - extract coding seqeunces written in gtk file from fasta file (kallisto)
- `fasta2extract_by_nt_range.py <file.fasta> <start> <end>` - extract a subsequence starting by nucleotide position  <start> ending by <end> from simple fasta file
- `fasta2nameslengths.py` - computes lengths of seqeunces in fasta file returned togheder with sequence headers`
- `fasta2fasta_length_filtering.py <file.fasta> <filter>` - on standard output will be printed a fasta containing only sequences longer than `<filter>`
- `fastq2fasta_length_filtering.py <file.fastq> <filter>` - on standard output will be printed a fasta containing only sequences longer than `<filter>`
- `fasta2genomic_stats.py <file.fasta> [<genome_size>]` - on standard output will be printed standard genomic stats (total sum, number of sequences, N50, L50). If `<genome_size>` is not specified, the half of the total sum is used for computation of N50 and L50
- `fasta2extract_by_list_of_headers.py <file.fa> <headers.list>` - on standard output will be printed a fasta containing only sequences in header list
- `fasta2fasta_annotated_portions.py -a <annotation.gff3> -g <genome.fa> -f <feature>` - subset a `<genome>` to scaffolds that contain an annotated `<feature>`.- `count-errors.py` - under construction

### R functions

- `getNX(x, NX, genome_size)` where x is vector of contig / scaffold lengths, NX is a X to be computed (or vector of NXs). If genome size is not provided it is computed as sum of all lengths
- `fixed_bin_histogram(list_of_things_to_display, pal, bins)` - a wrapper function for R hist to plot mutiple overlaping histograms with fixed breaks for all of them

```
fixed_bin_histogram <- function(list_of_things_to_display, pal = NA, bins = 50,
                                   xlim = NA, ylim = NA, probability = F,
                                   border = F, default_legend = T,
                                   main = '', xlab = 'Value', ylab = NA, ...)

#   list_of_things_to_display - list of vectors to be plotted
#   pal - pallete; their respective colours; got to have the same length
#   bins - similar like breaks it defines the number of bars in the histogram; but unlike breaks it the number of displayed bars (considering xlim), the number is approximate, used breaks for all the histograms are pretty(xlim, bins)
#   xlim, ylim - by defeault "all data and all hights", by changing xlim breaks get recalculated to keep "bins" relative the displayed number of bars
#   probability - create non/normalised histograms with Frequency/Density on the y axis (make big difference for datasets of different sizes)
#   default_legend - by detailt names of elements in the list, can be turned off by setting this value to F
#   main - sets title
#   xlab, ylab - sets label of the x axis (default: "Value"), for yaxis the defaut is Frequency/Density dependent on probability being = F/T
#   ... - all addenitional paramaters will be passed to the "plot" function rendering all the histograms
```

### Dataset

a 5 scaffold reference (`five_scaffolds.fa`) are saved in folder `test`. Using `make` you can generate a testing dataset consisting of

- 20x coverage pair-end reads generated from the reference for reasonable variant callings (`fq.gz`)
- 10 pair-reads for control of coordinates / nt sequences (`fq`)
- mapped reads (both read files) using bwa-mem (`.bam`)

this should serve for sanity checks, maybe latter on they will be integrated in for more formal tests of these scripts.

#### to add

GC content oneliner:

```
awk "BEGIN { print "$(grep -v ">" $ASM | tr -cd CG | wc -c)"/"$(grep -v ">" $ASM | tr -cd ATCG | wc -c)" }"
```
