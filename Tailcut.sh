#!/bin/bash
#PBS -d .
#PBS -l walltime=24:00:00

#args("$@")

#directory_raw=${args[0]}
#directory_tailcut=${args[1]}

cd $directory_raw

gunzip "Unmapped.fastq.gz"


cd



python Work/Komar/Scripts/Tailcut2.0.py $directory_raw "5" "0.15" "Unmapped.fastq" "Cut_5_0.15.fastq"



