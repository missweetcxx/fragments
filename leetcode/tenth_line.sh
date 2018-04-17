#!/usr/bin/env bash
#
# Create on 4/16/2018
#
# Author: Sylvia
#
# 195. Tenth Line
# Your script should output the tenth line of file.txt.

point="0"

cat file.txt | while read line
do
  let point=point+1
  if [ "$point" -eq "10" ]; then
     echo $line
  fi
done
