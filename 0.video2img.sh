#!/bin/bash
vname=$1
#-s ${h}*${w} 
vimg=$vname"_keyimgs"
echo $vimg
mkdir $vimg
ffmpeg -i $vname -vf select='eq(pict_type\,I)' -vsync 2 -f image2 $vimg/core-%02d.jpeg
