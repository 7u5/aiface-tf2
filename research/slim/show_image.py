# -*- coding:utf-8 -*-
# Author:      zhousf
# Date:        2018-12-29
# File:        show_image.py
# Description:  
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
setname = bald
from datasets import bald
import pylab

import tf_slim as slim
pre = ""
DATA_DIR = pre + "/" + setname

# Selects the 'validation' dataset.
dataset = bald.get_split('validation', DATA_DIR)

# Creates a TF-Slim DataProvider which reads the dataset in the background
# during both training and testing.
provider = slim.dataset_data_provider.DatasetDataProvider(dataset)
[image, label] = provider.get(['image', 'label'])

# 在session下读取数据，并用pylab显示图片
with tf.Session() as sess:
    # 初始化变量
    sess.run(tf.global_variables_initializer())
    # 启动队列
    tf.train.start_queue_runners()
    image_batch, label_batch = sess.run([image, label])
    # 显示图片
    pylab.imshow(image_batch)
    pylab.show()
