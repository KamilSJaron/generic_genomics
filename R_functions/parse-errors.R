#read.csv('timema.errors.fa.bam.profile.txt', header = T, sep = '\t')
mapstat <- read.csv('/Volumes/dump/projects/PacBio/canu/amphioPBvIl.fa.bam.profile.txt', header = T, sep = '\t')
cl <- read.csv('/Volumes/dump/data/sequences/draft_genomes/Amphioxus/canu_e025/amphio_read_lengths.csv', header = F)$V1
attach(mapstat)

colnames(mapstat)


align_len + insertions + matches + mismatches - read_len

hist(log(read_len,10))
hist(log(cl,10))

xaxe <- 100*align_len/(matches+deletions+insertions+mismatches)
xaxe[which(xaxe == Inf)] <- 100*align_len[which(xaxe == Inf)]

plot(xaxe ~ (align_len+insertions-deletions)/(align_len+unalign_len-deletions+insertions))

ggplot(mapstat, aes(x=xaxe, 
           y=(align_len+insertions-deletions)/(align_len+unalign_len-deletions+insertions))
) +
  xlab("Percent identity: 100* matches/(matches+deletions+insertions+mismatches)") +
  ylab("Fraction of read aligned: \n(align_len+ins-del)/(align_len+unalign_len-del+ins)") +
  geom_point(alpha=0.5) + 
  xlim(20,100) +
  ylim(0.0,1.0) +
  theme_bw(base_size=24)
