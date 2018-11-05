#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np

# 数组的转置和轴对换
# 转置不仅有transpose方法，也有一个T属性，不进行任何复制操作，是源数据的视图
arr = np.arange(15).reshape((3, 5))
print(arr)
print('----------snip------------')
print(arr.T)
print('----------snip------------')
# 在进行矩阵计算时，经常用到此操作,如利用np.dot计算矩阵内积X.T@X
arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))
print('----------snip------------')
# 对于高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print('----------snip------------')
print(arr.transpose((1, 0, 2)))
print('----------snip------------')
# 简单的转置使用.T,ndarray提供一个swapaxes方法，它需要接受一对轴编号,其返回的也是源数据的视图，不进行任何复制操作
print(arr)
print('----------snip------------')
print(arr.swapaxes(1, 2))
print('----------snip------------')



