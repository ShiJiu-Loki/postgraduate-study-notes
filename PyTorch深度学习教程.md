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

安装conda之后，Jupyter会携带着一起安装在base环境中，但是在pytorch中并没有Jupyter，需要手动安装

```shell
conda install nb_conda
```

安装失败可以使用以下命令（二选一）

```shell
conda install jupyter notebook
conda install nb_conda_kernels
```

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

jupyter启动命令`jupyter notebook`

## 5、PyTorch加载数据初认识

Dataset：提供一种方式去获取数据及其label

- 如何获取每一个数据及其label
- 告诉我们总共有多少个数据

Dataloader：为后面的网络提供不同的数据形式

## 6、Dataset类代码实战

数据集格式通常来说有两种

一种是：

- dataset
  - train
    - ants：蚂蚁图片
    - bees：蜜蜂图片
  - val

另一种是

- dataset
  - train
    - ants_image：蚂蚁图片，img图片格式
    - ants_label：蚂蚁数据标签，txt文本格式
    - bees_image：蜜蜂图片，img图片格式
    - bees_label：蜜蜂数据标签，txt文本格式
  - val

以下案例按照第一种方式进行数据读取

```python
from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants"
bees_label_dir = "bees"
ants_dataset = MyData(root_dir,ants_label_dir)
bees_dataset = MyData(root_dir,bees_label_dir)
# 可以将两个数据集进行拼接
train_dataset = ants_dataset + bees_dataset
```

控制台命令（需要将编辑器的代码复制到控制台运行）

```shell
img, label = ants_dataset[0]
img.show()

img, label = bees_dataset[0]
img.show()

img, label = train_dataset[123]
img.show()
img, label = train_dataset[124]
img.show()
```

## 7、TensorBoard的使用（一）

常用两个方法：add_image()和add_scalar()

add_scalar()方法的使用（常用来绘制train/val loss）：

- tag：数据标识名称（图像标题）

- scalar_value：y轴
- global_step：x轴

安装TensorBoard

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorboard
```

TensorBoard启动使用，logdir=事件文件所在文件夹名，--port=端口号（可自定义，避免多人在同一台机器上训练出现冲突），在终端中输入以下命令

```shell
tensorboard --logdir=logs
tensorboard --logdir=logs --port=6007
```

如果tag设置的相同，那么新数据和旧数据就会显示在同一个图像上

解决方案：重新写一个子文件夹，也就是说创建新的SummaryWriter("新文件夹")

参考代码：

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

# writer.add_image()
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)

writer.close()
```

## 8、TensorBoard的使用（二）

add_image()的使用（常用来观察训练结果）



利用Opencv读取图片，获得numpy型图片数据

下载Opencv

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
```

利用numpy.array()，对PIL图片进行转换

add_image要求shape是CHW，转换成numpy类型的shape是HWC，需要进行匹配

HWC（高度，宽度，通道），图片是3通道

从PIL到numpy，需要在add_image()中指定shape中每一个数字/维表示的含义

参考代码：

```python
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "data/train/bees_image/16838648_415acd9e3f.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("test", img_array, 2, dataformats="HWC")
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 2*i, i)

writer.close()
```

在终端输入以下命令：

```shell
tensorboard --logdir=logs --port=6007
```

## 9、Transoforms的使用（一）

torchvision中的transforms，transforms对图片做一些变换

transforms结构及用法（本质上是一个transforms.py文件，相当于一个工具箱，里面有不同的class，有不同的作用）：将一个图片经过totensor、resize等工具的变换得到一个想要的结果

- 创建具体的工具：transoforms.ToTensor()

使用参考代码

```python
from PIL import Image
from torchvision import transforms

# python的用法 -> tensor数据类型
# 通过 transforms.ToTensor去解决两个问题
# 1、transforms该如何使用（python）
# 2、为什么需要Tensor数据类型

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)

# 1、transforms如何使用
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
print(tensor_img)
```

## 10、Transoforms的使用（二）

高版本python不支持opencv，所以安装不上去，使用以下命令安装低版本的

```shell
pip install opencv-python==4.3.0.38
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python==4.3.0.38
```

参考代码

```python
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# python的用法 -> tensor数据类型
# 通过 transforms.ToTensor去解决两个问题
# 1、transforms该如何使用（python）
# 2、为什么需要Tensor数据类型

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

# 1、transforms该如何使用（python）
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
# print(tensor_img)
writer.add_image("Tensor_img", tensor_img)
writer.close()
```

在Python控制台可以使用cv2，查看cv2的图片的格式（ndarray），注意路径不要携带中文

```python
import cv2
cv_img = cv2.imread(img_path)
```

在Terminal终端中使用

```shell
tensorboard --logdir=logs
```

## 11、常见的Transforms（一）

输入	PIL		  Image.open()

输出	tensor	    ToTensor()

作用	ndarrays	cv.imread()

Python中\_\_call\_\_的用法

```python
class Person:
    def __call__(self, name):
        print("__call__" + " Hello " + name)

    def hello(self, name):
        print("hello" + name)


