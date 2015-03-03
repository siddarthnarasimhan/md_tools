#!/bin/bash

##################################################################
##           Secondary shift  assignments using STRIDE          ##
##                    Author: Sid Narasimhan                    ##
##################################################################

##Usage:
# 1) Make sure you only have the trajectory of the protein
# 2) Copy this script and cleanup.py to the folder with the .xtc and .tpr files
# 3) Rename your .xtc and .tpr to the same names
# 3) Run this script by calling: sh ss_stride.sh <name_of_xtc_tpr> <no_of_frames>

##Specific Requirements:
# 1) Bash
# 2) Python 2.6 or higher
# 3) GROMACS
# 4) STRIDE Compiled in your desktop

trjconv -f $1.xtc -s $1.tpr -o try_sid.pdb -sep
f=$2
i=0
while [ $i -le $f ]; do
  stride try_sid$i.pdb > ss_frame$i.txt
  let i=i+1
  done
rm -r try_sid*
i=0
while [ $i -le $f ]; do
  sed '/^REM/ d' ss_frame$i.txt > tmp.txt
  mv tmp.txt ss_frame$i.txt
  let i=i+1
  done
i=0
while [ $i -le $f ]; do 
  sed '/^CHN/ d' ss_frame$i.txt > tmp.txt
  mv tmp.txt ss_frame$i.txt
  let i=i+1
  done
i=0
while [ $i -le $f ]; do
  sed '/^SEQ/ d' ss_frame$i.txt > tmp.txt
  mv tmp.txt ss_frame$i.txt
  let i=i+1
  done
i=0
while [ $i -le $f ]; do
  sed '/^STR/ d' ss_frame$i.txt > tmp.txt
  mv tmp.txt ss_frame$i.txt
  let i=i+1
  done
i=0
while [ $i -le $f ]; do
  sed '/^LOC/ d' ss_frame$i.txt > tmp.txt
  mv tmp.txt ss_frame$i.txt
  let i=i+1
  done
python cleanup.py $2
