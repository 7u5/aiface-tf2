# -*- coding: utf-8 -*-

import os
import sys
import train_inception
_GConf_include={
    'slim_path':'research/slim',
    'slim_dataset_path':'research/slim/dataset',
}

_GConf_train={
    'default_model':'inception_resnetv2',
    'train_steps':300000,
    'batch_size':32,
    'gpu_set':'0',
}

_GConf={
    'default_model':'inception_resnetv2',
    'model_dir':'models',
    'data_dir':'../data',

    'tensorboard_host':'127.0.0.1',
    'tensorboard_train_port':'6006',
    'tensorboard_eval_port':'6007',
}

#include 2 dir  slim_dir, slim_dir/dataset
root_dir = os.path.dirname(os.getcwd()) + '/'
for (k,v) in _GConf_include.items():
    if '_path' in k:
        sys.path.append(root_dir+v)
    
TRAIN_MODEL = train_inception.TrainCommon()
