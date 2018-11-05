#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

"""ndarray：一种多维数组对象"""
# ndarray对象是一个通用的同构数据多维容器，其中的所有元素必须是相同类型
data = np.array([[0.9526, -0.246, -0.8856], [0.5639, 0.2379, 0.9104]])
print(data)
print('------------------snip---------------')
print(data * 10)
print('------------------snip---------------')
print(data + data)
print('------------------snip---------------')
# 每个数组都有一个shape（表示各维度大小的元组）和一个dtype（一个用于说明数组数据类型的对象）
print(data.shape)
print(data.dtype)
# 创建ndarray对象
# 创建数组最简单的方法是使用array函数: 它接受一切序列类型的对象，然后产生一个新的含有传入数据的numpy数组
data1 = [1, 2, 3, 4, 5]
arr1 = np.array(data1)
print(arr1)
print(arr1.dtype)
print('------------------snip---------------')
# 嵌套序列（由一组等长列表组成的列表）将会被转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print('------------------snip---------------')
print(arr2.shape)
print('arr2中的最小维度:', arr2.ndim)
# 除非显式说明，np.array会尝试为新建的这个数组推断出一个较为合适的数据类型，数据类型保存在一个特殊的dtype对象中
print(arr2.dtype)
# 除了array函数能创建数组外，zeros,ones,分别创建指定长度或形状的全0或全1的数组，empty创建一个没有任何具体数值的数组
# 使用这些函数时，只需要传入一个表示形状的元组即可
arr = np.zeros(10)
print(arr)
arr1 = np.zeros((3, 6))
print(arr1)
print('------------------snip---------------')
arr2 = np.empty((2, 3, 2))
print(arr2)
# arange是python内置函数range的数组版
arr = np.arange(15)
print(arr)
# 创建单位方阵
arr = np.eye(3)
print(arr)
print('------------------snip---------------')
# ndarray的数据类型
# dtype是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息
arr = np.array([1, 2, 3], dtype=np.float32)
arr1 = np.array([1, 2, 3], dtype=np.int32)
print(arr.dtype, arr1.dtype)
# 通过ndarray的astype方法显式地转成其他dtype
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float32)
print(float_arr.dtype)
# 如果将浮点数转换成整数，小数部分将会被截断
arr = np.array([-2.1, 5.4, 34.3, 24.8, 8.9])
print(arr)
arr1 = arr.astype(np.int32)
print(arr1)
# 如果某字符数组表示的全是数字，也可以使用astype将其转换为数组形式
number = np.array(['3.4', '6.4', '34.8', '9.4', '0.618'])
print(number.astype(np.float64))
# 数组的dtype还有另一个用法
int_array = np.arange(10)
calibers = np.array([0.22, 0.270, 0.357, 0.380, 0.44, 0.50], dtype=np.float64)
print(int_array.astype(calibers.dtype))
# 注：调用astype无论如何都会创建一个新的数组，即使新的dtype跟老的数组是同一类型的，都是对原始数组的拷贝
# 注：浮点数只能表示近似的分数值，在比较操作中只能在一定的小数位以内有效

