# PyTorch深度学习教程

参考课程：B站up主：我是土堆

## 1、PyTorch环境得配置及安装

下载安装anaconda或者miniconda

conda的环境管理，不同项目可能需要使用不同版本的工具包

```shell
conda create -n pytorch python=3.6
```

```shell
# To activate this environment, use
#
#     $ conda activate pytorch
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

查看工具包

```shell
pip list
```

pytorch安装：https://pytorch.org/

查看GPU是否支持cuda：https://www.nvidia.cn/geforce/technologies/cuda/supported-gpus/

```shell
python
>>> import torch
>>> torch.cuda.is_available()
```

## 2、Python编辑器选择、安装及配置

安装pycharm后编译器选择`Conda Environment`，高版本选择系统解释器，找到conda目录下的python.exe

Jupyter 可交互

## 3、Python学习中的两大法宝函数

（1）理解Package结构及法宝函数的作用

dir()函数，能让我们知道工具箱以及工具箱中的分隔区有什么东西

help()函数，能让我们知道每个工具是如何使用的，工具的使用方法

例如：`dir(torch.cuda)`，`help(torch.cuda.is_available)`，使用help函数时，查看的函数不加()括号

## 4、Pycharm和Jupyter使用及对比

代码是以块为一个整体运行的话，那么

- Pycharm：python文件的块是所有行的代码；遇到错误，下次执行需要从头开始；
  - 优点：通用，传播方便，适用于大型项目
  - 缺点：需要从头运行

- 控制台：以每一行为块，运行的；遇到错误，修改错误后，可以继续执行（阅读性差，但可以看到变量的属性）
  - 优点：显示每个变量属性
  - 缺点：不利于代码阅读及修改

- Jupyter：以任意行为块运行的
  - 优点：利于代码阅读及修改
  - 缺点：环境需要配置

## 5、PyTorch加载数据初认识

Dataset：提供一种方式去获取数据及其label

- 如何获取每一个数据及其label
- 告诉我们总共有多少个数据

Dataloader：为后面的网络提供不同的数据形式

## 6、Dataset类代码实战





























