#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

'''用于数组的文件输入输出'''


# 将数组以二进制格式保存到磁盘
# np.save() np.load()是读写磁盘数组数据的两个主要函数。默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中的
arr = np.arange(10)
np.save('some_array', arr)
# 通过np.load 读取磁盘上的数组
print(np.load('some_array.npy'))
# 通过np.savez可以将多个数组保存到一个压缩文件中,将数组以关键字参数的形式传入即可
np.savez('array_archive.npz', a=arr, b=arr)
# 加载.npz文件时,会得到一个类型字典的对象，该对象会对各个数组进行延时加载
arch = np.load('array_archive.npz')
print(arch['b'])
print('-----------snip-----------')
# 存取文本文件
arr = np.loadtxt('carry.txt', delimiter=',')
print(arr)
# 存储文本
# np.savetxt()执行的是相反的操作：将数组写到以某种分隔符隔开的文本文件中


