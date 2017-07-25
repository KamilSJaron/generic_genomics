# five_scaffolds.fa

REF_DATA := five_scaffolds.fa.bwt
TINY_DATA := ten_reads_R1.fq ten_reads_map.bam
MODERATE_DATA := 20x_reads_map.bam 20x_reads_R1.fq.gz

.PHONY : all
all : $(REF_DATA) $(TINY_DATA) $(MODERATE_DATA)

.PHONY : tiny
tiny : $(TINY_DATA)

.PHONY : clean
clean :
	rm ten_reads_R* 20x_reads_R1*

five_scaffolds.fa.bwt : five_scaffolds.fa.gz
	bwa index $<

ten_reads_map.bam : five_scaffolds.fa.bwt ten_reads_R1.fq
	bwa mem five_scaffolds.fa ten_reads_R1.fq ten_reads_R2.fq | samtools sort -T sort_temp -O bam - > $@

20x_reads_map.bam : five_scaffolds.fa.bwt 20x_reads_R1.fq.gz
	bwa mem five_scaffolds.fa 20x_reads_R1.fq.gz 20x_reads_R2.fq.gz | samtools sort -T sort_temp -O bam - > $@

#ten_reads_map.bam

PARAM := -1 125 -2 125 -d 350 -s 30 -r 0.001 -R 0.05 -X 0.3 -h

ten_reads_R1.fq : five_scaffolds.fa.gz
	wgsim -N 10 $(PARAM) -s 170725 $< ten_reads_R{1,2}.fq > ten_reads_variants.bed

20x_reads_R1.fq.gz : five_scaffolds.fa.gz
	wgsim -N 300000 $(PARAM) -s 170726 $< 20x_reads_R{1,2}.fq > 20x_variants.bed
	gzip 20x_reads_R1.fq 20x_reads_R2.fq
