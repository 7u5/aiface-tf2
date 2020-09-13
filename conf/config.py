# -*- coding: utf-8 -*-

import os
import sys
import conf.train_inception as train_inception
_conf_include={
    'slim_path':'research/slim',
    'slim_dataset_path':'research/slim/dataset',
}

_conf_train={
    'default_model':'inception_resnet_v2',
    'train_steps':2000,
    'batch_size':16,
    'gpu_set':'0',
    'optimizer':'adam',
    'weight_decay': 0.0004,
    'learning_rate': 0.01, #lr decay type
    'learning_rate_decay_type':'polynomial', #lr decay type
    'gpu_mem_limit':'0.9',
}

_conf={
    'default_model':'inception_resnetv2',
    'model_dir':'models',
    'data_dir':'../data',
    'label_filename':'labels.txt',

    'tensorboard_host':'127.0.0.1',
    'tensorboard_train_port':'6006',
    'tensorboard_eval_port':'6007',
	'train':_conf_train,
	'include':_conf_include,
}

root_dir = os.getcwd() + '/'
for (k,v) in _conf_include.items():
    #if '_path' in k:
    sys.path.append(root_dir+v)
TRAIN_MODEL = train_inception.TrainCommon()