person = Person()
person("zhangsan")
person.hello("lisi")
```

**ToTensor的使用**

```python
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img = Image.open("images/vegetable_dog.jpg")
print(img)

# ToTensor的使用
trans_totensor =transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)
writer.close()
```

**Normalize的使用**

```python
# Normalize的使用
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image("Normalize", img_norm)
```

```shell
归一化计算公式
output[channel] = (input[channel] - mean[channel]) / std[channel]
(input - 0.5) / 0.5 = 2 * input - 1
input[0,1]
output[-1,1]
```

以下内容为弹幕参考

> 归一化目的让数据在一个范围内比如0到1之间，从而避免奇异样本数据的影响，比如有极大数据
> 不同维度之间的特征在数值上量纲可能不一样，归一化就是让他们量纲大致差不多，这样梯度下降更快，更容易求解
> 归一化是为了消除奇异值，及样本数据中与其他数据相比特别大或特别小的数据 这样可以加快训练速度
> 归一化就是用来预处理图片的
> 标准化和归一化都是对数据进行线性变换

## 12、常见的Transforms（二）

**Resize()的使用**

```python
# Resize
print(img.size)
trans_resize = transforms.Resize((200, 200))
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> totensor -> img_resize tensor
img_resize = trans_totensor(img_resize)
writer.add_image("Resize", img_resize, 0)
print(img_resize)
```

**Compose()用法**

Compose()中的参数需要是一个列表，Python中，列表的表示形式为[数据1, 数据2, ...]

在Compose中，数据需要是transforms类型，所以得到Compose([transforms参数1, transforms参数2, ...])

```python
# Compose
trans_resize_2 = transforms.Resize(300)
# PIL -> PIL -> tensor
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
img_resize_2 = trans_compose(img)
writer.add_image("Resize", img_resize_2, 1)
```

**RandomCrop()用法**

```python
# RandomCrop
trans_random = transforms.RandomCrop(300)   # 可以指定高和宽
trans_compose_2 = transforms.Compose([trans_random, trans_totensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomCrop", img_crop, i)
```

**总结使用方法**

关注输入和输出类型

多看官方文档、源码

关注方法需要什么参数，参数是否有默认值

不知道返回值数据类型的时候，可以使用print()、print(type())，加断点调试

## 13、torchvision中的数据集使用

要想使用数据集，可以在pytorch官网查看：https://pytorch.org/

PyTorch -> PyTorch Domains -> torchvision -> 左侧dataset

torchvision数据集下载和使用

```python
import torchvision

train_set = torchvision.datasets.CIFAR10(root="./dataset_torchvision", train=True, download=True)
test_set = torchvision.datasets.CIFAR10(root="./dataset_torchvision", train=False, download=True)

print(test_set[0])
print(test_set.classes)

img, target = test_set[0]
print(img)
print(target)
print(test_set.classes[target])
img.show()
```

torchvision数据集和transform结合使用

```python
# torchvision数据集和transforms结合使用
dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
train_set = torchvision.datasets.CIFAR10(root="./dataset_torchvision", train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root="./dataset_torchvision", train=False, transform=dataset_transform, download=True)

writer = SummaryWriter("p10")
for i in range(10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)

writer.close()
```

## 14、DataLoader的使用

参考代码

```python
import torchvision

# 准备的测试数据集
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10("./dataset_torchvision", train=False, transform=torchvision.transforms.ToTensor())

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)

# 测试数据集中第一张图片及target
img, target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("dataloader")
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        # print(imgs.shape)
        # print(targets)
        writer.add_images("Epoch: {}".format(epoch), imgs, step)
        step += 1

writer.close()
```

Terminal终端

```shell
tensorboard --logdir=dataloader
```

target不是标签，是标签存放的位置，标签列表是classes，真正的标签是classes[target]

运行for循环就会重新调用test_loader,如果shuffle是True的话，那么bactch_size中的图片都不一样

其实很形象,suffle就是洗牌

## 15、神经网络的基本骨架——nn.Module的使用

torch.nn是Python API的神经网络工具包，nn是神经网络neural network的缩写

nn.Module的基本使用

```python
import torch
from torch import nn


class Tudui(nn.Module):
    def __init__(self) -> None:
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output


tudui = Tudui()
x = torch.tensor(1.0)
output = tudui(x)
print(output)
```

输入内容在神经网络中需要经过forward函数的处理，然后生成一个输出

## 16、卷积操作

在Pytorch官网上有对神经网络相关内容的封装：https://pytorch.org/docs/stable/nn.html#convolution-layers

torch.nn是对torch.nn.functional的封装，更加易于使用

conv是convolution（卷积）的简写

卷积的计算是卷积核（3×3）在输入图像（5×5）中从左上角依次向右向下移动，将每个位置的两个数值做乘法运算再累加，得到该位置的结果，结果也是一个图像

```python
import torch
import torch.nn.functional as F
input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])
kernel = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])

