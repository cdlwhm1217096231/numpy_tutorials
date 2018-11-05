#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

# 数组与标量之间的运算

# 大小相等的数组之间的任何算术运算都会应用到元素级
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print('-------------snip------------')
print(arr * arr)
print('-------------snip------------')
print(arr - arr)
print('-------------snip------------')
# 数组与标量之间的算术运算也会将那个标量值传播到各个元素
print(1 / arr)
print('-------------snip------------')
print(arr ** 0.5)
print('-------------snip------------')
# 不同大小的数组之间的运算叫做广播,稍后介绍
