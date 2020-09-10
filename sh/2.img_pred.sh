#!/bin/bash
vname=$1
#-s ${h}*${w} 
vimg=$vname"_keyimgs"
source path.sh
for file in ` ls $vimg`
do
     if [ -d $vimg"/"$file ]
         python eval_single_img.py $vimg"/"$file
     fi
done
