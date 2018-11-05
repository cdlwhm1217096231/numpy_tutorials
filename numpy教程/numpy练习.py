#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-01 13:36:11
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
# 1.查看 NumPy 版本信息
print(np.__version__)
# 2.创建数组
# NumPy 的主要对象是多维数组 Ndarray。在 NumPy 中维度（dimensions）叫做轴（axes），轴的个数叫做秩（rank）
# 3. 通过列表创建一维数组
print(np.array([1, 2, 3]))
# 4. 通过列表创建二维数组
print(np.array([(1, 2, 3), (4, 5, 6)]))
# 5. 创建全为 0 的二维数组
print(np.zeros((3, 3)))
# 6. 创建全为 1 的三维数组
print(np.ones((2, 3, 4)))
# 7. 创建一维等差数组
print(np.arange(5))
# 8.创建二维等差数组
print(np.arange(6).reshape(2, 3))
# 9.创建单位矩阵（二维数组）
print(np.eye(3))
# 10. 创建等间隔一维数组
print(np.linspace(1, 10, num=6))
# 11.创建二维随机数组
print(np.random.rand(2, 3))
# 12. 创建二维随机整数数组（数值小于 5）
print(np.random.randint(5, size=(2, 3)))
# 数组运算
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1, 6)
# 13.一维数组加法运算
print(a + b)
# 14.一维数组减法运算
print(a - b)
# 15. 一维数组乘法运算
print(a * b)
# 16. 一维数组除法运算
print(a / b)
# 生成二维示例数组（可以看作矩阵）
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# 17.矩阵加法运算
print(A + B)
# 18.矩阵减法运算
print(A - B)
# 19.矩阵元素间乘法运算
print(A * B)
# 20. 矩阵乘法运算（注意与上题的区别）
print(np.dot(A, B))
# 如果使用 np.mat 将二维数组准确定义为矩阵，就可以直接使用 * 完成矩阵乘法计算
print(np.mat(A) * np.mat(B))
# 21.数乘矩阵
print(2 * A)
# 22.矩阵的转置
print(A.T)
# 23.矩阵求逆
print(np.linalg.inv(A))
# 数学函数
# 24.三角函数
print(np.sin(a))
# 25. 以自然对数函数为底数的指数函数
print(np.exp(a))
# 26.数组的方根的运算（开平方）
print(np.sqrt(a))
# 27.数组的方根的运算（立方）
print(np.power(a, 3))
# 数组切片和索引
# 28.一维数组索引
a = np.array([1, 2, 3, 4, 5])
print(a[0], a[-1])
# 29.一维数组切片
print(a[0:2], a[:-1])
# 30.二维数组索引
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[0], a[-1])
# 31.二维数组切片（取第 2 列）
print(a[:, 1])
# 32. 二维数组切片（取第 2，3 行）
print(a[1:3, :])
# 数组形状操作
a = np.random.random((3, 2))
print(a)
# 33.查看数组形状
print(a.shape)
# 34.更改数组形状（不改变原始数组）
# reshape 并不改变原始数组
print(a.reshape(2, 3))
print(a)
# 35.更改数组形状（改变原始数组）
# resize 会改变原始数组
a.resize(2, 3)
print(a)
# 36.展平数组
print(a.ravel())
# 37.垂直拼合数组
a = np.random.randint(10, size=(3, 3))
b = np.random.randint(10, size=(3, 3))
print(a, b)
print(np.vstack((a, b)))
# 38.水平拼合数组
print(np.hstack((a, b)))
# 39.沿横轴分割数组
print(np.hsplit(a, 3))
# 40.沿横轴分割数组
print(np.vsplit(a, 3))
# 数组排序
a = np.array([[1, 4, 3], [6, 2, 9], [4, 7, 2]])
print(a)
# 41.返回每列最大值
print(np.max(a, axis=0))
# 42.返回每行最小值
print(np.min(a, axis=1))
# 43.返回每列最大值索引
print(np.argmax(a, axis=0))
# 44.返回每行最小值索引
print(np.argmin(a, axis=1))
# 数组统计
# 45.统计数组各列的中位数
print(np.median(a, axis=0))
# 46.统计数组各行的算术平均值
print(np.mean(a, axis=1))
# 47.统计数组各列的加权平均值
print(np.average(a, axis=0))
# 48.统计数组各行的方差
print(np.var(a, axis=1))
# 49.统计数组各列的标准偏差
print(np.std(a, axis=0))
# 50.创建一个 5x5 的二维数组，其中边界值为1，其余值为0
z = np.ones((5, 5))
print(z)
z[1:-1, 1:-1] = 0
print(z)

