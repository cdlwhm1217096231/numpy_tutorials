#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

#############N维数组ndarray##############
# 1. 构建ndarray
a = np.array([0, 1, 2, 3])
print(a)
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)
# 2.利用函数来创建ndarray
a = np.arange(10)
print(a)
b = np.arange(1, 6, 2)  # 步长设为2
print(b)
a = np.ones((3, 3))  # 全1矩阵
print(a)
b = np.zeros((2, 2))  # 全0矩阵
print(b)
c = np.eye(3)  # 单位阵
print(c)
d = np.diag(np.array([1, 2, 3, 4]))  # 对角阵
print(d)
a = np.random.rand(2, 3)  # 随机矩阵,满足[0, 1]上的均匀分布
print(a)
b = np.random.randn(2, 3)   # 随机矩阵,满足高斯分布
print(b)
# 3.ndarry常用属性
"""
ndarray.flags                       有关数组的内存布局的信息
ndarray.shape                       数组维数
ndarray.strides                     遍历数组时，在每个维度中步进的字节数组
ndarray.ndim	                    数组维数，在Python世界中，维度的数量被称为rank
ndarray.data	                    Python缓冲区对象指向数组的数据的开始
ndarray.size	                    数组中的元素总个数
ndarray.itemsize	                一个数组元素的长度（以字节为单位）
ndarray.nbytes	                    数组的元素消耗的总字节数
ndarray.base	                    如果内存是来自某个其他对象的基本对象
ndarray.dtype	                    数组元素的数据类型
ndarray.T	                        数组的转置
"""
a = np.array([[2, 3, 4], [4, 5, 6]])
print(a)
print(a.flags)
print(a.shape)
print(a.ndim)
print(a.strides)
print(a.data)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.dtype)
print(a.T)