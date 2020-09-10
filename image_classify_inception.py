# -*- coding:utf-8 -*-
# Author:      zhousf
# Date:        2018-12-25
# File:        image_classify_inception.py
# Description: 生成slim数据格式的tfRecord
# 每个文件夹放一个类别图片即可
import os
import sys

dataset_name = sys.argv[1] if len(sys.argv) > 1 else 'bald'
rdataset_dir = sys.argv[2] if len(sys.argv) > 2 else '/mnt/sda1/ml/image_data/'+dataset_name+'/train'
path_pre = os.getcwd()
dataset_dir = path_pre+'/../data/'+dataset_name
if not os.path.exists(dataset_dir):
    cmd = 'ln -sf %s %s'% (rdataset_dir, dataset_dir)
    os.system(cmd)
else:
    if os.path.normcase(rdataset_dir) != os.path.normcase(os.readlink(dataset_dir)):
        cmd = 'ln -sf %s %s'% (rdataset_dir, dataset_dir)
        os.system(cmd)
command = 'python %s/research/slim/convert_data.py ' \
          '--dataset_name=%s ' \
          '--dataset_dir=%s' % (path_pre, dataset_name, dataset_dir)
os.system(command)



