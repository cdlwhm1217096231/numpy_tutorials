#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np
import matplotlib.pyplot as plt

# 利用数组进行数据处理
# np.meshgrid()函数接收两个一维数组，并产生两个二维矩阵
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print('---------------snip-------------')
print(ys)
print('---------------snip-------------')
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
print('---------------snip-------------')
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title('Image plot of...')
plt.show()
# 将条件逻辑表述为数组运算
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 当conda中的值为True时，选取xarr的值，否则从yarr中选取
result = [x if c else y for x, y, c in zip(xarr, yarr, cond)]
print(result)
print('---------------snip-------------')
# np.where的第二个第三个参数不是必须的数组，可以是标量值，where一般用于根据另一个数组产生一个新的数组
result = np.where(cond, xarr, yarr)
print(result)
print('---------------snip-------------')
# 如一个用随机数据组成的矩阵，希望正值替换成2，负值替换成-2，利用np.where会很简单
arr = np.random.randn(4, 4)
print(arr)
print('---------------snip-------------')
print(np.where(arr > 0, 2, -2))
print('---------------snip-------------')
print(np.where(arr > 0, 2, arr))
print('---------------snip-------------')
# 数学和统计方法
# 通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算，sum、mean、以及标准差std等聚合计算
arr = np.random.randn(5, 4)  # 正态分布的数据
print(arr.mean())
print('---------------snip-------------')
print(np.mean(arr))
print('---------------snip-------------')
print(arr.sum())
print('---------------snip-------------')
# mean和sum这类的函数可以接受一个axis参数，最终结果是一个少一维的数组
print(arr.mean(axis=1))
print('---------------snip-------------')
print(arr.sum(0))
print('---------------snip-------------')
# 例如cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(0))
print('---------------snip-------------')
print(arr.cumprod(1))
print('---------------snip-------------')
# 基本数组统计方法
# sum   对数组中全部或某轴向的元素求和
# mean  算术平均数
# std var 分别为标准差和方差
# argmin argmax 分别为最小和最大元素的索引
# cumsum   所有元素的累积和
# cumprod  所有元素的累积积

# 用于布尔型数组的方法
arr = np.random.randn(100)
print((arr > 0).sum())
# 两个方法any和all，对布尔型数组非常有用，any用于测试数组中是否存在一个或多个True，而all则检查数组中所有值是否都是True
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())
# 这两个方法能用于非布尔型数组，所有非0元素将会被当做True

# 排序-----使用sort方法进行排序
arr = np.random.randn(8)
print(arr)
arr.sort()
print(arr)
# 多维数组可以在任何一个轴向上进行排序，只需将轴编号传给sort即可
arr = np.random.randn(5, 3)
print(arr)
print('---------------snip-------------')
arr.sort(1)
print(arr)
print('---------------snip-------------')
# np.sort返回是数组的已排序副本，计算数组分位数最简单的办法是对其进行排序，然后选取特定位置的值
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05*len(large_arr))])  # 5%分位数
print('---------------snip-------------')

# 唯一化及其他的集合逻辑------最常用的可能要数np.unique，用于找出数组中的唯一值并返回已排序的结果
names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
print(np.unique(names))
print('---------------snip-------------')
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print('---------------snip-------------')
# 使用函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
print('---------------snip-------------')
