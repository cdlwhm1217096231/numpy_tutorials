#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-17 10:23:20
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
import numpy as np


"""复制和视图"""
# 1.完全不复制
# 简单赋值不会创建数组对象或其数据的拷贝
a = np.arange(6)
print(a)
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
b.shape = (3, 2)
print(a.shape)
# 2.视图或浅复制
# 不同的数组对象可以共享相同的数据。view方法创建一个新数组对象，该对象看到相同的数据。与前一种情况不同，新数组的维数更改不会更改原始数据的维数，但是新数组数据更改后，也会影响原始数据。
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
c = a.view()
print('c is a:', c is a)
print('c.base is a:', c.base is a)
print('c.flags.owndata: ', c.flags.owndata)
c.shape = (2, 6)
print(a.shape)
c[0, 4] = 1234
print(a)
print('------------------------snip--------------------')
# 3.深复制
# copy方法生成数组及其数据的完整拷贝
d = a.copy()   # 一个完整的新的数组
print('新数组d:\n', d)
print('d is a: ', d is a)
print('d.base is a: ', d.base is a)
print('------------------------snip--------------------')
d[0, 0] = 999
print('修改某个值后的新数组d:\n', d)
print('------------------------snip--------------------')
print('原始数组a:\n', a)  # 修改数组d的值，a不会受影响
