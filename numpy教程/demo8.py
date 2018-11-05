#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np
from numpy.linalg import inv, qr


# 线性代数
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
print(x)
print('------------snip----------')
print(y)
# 矩阵相乘
print(x.dot(y)) #  np.dot(x, y)
print('------------snip----------')
# 一个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组
print(np.dot(x, np.ones(3)))
print('------------snip----------')
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(mat)
print('------------snip----------')
print(inv(mat))
print('------------snip----------')
print(mat.dot(inv(mat)))
print('------------snip----------')
q, r = qr(mat)
print(r)
print('------------snip----------')
# 常用的numpy.linalg函数
# diag: 以一维数组的形式返回方阵的对角线元素，或将一维数组转换为方阵
# dot： 矩阵乘法
# trace: 计算对角线元素的和
# det: 计算矩阵行列式
# inv：计算方阵的逆
# pinv: 伪逆
