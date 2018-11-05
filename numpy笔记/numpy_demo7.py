#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-17 10:44:08
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
from numpy import newaxis
from pprint import pprint
"""形状操作"""
# 1.更改数组形状------数组具有由沿着每个轴的元素数量给出的形状
a = np.floor(10 * np.random.random((3, 4)))
print('原始多维数组:\n', a)
print(a.shape)
print('进行平铺:\n', a.ravel())
print('重塑多维数组a:\n', a.reshape(2, 6))  # 重塑成 2x6
# 技巧：在使用 reshape 时，可以将其中的一个维度指定为 -1，Numpy 会自动计算出它的真实值
print('在使用 reshape 时，可以将其中的一个维度指定为 -1，Numpy 会自动计算出它的真实值:\n', a.reshape(3, -1))
print('a的转置:\n', a.T)
print(a.shape)
# 注:无论是ravel、reshape、T，它们都不会更改原有的数组形状，都是返回一个新的数组
# 使用 resize 方法可以直接修改数组本身
a.resize(2, 6)
print('已经被修改后的原始数组:\n', a)
# 2.将不同数组堆叠在一起
# 除了可以对单个数组的形状进行转换外，还可以把多个数据进行堆叠
a = np.floor(10 * np.random.random((2, 2)))
print('原始多维数组a:\n', a)
b = np.floor(10 * np.random.random((2, 2)))
print('原始多维数组b:\n', b)
print('---------------------snip-----------------')
print(np.vstack((a, b)))
print('---------------------snip-----------------')
print(np.hstack((a, b)))
print('---------------------snip-----------------')
# 对于2D数组来说，使用hstack和column_stack 效果一样，对于1D数组来说，column_stack 会将1D数组作为列堆叠到2D数组中
print(np.column_stack((a, b)))
# 一维数组的情况下，column_stack和hstack结果不一样
a = np.array([4, 2], dtype=np.float32)
b = np.array([3, 8], dtype=np.float32)
print('一维数组使用column_stack:\n', np.column_stack((a, b)))
print('---------------------snip-----------------')
print('将一维数组转为二维数组:\n', a[:, newaxis])  # 将一维数组转为二维数组
print('---------------------snip-----------------')
print('一维数组使用column_stack:\n', np.column_stack((a[:, newaxis], b[:, newaxis])))
# 对于任何输入数组，函数row_stack等效于vstack
"""
一般来说，对于具有两个以上维度的数组，hstack沿第二轴堆叠，vstack沿第一轴堆叠，concatenate允许一个可选参数，给出串接应该发生的轴
"""
# 3.将一个数组分成几个较小的数组
# 使用hsplit，可以沿其水平轴拆分数组，通过指定要返回的均匀划分的数组数量，或通过指定要在其后进行划分的列
a = np.floor(10 * np.random.random((2, 12)))
print('原始多维数组a:\n', a)
print('---------------------snip-----------------')
print(np.hsplit(a, 3))   # 水平切成3等份
# vsplit沿垂直轴分割，array_split允许指定沿哪个轴分割
pprint('---------------------snip-----------------')
pprint(np.vsplit(a, 2))  # 垂直切成2等份
