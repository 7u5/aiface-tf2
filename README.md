## tf-slim-inception
Modify the original code to support tensorflow2.3,  change some of the codes structure that easier to modify.

### Tensorflow 1.14 codes upgrade to tensorflow 2.3 compitable way, and test ok.

please run export PYTHONPATH="" first if there has PYTHONPATH value in Linux env.
then source path.sh

### Directory structure change and code changes:
(1) remove models-master dir, research move forward

(2) remove conf, config.py and train_inception.py move to root dir. config.py now can control model-name, steps, almost training config related configuration.

(3) remove duplicate {root_dir}/research/slim/datasets/{classname}.py, merge into a common.py

no longer to need create many files for new class creation. there has a common.py within {root_dir}/research/slim/datasets directory.


tensorflow-slim下的inception_v3、inception_v4、inception_resnet_v2分类模型的数据制作、训练、评估、导出模型、测试。
训练比较请参考：[InceptionV3、InceptionV4图像分类训练与比较](https://blog.csdn.net/zsf442553199/article/details/85683335)


## 相关截图
### 项目结构

{classname}是某个分类任务的名字，与 data/{classname} 样本目录相关
pos_{classname} 为该分类正例, neg_{classname}为复例

### 数据制作
image2tfrecord.py
数据制作请参考flowers

### 训练
* train.py {classname}

### 评估
* eval.py {classname}

### 可视化
* show_train.py 训练
* show_eval.py 评估

### 导出模型
* export.py {classname}

### 测试
eval_single_img.py {classname}
eval_single_dir.py {classname}

### 模型配置文件
* train_inception.py 配置训练的参数(网络模型选择，训练次数，batch_size、指定GPU等)
* config.py 配置文件

