#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-20 09:39:46
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np

# 数据类型对象 (dtype)


# 使用数组标量类型
dt = np.dtype(np.int32)
print(dt)
# int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他
dt = np.dtype('i4')
print(dt)
# 使用端记号
dt = np.dtype('>i4')
print(dt)
# 下面的例子展示了结构化数据类型的使用,这里声明了字段名称和相应的标量数据类型
dt = np.dtype([('age', np.int8)])
print(dt)
# 现在将其应用于 ndarray 对象
dt = np.dtype([('age', np.int8)])
a = np.array([[10, ], [20, ], [30, ]], dtype=dt)
print(a)
print(a['age'])
# 以下示例定义名为 student 的结构化数据类型，其中包含字符串字段name，整数字段age和浮点字段marks。 此dtype应用于ndarray对象
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
# 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
