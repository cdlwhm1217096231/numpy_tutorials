#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np

# 基本的索引和切片

# 数组切片是原始数组的视图，这说明数据不会被复制，视图上的任何修改都会直接反映到源数组上
arr = np.arange(10)
print(arr[5])
print(arr[5:8])  # 切片
arr[5:8] = 12
print(arr)
arr_slice = arr[5:8]
arr_slice[1] = 666
print(arr)
# 冒号表示整个维度
arr_slice[:] = 777
print(arr)
# 在一个二维数组上，各个索引位置上的元素不再是标量而是一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
# 传入一个以逗号隔开的索引列表选取单个元素,下面两种方法等效
print(arr2d[0, 2])
print(arr2d[0][2])
# 在多维数组中，如果省略后面的索引，则返回对象将会是一个维度低一点的ndarray,例如2*2*3数组
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print('----------snip------------')
print(arr3d[0])  # 2*3数组
print('----------snip------------')
# 标量值和数组都可以被赋值给arr3d[0]
old_value = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
print('----------snip------------')
arr3d[0] = old_value
print(arr3d)
print('----------snip------------')
print(arr3d[1, 0])
print('----------snip------------')
print(arr3d[1, 1, 2])
print('----------snip------------')
# 切片索引
arr = np.arange(10)
print(arr[1:6])
print('----------snip------------')
print(arr2d)
print('----------snip------------')
print(arr2d[:2])  # 沿着第0轴切片的
print('----------snip------------')
# 一次传入多个切片
print(arr2d[:2, 1:])
# 通过将整数索引和切片混合，可以得到低维度的切片
print(arr2d[1, :2])
print('----------snip------------')
print(arr2d[2, :1])
print('----------snip------------')
# 注意:只有冒号表示选取整个轴
print(arr2d[:, :1])
print('----------snip------------')
# 对切片表达式赋值也会扩散到整个选区
arr2d[:2, 1:] = 0
print(arr2d)
print('----------snip------------')
# 布尔型索引
names = np.array(['curry', 'bob', 'will', 'bob', 'harden', 'durant', 'james'])
data = np.random.randn(7, 4)
print(names)
print('----------snip------------')
print(data)
# 对names和字符串bob的比较运算会产生一个布尔型数组
print(names == 'bob')
# 可以使用这个布尔型数组作为数组索引
print(data[names == 'bob'])
print('----------snip------------')
# 布尔型数组的长度必须与被索引的轴长度一致，此外可以将布尔型数组跟切片、整数混合使用
print(data[names == 'bob', 2:])
print('----------snip------------')
print(data[names == 'bob', 3])
print('----------snip------------')
# 可以使用不等号!=,符号-对条件进行否定
print(names != 'bob')
print('----------snip------------')
print(data[~(names == 'bob')])
# 选取三个名字中的两个需要组合应用多个布尔条件
mask = (names == 'bob') | (names == 'james')
print(mask)
print('----------snip------------')
print(data[mask])
print('----------snip------------')
# 注：通过布尔型索引选取数组中的数据，将总是创建数据的副本
# 通过布尔型数组设置值是一种常用手段,将data中的负数设为0
data[data < 0] = 0
print(data)
print('----------snip------------')
# 通过一维布尔数组设置整行或整列的值
data[names != 'james'] = 7
print(data)
print('----------snip------------')
# 花式索引和切片不同，它总是将数据复制到新数组
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
print('----------snip------------')
# 以特定顺序选取行子集，只需要传入一个用于指定顺序的整数列表或ndarray
print(arr[[4, 3, 0, 6]])
print('----------snip------------')
# 使用负数索引将会从末尾开始选取行
print(arr[[-3, -5, -7]])
print('----------snip------------')
# 一次传入多个索引数组，将返回一个一维数组,其中的元素对应各个索引元组
arr = np.arange(32).reshape((8, 4))
print(arr)
print('----------snip------------')
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print('----------snip------------')
# 选取矩阵的行列子集应该是一个矩形区域
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print('----------snip------------')
# 另一个方法是使用np.ix_函数，将两个一维整数数组转化为一个用于选取方形区域的索引器
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
print('----------snip------------')
