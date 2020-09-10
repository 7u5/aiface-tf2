#!/usr/bin/env bash
PROJECT_DIR=`pwd`
PROJECT_DIR='/data/qiuwu/tf-slim-inception'
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/models-master
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/train_config
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/models-master/research
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/models-master/research/slim
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/models-master/research/slim/datasets
