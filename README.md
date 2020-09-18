original Forked from MrZhousf/tf-slim-inception ,i haven't fork inplace becoz i both have tf1 and tf2 version, are incompatible. 

## tf-slim-inception for inceptionv3/v4/inception_resnet_v2 image clasification's data generation to tfrecord, training, evalue, tensorboard showing, export and test.
Modify the original code to support tensorflow2.3,  change some of the codes structure that easier to modify.

### Tensorflow 1.14 codes upgrade to tensorflow 2.3 compitable way, and test ok.

you should install tf-slim in tensorflow 2 by "pip install tf-slim"

please run export PYTHONPATH="" first if there has PYTHONPATH value in Linux env.
then source path.sh

### Directory structure change and code changes:
(1) remove models-master dir, research move forward

(2) remove conf, config.py and train_inception.py move to root dir. config.py now can control model-name, steps, almost training config related configuration.

(3) remove duplicate {root_dir}/research/slim/datasets/{classname}.py, merge into a common.py

no longer to need create many files for new class creation. there has a common.py within {root_dir}/research/slim/datasets directory.


if you read Chinese, viewing Mrzhou's comparation amongs them ：[InceptionV3、InceptionV4 image classification comparison](https://blog.csdn.net/zsf442553199/article/details/85683335)


## snapshot(ommit)
### project structure

{classname} is class name of sub task classification， related to ../data/{classname} sample directory

if you serving a binary-classification: you can name pos_{classname} is positive sample, neg_{classname} is negative samples
if you serving multi-classfication: you can try a classname as a taskname, then directory under ../data/{classname}/{sub-classname1-N}

### data generation from image to tfrecord
image2tfrecord.py

// demo class is "flowers"

### training
* train.py {classname}

### eval
* eval.py {classname}

### visualized by tensorboard, need to open 6006/6007 port as tensorboad will serve a web services,
* show_train.py // default using 6006 port. can be cutomized and view by http://{ip}:6006 // if you have relay machine, you need to open 6006 port mapping in tunnel config.
* show_eval.py  // default using 6007 port. can be cutomized and view by http://{ip}:6006

### export
* export.py {classname}

### test eval after training and export the model
eval_single_img.py {classname}  // single image
eval_single_dir.py {classname}  // a directory with many images

### model config 
* config.py 

