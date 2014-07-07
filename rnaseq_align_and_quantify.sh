#!/bin/bash
echo "Running pipeline for $1"
cd $1/
echo "In directory"
pwd
/home/STAR/STAR --genomeDir $2/Sequence/StarFiles/ --readFilesIn R1.fq R2.fq --runThreadN 8
echo "Sorting alignment"
sed 's/chrM/chrZ/g' Aligned.out.sam | sort -k 3,3 -k 4,4n > Aligned.out.sorted.sam
/home/cufflinks/cuffquant --library-type fr-firststrand -p 4 $2/Annotation/Genes/genes.gtf Aligned.out.sorted.sam
