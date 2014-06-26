from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class RNASeq(ClusterSetup):
     def __init__(self):
         pass

     def run(self, nodes, master, user, user_shell, volumes):
         log.info('Installing Ashley lab RNAseq pipeline')
         log.info('Installing Cufflinks')
         log.info('Downloading')
         master.ssh.execute('wget http://cufflinks.cbcb.umd.edu/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz')
         log.info('Uncompressing')
         master.ssh.execute('tar zxf cufflinks-2.2.1.Linux_x86_64.tar.gz')
         log.info('Installing STAR aligner')
         log.info('Downloading')
         master.ssh.execute('wget https://rna-star.googlecode.com/files/STAR_2.3.0e.Linux_x86_64.tgz')
         log.info('Uncompressing')
         master.ssh.execute('tar zxf STAR_2.3.0e.Linux_x86_64.tgz')
         log.info('Creating links')
         master.ssh.execute('mv cufflinks-2.2.1.Linux_x86_64 /home/')
         master.ssh.execute('mv STAR_2.3.0e.Linux_x86_64 /home/')
         master.ssh.execute('ln -s /home/STAR_2.3.0e.Linux_x86_64/ /home/STAR')
         master.ssh.execute('ln -s /home/cufflinks-2.2.1.Linux_x86_64/ /home/cufflinks')
         log.info('Getting pipeline script from github')
         master.ssh.execute('wget https://raw.githubusercontent.com/dimenwarper/ashley_scripts/master/rnaseq_align_and_quantify.sh -O /home/rnaseq_align_and_quantify.sh')
