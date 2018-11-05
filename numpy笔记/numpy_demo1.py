#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

# 1.numpy是什么
"""
Numpy 是 Python 的一个科学计算包，包含了多维数组以及多维数组的操作
Numpy 的核心是ndarray对象，这个对象封装了同类型数据类型的n维数组。起名ndarray的原因是因为是n-dimension-array的简写
"""
# 2.ndarray 与 python 原生 array 有什么区别
"""
NumPy 数组在创建时有固定的大小，不同于Python列表（可以动态增长）。更改ndarray的大小将创建一个新的数组并删除原始数据。
NumPy 数组中的元素都需要具有相同的数据类型，因此在存储器中将具有相同的大小。
数组的元素如果也是数组（可以是 Python 的原生 array，也可以是 ndarray）的情况下，则构成了多维数组。
NumPy 数组便于对大量数据进行高级数学和其他类型的操作。通常，这样的操作比使用Python的内置序列可能更有效和更少的代码执行。
"""
# 3.Numpy 的矢量化（向量化）功能
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
c = a * b  # a b为两个同类型的向量
print(c)
