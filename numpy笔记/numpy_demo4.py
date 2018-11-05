#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np


""""基本运算操作"""
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
print(c)
print(b**2)
print(a < 35)
# 矩阵对应元素的乘积
a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
print('元素乘积:\n', a*b)
# 两个矩阵相乘
print('矩阵相乘:\n', a.dot(b))
# 矩阵相乘的另一种方式
print('矩阵相乘的另一种方式:\n', np.dot(a, b))
# 某些操作（如+=和*=）可以修改现有数组，而不是创建新数组
a = np.ones((2, 3), dtype=np.int32)
b = np.random.random((2, 3))
print(a)
a *= 3
print(a)
print(a.dtype)
print(b.dtype)
# 当使用不同类型的数组操作时，结果数组的类型对应于更一般或更精确的数组（称为向上转换的行为）
b += a
print(b)
# 由于定义a时，数据类型指定为np.int32，而 a+b 生成的数据类型为 np.float64，所以自动转换出错
# a += b
# print(a)
