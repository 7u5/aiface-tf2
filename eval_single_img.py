# -*- coding:utf-8 -*-
from train_config import config

import sys
import os

if __name__ == '__main__':
    pre = os.getcwd()
    if os.path.exists(pre):
        image_path = sys.argv[1]
    else:
        image_path = pre + '/' + sys.argv[1]
    config.TRAIN_MODEL.vis_single_img(image_path)
