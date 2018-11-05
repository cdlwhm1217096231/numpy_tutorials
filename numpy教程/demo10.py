#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

"""numpy高级应用"""

# 1.数组重塑
arr = np.arange(8)
print(arr)
print('----------snip----------')
print(arr.reshape((4, 2)))
print('----------snip----------')
# 多维数组也可以被重塑
print(arr.reshape((4, 2)).reshape((2, 4)))
print('----------snip----------')
# 作为参数的形状的其中一维可以是-1，表示该维度的大小由数据本身推断出来
arr = np.arange(15)
print(arr.reshape((5, -1)))
print('----------snip----------')
# 由于shape属性也是一个元组,因此也可以被传入到reshape中
other_arr = np.ones((3, 5))
dim = other_arr.shape
print(dim)
print(arr.reshape(dim))
print('----------snip----------')
# reshape将一维数组转换为多维数组，而flattening和raveling则是扁平化处理和散开处理
arr = np.arange(15).reshape((5, 3))
print(arr)
print('----------snip----------')
print(arr.ravel())  # ravel（）返回的是视图
print('----------snip----------')
print(arr.flatten())  # flatten（）返回的是副本
print('----------snip----------')
# C和F顺序排序即按行或列优先排序
"""
C/行优先顺序：先经过更高的维度
F/列优先排序: 后经过更高的维度
"""
print(arr.ravel('F'))
print('----------snip----------')
# 数组的合并和拆分
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([arr1, arr2], axis=0))
print('----------snip----------')
print(np.concatenate([arr1, arr2], axis=1))
# 对于常见的连接操作，可以使用vstack和hstack
print(np.vstack((arr1, arr2)))
print('----------snip----------')
print(np.hstack((arr1, arr2)))
print('----------snip----------')
# split可以将一个数组沿指定轴拆分为多个数组
arr = np.random.randn(5, 2)
print(arr)
print('----------snip----------')
first, second, third = np.split(arr, [1, 3])
print(first)
print('----------snip----------')
print(second)
print('----------snip----------')
print(third)
print('----------snip----------')
# 元素的重复操作tile和repeat
"""repeat会将数组中的各个元素重复一定次数，从而产生一个更大的数组"""
arr = np.arange(3)
print(arr.repeat(3))
print('----------snip----------')
# 如果传入一组整数，则各个元素可以重复不同的次数
print(arr.repeat([2, 3, 4]))
print('----------snip----------')
# 对于多维数组，可以指定沿哪个轴重复
arr = np.random.randn(2, 2)
print(arr)
print('----------snip----------')
print(arr.repeat(2, axis=1))
print('----------snip----------')
# tile的功能是沿指定轴堆叠数组的副本
print(np.tile(arr, 2))   # 对于标量是水平铺设的
print('----------snip----------')
print(np.tile(arr, (3, 2)))
print('----------snip----------')
# 广播：不同形状数组之间的算术运算方式
'''最简单的广播：标量和数组的合并'''
arr = np.arange(5)
print(arr)
print('----------snip----------')
# 标量4被广播到数组的其他的元素上
print(arr * 4)
print('----------snip----------')
arr = np.random.randn(4, 3)
print(arr)
print('----------snip----------')
mean_value = arr.mean(0)
print(mean_value)
print('----------snip----------')
demeaned = arr - mean_value
print(demeaned)
print('----------snip----------')
print(demeaned.mean(0))
print('----------snip----------')
arr = np.random.randn(4, 3)
print('原数组:\n', arr)
print('----------snip----------')
row_means = arr.mean(1)
print('轴1上的平均值:{}'.format(row_means))
demeaned = arr - row_means.reshape((4, 1))
print(demeaned.mean(1))
##################通过np.newaxis属性以及全切片来插入一个长度为1的新轴######################
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
print(arr_3d.shape)
arr_1d = np.random.normal(size=3)
print(arr_1d)
print('----------snip----------')
print(arr_1d[:, np.newaxis])
print('----------snip----------')
print(arr_1d[np.newaxis, :])
# 假设有一个三维数组，并对轴2进行距平化
arr = np.random.randn(3, 4, 5)
print(arr)
print('----------snip----------')
depth_means = arr.mean(2)
print(depth_means)
print('----------snip----------')
demeaned = arr - depth_means[:, :, np.newaxis]
print(demeaned.mean(2))
print('----------snip----------')
# 通过广播设置数组的值
col = np.array([1.28, -0.42, 0.44, 1.6])
temp = col[:, np.newaxis]
print(temp)
print('----------snip----------')
arr[:] = temp
print(arr)
