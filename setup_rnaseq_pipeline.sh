 echo "Installing Ashley lab RNAseq pipeline"
 echo "Installing Cufflinks"
 echo "Downloading"
 wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
 echo "Uncompressing"
 tar zxf cufflinks-2.2.1.Linux_x86_64.tar.gz
 echo "Installing STAR aligner"
 echo "Downloading"
 wget https://rna-star.googlecode.com/files/STAR_2.3.0e.Linux_x86_64.tgz
 echo "Uncompressing"
 tar zxf STAR_2.3.0e.Linux_x86_64.tgz
 echo "Creating links"
 mv cufflinks-2.2.1.Linux_x86_64 /home/
 mv STAR_2.3.0e.Linux_x86_64 /home/
 ln -s /home/STAR_2.3.0e.Linux_x86_64/ /home/STAR
 ln -s /home/cufflinks-2.2.1.Linux_x86_64/ /home/cufflinks
 echo "Getting pipeline script from github"
 wget https://raw.githubusercontent.com/dimenwarper/ashley_scripts/master/rnaseq_align_and_quantify.sh -O /home/rnaseq_align_and_quantify.sh
