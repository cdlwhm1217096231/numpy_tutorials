#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-20 08:56:25
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np

'''ndarray数组的操作------数组的索引和切片'''
# 1.索引：获取数组中特定位置元素的过程
# 一维数组的索引：与python的列表类似
a = np.array([9, 8, 7, 6, 5])
print(a[2])
# 多维数组的索引
b = np.arange(24).reshape((2, 3, 4))
print(b)
print(b[1, 2, 3])  # 每一个维度的索引值之间用逗号分割
print(b[0, 1, 2])
print(b[-1, -2, -3])
# 2.切片：获取数组元素子集的过程
# 一维数组的切片：与Python的列表类似
print(a[1:4:2])   # 起始编号：终止编号（不含）：步长，3元素冒号分割
# 多维数组的切片
c = np.arange(24).reshape((2, 3, 4))
print(c[:, 1, -3])  # 通过冒号:可以选择整个维度
print('-----------------snip----------------')
print(c[:, 1:3, :])
print('-----------------snip----------------')
print(c[:, :, ::2])  # ::2表示选择整个维度，以2为步长进行切片
print('-----------------snip----------------')
