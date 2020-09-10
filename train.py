# -*- coding:utf-8 -*-
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
from conf import config

'''
训练
'''
if __name__ == '__main__':
    config.TRAIN_MODEL.train()
