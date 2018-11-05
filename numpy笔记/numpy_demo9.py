#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-18 10:48:36
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np

# 1.什么是广播
"""
Numpy中的基本运算（加、减、乘、除、求余等等）都是元素级别的，但是这仅仅局限于两个数组的形状相同的情况下
广播机制：Numpy 可以转换这些形状不同的数组，使它们都具有相同的大小，然后再对它们进行运算
"""
# 广播实例
a = np.arange(0, 40, 10)
print(a.shape)
b = np.array([0, 1, 2])
print(b.shape)
a = a[:, np.newaxis]  # 转换a的维度(形状)
print(a)
print('---------------snip-------------')
print(a + b)
print('---------------snip-------------')
# 上述广播的详细过程
a2 = np.array(([i * 3 for i in a.tolist()]))
print(a2)
print('---------------snip-------------')
b2 = np.array([b.tolist()] * 4)
print(b2)
print('---------------snip-------------')
print(a2 + b2)
