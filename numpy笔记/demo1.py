#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 22:04:49
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np  # (引入模块的别名)
# 数据的维度  ------一组数据的组织形式
# 一维数据：由对等关系的有序或无序数据构成，采用线性方程形式
# 列表：数据类型可以不同，有序的结构；
# 二维数据：由多个一维数据构成，是一维数据的组合形式
# 多维数据：由一维或二维数据在新维度上扩展形成
# 高维数据: 仅利用最基本的二元关系展示数据间的复杂结构
# numpy中的数组对象:ndarray


def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([5, 6, 7, 8, 9])
    c = a**2 + b**2
    return c


print(npSum())
'''
# 数组对象可以去掉元素间运算所需的循环，使一维向量更像单个数据
# 设置专门的数组对象，经过优化，可以提升这类应用的运算速度
# 数组对象采用相同的数据类型，有助于节省运算和存储空间
# ndarray是一个多维数组对象，由两部分构成：实际的数据，描述这些数据的元数据(数据维度，数据类型等)
# ndarray数组一般要求所有元素类型相同（同质），数组下标从0开始
'''
# np.array()生成一个ndarray数组，ndarray在程序中的别名是array
a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
# np.array()输出成[]形式，元素由空格分割
# 轴（axis）:保存数据的维度，秩（rank）:轴的数量
print(a)
print('-------------------snip ----------------')
# ndarray对象的属性
'''
.ndim  秩，即轴的数量或者维度的数量
.shape ndarry对象的尺度，对于矩阵n行m列
.size  ndarry对象元素的个数，相当于.shape中n*m的值
.dtype ndarry对象的元素类型
.itemsize  ndarry对象中每个元素的大小，以字节为单位
'''
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.size)
print(a.itemsize)
print('-------------------snip ----------------')
# ndarry的元素类型
'''
bool intc intp int8 int16 int32 int64 uint8 uint16 uint32 uint64 float16 float32 float64 complex64 complex128
'''
# 对比：python仅支持整数、浮点数、复数3种类型
# ndarray数组可以由非同质对象构成，非同质ndarry元素为对象类型，非同质ndarry对象无法有效发挥numpy优势，尽量不用
x = np.array([[0, 1, 2, 3, 4], [9, 8, 7, 6]])
print(x.shape)
print(x.dtype)
print(x.ndim)
print(x.size)
print(x.itemsize)
