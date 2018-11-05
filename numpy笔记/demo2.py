#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 22:43:30
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np


"""ndarry数组的创建和变换"""

# 1.从python中的元组、列表等类型创建ndarry数组-----x=np.array(list/tuple)或x=np.array(list/tuple，dtype=np.float32)
# 当np.array()不指定dtype时，numpy将根据数据情况关联一个dtype类型
a = np.array([0, 1, 2, 3])  # 从列表类型创建
print(a)
print('---------------snip-----------')
x = np.array((5, 6, 7, 8))  # 从元组类型创建
print(x)
print('---------------snip-----------')
y = np.array([[1, 2], [9, 8], (0.1, 0.2)])  # 从元组和列表混合类型创建
print(y)
print('---------------snip-----------')

# 2.使用numpy中的函数创建ndarry数组，例如：arange、ones、zeros等
"""
np.arange(n)    返回ndarry类型，元素从0到n-1
np.ones(shape)  生成全1数组，shape是元组类型
np.zeros(shape) 生成全0数组，shape是元组类型
np.full(shape,val) 根据shape生成一个数组，每个元素都是val
np.eye(n)      创建一个单位阵
np.ones_like(a) 根据数组a的形状生成一个全1数组
np.zeros_like(a) 根据数组a的形状生成一个全0数组
np.full_like(a, val) 根据数组a的形状生成一个数组，每个元素的值都是val
np.linspace()  根据起止数据等间距填充数剧，形成数组
np.concatenate()  将两个或多个数据合并成一个新的数组
"""
a = np.arange(10)
print(a)
print('---------------snip-----------')
b = np.ones((2, 5, 4))
print(b)
print('---------------snip-----------')
c = np.zeros((4, 3))
print(c)
print('---------------snip-----------')
d = np.eye(5)
print(d)
print('---------------snip-----------')
a = np.linspace(1, 10, 4)
print(a)
print('---------------snip-----------')
b = np.linspace(1, 10, 4, endpoint=False)
print(b)
print('---------------snip-----------')
c = np.concatenate((a, b))
print(c)
print('---------------snip-----------')
# 3.ndarry数组的维度变换
'''
.reshape()       不改变数组元素，返回一个shape形状的数组，原数组不变
.resize()        与.reshape()功能一致，但修改原数组
.swapaxes(ax1, ax2)  将数组n个维度中的两个维度进行调换
.flatten()     对数组进行降维，返回折叠后的一维数组，原数组不变
'''
a = np.ones((2, 3, 4), dtype=np.int32)
print(a.reshape(3, 8))
print('---------------snip-----------')
print(a)
print('---------------snip-----------')
b = a.flatten()
print(b)
print('---------------snip-----------')
a.resize(3, 8)
print(a)
print('---------------snip-----------')
# ndarry数组的类型变换
a = np.ones((2, 3, 4), dtype=np.int32)
print(a)
print('---------------snip-----------')
new_a = a.astype(np.float32)
print(new_a)
# astype()方法一定会创建一个新的数组（原始数据的一个拷贝），即使两个类型一致
print('---------------snip-----------')
# ndarry数组向列表的转换
a = np.full((2, 3, 4), 25, dtype=np.int32)
print(a)
print('---------------snip-----------')
ls = a.tolist()
print(ls)
