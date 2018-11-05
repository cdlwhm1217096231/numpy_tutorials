#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np

# 通用函数：快速的元素级数组函数
# 通用函数（ufunc）是一种对ndarray中的数据执行元素级运算的函数，可以将其看做简单函数的矢量化包装器
arr = np.arange(10)
print(np.sqrt(arr))
print('---------------snip-------------')
print(np.exp(arr))
# 另外一些函数接收2个数组，并返回一个结果数组
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print('---------------snip-------------')
print(y)
print('---------------snip-------------')
print(np.maximum(x, y))   # 元素级最大值
# ufunc的确可以返回多个数组，modf就是一个例子，用于浮点数数组的小数和整数部分
arr = np.random.randn(7) * 5
print(np.modf(arr))
print('---------------snip-------------')
# 一元ufunc
# abs fabs sqrt square exp log log10 log2 sign ceil:计算大于等于该值的最小整数  floor：计算小于等于该值的最大整数
# modf：将数组的小数和整数部分以两个独立数组的形式返回  sin cos arccos arccosh arctan arctanh tan cosh sinh isnan
# 二元ufunc
# add subtract multipy divide mod power maximum fmax minimum fmin


