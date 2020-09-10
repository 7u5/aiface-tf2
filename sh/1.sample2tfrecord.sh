#!/bin/bash
vname=$1
source path.sh
source undo_train.sh $vname
python image2tfrecord.py $vname
