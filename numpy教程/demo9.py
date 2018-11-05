#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

# 随机数生成
# 可以normal来得到一个标准正态分布的4*4样本数组
samples = np.random.normal(size=(4, 4))
print(samples)
print('------------snip----------')
# numpy.random函数
# seed  确定随机数生成器的种子
# shuffle 对一个序列就地随机排列
# rand  产生均匀分布的样本值
# randint 从给定的上下限范围内随机选取整数
# randn  产生正态分布的样本值
# normal  产生正态分布的样本值
# uniform 产生在[0，1）中均匀分布的样本值
