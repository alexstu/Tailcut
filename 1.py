import sys
from subprocess import call


dirr = ['Work/Komar/Data/pn/Raw/D0_1',
'Work/Komar/Data/pn/Raw/D0_2',
'Work/Komar/Data/pn/Raw/D24_1',
'Work/Komar/Data/pn/Raw/D24_2',
'Work/Komar/Data/pn/Raw/PnLarvae',
'Work/Komar/Data/pv/Raw/d0.1',
'Work/Komar/Data/pv/Raw/d0.2',
'Work/Komar/Data/pv/Raw/d24.1',
'Work/Komar/Data/pv/Raw/d24.2',
'Work/Komar/Data/pv/Raw/d48.1',
'Work/Komar/Data/pv/Raw/d48.2',
'Work/Komar/Data/pv/Raw/egg',
'Work/Komar/Data/pv/Raw/female',
'Work/Komar/Data/pv/Raw/larva',
'Work/Komar/Data/pv/Raw/male',
'Work/Komar/Data/pv/Raw/pupae',
'Work/Komar/Data/pv/Raw/r24.1',
'Work/Komar/Data/pv/Raw/r24.2',
'Work/Komar/Data/pv/Raw/r3.1',
'Work/Komar/Data/pv/Raw/r3.2']

for d in dirr:
	command = ['qsub', 'Work/Komar/Scripts/Tailcut.sh', '-v', 'directory_raw='+d]
	call(command)




bowtie2 -U Work/Komar/Data/pn/Raw/D0_1/Cut_5_0.15.fastq -S Work/Komar/Data/pn/Raw/D0_1Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PnScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pn/Raw/D0_2/Cut_5_0.15.fastq -S Work/Komar/Data/pn/Raw/D0_2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PnScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pn/Raw/D24_1/Cut_5_0.15.fastq -S Work/Komar/Data/pn/Raw/D24_1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PnScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pn/Raw/D24_2/Cut_5_0.15.fastq -S Work/Komar/Data/pn/Raw/D24_2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PnScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pn/Raw/PnLarvae/Cut_5_0.15.fastq -S Work/Komar/Data/pn/Raw/PnLarvae/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PnScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d0.1/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d0.1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d0.2/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d0.2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d24.1/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d24.1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d24.2/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d24.2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d48.1/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d48.1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/d48.2/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/d48.2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/egg/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/egg/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 2 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/female/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/female/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/larva/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/larva/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/male/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/male/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/pupae/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/pupae/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/r3.2/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/r3.2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/r3.1/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/r3.1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/r24.2/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/r24.2/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 
bowtie2 -U Work/Komar/Data/pv/Raw/r24.1/Cut_5_0.15.fastq -S Work/Komar/Data/pv/Raw/r24.1/Cut_5_0.15.sam -x /home/mazin/pvan/ref.v9/index/PvScaf_v0.9 -N 1 -D 20 -R 3 



qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pn/Raw/D0_1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pn/Raw/D0_2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pn/Raw/D24_1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pn/Raw/D24_2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pn/Raw/PnLarvae

qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d0.1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d0.2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d24.1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d24.2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d48.1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/d48.2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/egg
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/female
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/larva
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/male
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/pupae
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/r24.1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/r24.2
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/r3.1
qsub Work/Komar/Scripts/Coverager2.0.sh -v directory_raw=Work/Komar/Data/pv/Raw/r3.2



scp Work/Komar/Data/pn/Raw/D0_1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PN_D0_1.bg
scp Work/Komar/Data/pn/Raw/D0_2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PN_D0_2.bg
scp Work/Komar/Data/pn/Raw/D24_1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PN_D24_1.bg
scp Work/Komar/Data/pn/Raw/D24_2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PN_D24_2.bg
scp Work/Komar/Data/pn/Raw/PnLarvae/Cut_5_0.15.bg Work/Komar/Data/AT_all/PN_PnLarvae.bg

scp Work/Komar/Data/pv/Raw/d0.1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D0_1.bg
scp Work/Komar/Data/pv/Raw/d0.2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D0_2.bg
scp Work/Komar/Data/pv/Raw/d24.1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D24_1.bg
scp Work/Komar/Data/pv/Raw/d24.2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D24_2.bg
scp Work/Komar/Data/pv/Raw/d48.1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D48_1.bg
scp Work/Komar/Data/pv/Raw/d48.2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_D48_2.bg
scp Work/Komar/Data/pv/Raw/egg/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_EGG_1.bg
scp Work/Komar/Data/pv/Raw/female/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_FEMALE.bg
scp Work/Komar/Data/pv/Raw/larva/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_LARVA.bg
scp Work/Komar/Data/pv/Raw/male/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_MALE.bg
scp Work/Komar/Data/pv/Raw/pupae/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_PUPAE.bg
scp Work/Komar/Data/pv/Raw/r24.1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_R24_1.bg
scp Work/Komar/Data/pv/Raw/r24.2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_R24_2.bg
scp Work/Komar/Data/pv/Raw/r3.1/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_R3_1.bg
scp Work/Komar/Data/pv/Raw/r3.2/Cut_5_0.15.bg Work/Komar/Data/AT_all/PV_R3_2.bg







