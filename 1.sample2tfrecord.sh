#!/bin/bash
vname=$1
source path.sh
source undo_train.sh $vname
python image_classify_inception.py $vname