input = torch.reshape(input, (1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))

print(input.shape)
print(kernel.shape)

output = F.conv2d(input, kernel, stride=1)
print(output)

output2 = F.conv2d(input, kernel, stride=2)
print(output2)

output3 = F.conv2d(input, kernel, stride=1, padding=1)
print(output3)
```

stride=1（步径、步长），进行计算时向右移动1格，到最右侧时，需要回到最左侧向下移动1格

padding=1，在输入图像左右各插入一列，上下各插入一行，插入的数值为0，然后进行卷积运算

## 17、神经网络-卷积层

参考代码

```python
import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../dataset_torchvision", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x

tudui = Tudui()

writer = SummaryWriter("../logs")

step = 0
for data in dataloader:
    imgs, targets = data
    output = tudui(imgs)
    print(imgs.shape)
    print(output.shape)
    # torch.Size([64, 3, 32, 32])
    writer.add_images("input", imgs, step)
    # torch.Size([64, 6, 30, 30]) -> [xxx, 3, 30, 30]

    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images("output", output, step)
    step += 1
```

目录中./、../、/的区别

> ./是当前目录（其中./等价于不写，即href=“./layui/css/layui.css”和href=“layui/css/layui.css”是一样的效果）
> ../是父级目录（表示当前文件夹下的，上一个文件夹）
> /是根目录（表示一下子回到最顶端的那个文件夹下）

## 18、神经网络-最大池化的使用

Floor向下取整，Ceiling向上取整

池化核大小Kernel_Size=3（3×3），那么移动步长则为池化核大小，即3

池化核在输入图像上覆盖数量不足时，是否计算要看Ceil_model值，Ceil_model=True则计算，=False则不计算

最大池化作用：保留输入数据的特征，并且想让数据量减少

```python
import torch
from torch import nn
from torch.nn import MaxPool2d

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]], dtype=torch.float32)

input = torch.reshape(input, (-1, 1, 5, 5))
print(input.shape)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output

tudui = Tudui()
output = tudui(input)
print(output)
```

## 19、神经网络-非线性激活

非线性变换：给神经网络引入非线性特征，非线性特征够多，才能训练出符合各种曲线、符合各种特征的一个模型

```python
import torch
from torch import nn
from torch.nn import ReLU

input = torch.tensor([[1, -0.5],
                      [-1, 3]])

output = torch.reshape(input, (-1, 1, 2, 2))
print(output.shape)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.relu1 = ReLU()

    def forward(self, input):
        output = self.relu1(input)
        return output

tudui = Tudui()
output = tudui(input)
print(output)
```

## 20、神经网络-线性层及其他层介绍

torch.nn中：

- Convolution Layers 卷积层
- Pooling Layers 池化层
- Non-linear Activations 非线性激活
- Normalization Layers 正则层
- Linear Layers 线性层

正则层能加快神经网络的训练速度

```python
import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./dataset_torchvision", train=False,
                                       transform=torchvision.transforms.ToTensor(),
                                       download=True)

dataloader = DataLoader(dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.linear1 = Linear(196608, 10)

    def forward(self, input):
        output = self.linear1(input)
        return output

tudui = Tudui()

for data in dataloader:
    imgs, targets = data
    print(imgs.shape)
    # output = torch.reshape(imgs, (1, 1, 1, -1))
    output = torch.flatten(imgs)
    print(output.shape)
    output = tudui(output)
    print(output.shape)
```

## 21、神经网络-搭建小实战和Sequential的使用

```python
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.conv1 = Conv2d(3, 32, 5, padding=2)
        self.maxpool1 = MaxPool2d(2)
        self.conv2 = Conv2d(32, 32, 5, padding=2)
        self.maxpool2 = MaxPool2d(2)
        self.conv3 = Conv2d(32, 64, 5, padding=2)
        self.maxpool3 = MaxPool2d(2)
        self.flatten = Flatten()
        self.linear1 = Linear(1024, 64)
        self.linear2 = Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.conv3(x)
        x = self.maxpool3(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.linear2(x)
        return x

tudui = Tudui()
print(tudui)
```



## 国内pip镜像源

国内 pip 镜像源包括但不限于以下几种：

```shell
阿里云Python镜像源：https://mirrors.aliyun.com/pypi/simple/
豆瓣Python镜像源：https://pypi.douban.com/simple/
清华大学Python镜像源：https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学Python镜像源：http://pypi.mirrors.ustc.edu.cn/simple/
华中科技大学Python镜像源：http://pypi.hustunique.com/
```

使用方式

```shell
pip install -i https://mirrors.aliyun.com/pypi/simple some-package
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

这些镜像源都提供了和 **PyPI** 类似的软件包索引和下载服务，开发者可以通过配置 **pip** 使用这些镜像源来加速软件包的下载速度，提高稳定性。



