# -*- coding:utf-8 -*-
import os,sys
#os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
import conf.config as config

'''
训练
'''
if __name__ == '__main__':
    config.TRAIN_MODEL.train()
