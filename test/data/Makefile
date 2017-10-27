# five_scaffolds.fa

REF_DATA := five_scaffolds.fa.gz.bwt
TINY_DATA := ten_reads_R1.fq ten_reads_map.bam ten_reads_map.bam.bai
MODERATE_DATA := 20x_reads_R1.fq.gz 20x_reads_map.bam 20x_reads_map.bam.bai

.PHONY : all
all : $(REF_DATA) $(TINY_DATA) $(MODERATE_DATA)

.PHONY : tiny
tiny : $(TINY_DATA)

.PHONY : clean
clean :
	rm ten_reads_* 20x_reads_*

five_scaffolds.fa.gz.bwt : five_scaffolds.fa.gz
	bwa index $<

ten_reads_map.bam : five_scaffolds.fa.gz.bwt ten_reads_R1.fq
	bwa mem five_scaffolds.fa.gz ten_reads_R1.fq ten_reads_R2.fq | samtools sort -T sort_temp -O bam - > $@

20x_reads_map.bam : five_scaffolds.fa.gz.bwt 20x_reads_R1.fq.gz
	bwa mem five_scaffolds.fa.gz 20x_reads_R1.fq.gz 20x_reads_R2.fq.gz | samtools sort -T sort_temp -O bam - > $@

#ten_reads_map.bam
%.bam.bai : %.bam
	samtools index $<

PARAM := -1 125 -2 125 -d 350 -s 30 -r 0.001 -R 0.05 -X 0.3 -h

ten_reads_R1.fq : five_scaffolds.fa.gz
	echo ">one_scaffold" > scf_temp
	gunzip -c $< | grep -v ">" >> scf_temp
	wgsim -N 10 $(PARAM) -s 170725 scf_temp ten_reads_R{1,2}.fq > ten_reads_variants.bed
	rm scf_temp

20x_reads_R1.fq.gz : five_scaffolds.fa.gz
	wgsim -N 300000 $(PARAM) -s 170726 $< 20x_reads_R{1,2}.fq > 20x_variants.bed
	gzip 20x_reads_R1.fq 20x_reads_R2.fq
