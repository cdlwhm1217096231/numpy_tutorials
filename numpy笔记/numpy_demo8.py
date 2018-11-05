#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-18 10:25:24
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np

# 1.数学运算函数

"""
add(x1，x2 [，out])	按元素添加参数，等效于 x1 + x2
subtract(x1，x2 [，out])	按元素方式减去参数，等效于x1 - x2
multiply(x1，x2 [，out])	逐元素乘法参数，等效于x1 * x2
divide(x1，x2 [，out])	逐元素除以参数，等效于x1 / x2
exp(x [，out])	计算输入数组中所有元素的指数。
exp2(x [，out])	对于输入数组中的所有p，计算2 ** p
log(x [，out])	自然对数，逐元素
log2(x [，out])	x的基础2对数
log10(x [，out])	以元素为单位返回输入数组的基数10的对数
expm1(x [，out])	对数组中的所有元素计算exp(x) - 1
log1p(x [，out])	返回一个加自然对数的输入数组，元素
sqrt(x [，out])	按元素方式返回数组的正平方根
square(x [，out])	返回输入的元素平方
sin(x [，out])	三角正弦
cos(x [，out])	元素余弦
tan(x [，out])	逐元素计算切线
"""
x = np.random.randint(4, size=6).reshape(2, 3)
print(x)
print('----------------------snip------------------')
y = np.random.randint(4, size=6).reshape(2, 3)
print(y)
print('----------------------snip------------------')
print(x + y)
print('----------------------snip------------------')
print(np.add(x, y))
print('----------------------snip------------------')
print(np.square(x))
print('----------------------snip------------------')
print(np.log1p(x))
print('----------------------snip------------------')
# 2.规约函数
# 下面所有的函数都支持axis来指定不同的轴，用法都是类似的
"""
ndarray.sum([axis，dtype，out，keepdims])	返回给定轴上的数组元素的总和
ndarray.cumsum([axis，dtype，out])	返回沿给定轴的元素的累积和
ndarray.mean([axis，dtype，out，keepdims])	返回沿给定轴的数组元素的平均值
ndarray.var([axis，dtype，out，ddof，keepdims])	沿给定轴返回数组元素的方差
ndarray.std([axis，dtype，out，ddof，keepdims])	返回给定轴上的数组元素的标准偏差
ndarray.argmax([axis，out])	沿着给定轴的最大值的返回索引
ndarray.min([axis，out，keepdims])	沿给定轴返回最小值
ndarray.argmin([axis，out])	沿着给定轴的最小值的返回索引
"""
x = np.random.randint(10, size=6).reshape(2, 3)
print(x)
print('----------------------snip------------------')
print('沿水平轴求和:\n', np.sum(x, axis=0))  # 水平轴
print('----------------------snip------------------')
print('沿垂直轴求和:\n', np.sum(x, axis=1))  # 垂直轴
print('----------------------snip------------------')
print(np.argmax(x))
print('----------------------snip------------------')
print('水平轴最大值索引:\n', np.argmax(x, axis=0))  # 水平轴
print('----------------------snip------------------')
print('水平轴最大值:\n', np.max(x, axis=0))
print('----------------------snip------------------')
print('垂直轴最大值索引:\n', np.argmax(x, axis=1))  # 垂直轴
print('----------------------snip------------------')
print('垂直轴最大值:\n', np.max(x, axis=1))
