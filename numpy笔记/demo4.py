#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-20 09:16:08
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np


"""ndarray数组的运算"""
# 1.数组与标量之间的运算
# 数组与标量之间的运算作用于数组的每一个元素
a = np.arange(24).reshape((2, 3, 4))
print(a)
print('----------------snip--------------')
print(a.mean())  # 标量值
print(a / a.mean())
print('----------------snip--------------')
# 2.numpy一元函数---------对ndarray中的数据执行元素级运算的函数
"""
np.abs(x).  np.fabs(x)   计算数组各元素的绝对值
np.sqrt(x)               计算数组各元素的平方根
np.square(x)             计算数组各元素的平方
np.log(x)  np.log10(x) np.log2(x)  计算数组各元素的对数
np.ceil(x)  np.floor(x)            计算数组各元素的ceiling值或者floor值
np.exp(x)                          计算数组各元素的指数
"""
a = np.arange(24).reshape((2, 3, 4))
print(np.square(a))
print('----------------snip--------------')
print(np.sqrt(a))
print('----------------snip--------------')
# 原始数组a并没有被改变，真实改变时，使用赋值语句a = np.sqrt(a)
a = np.sqrt(a)
print(np.modf(a))
print('----------------snip--------------')
