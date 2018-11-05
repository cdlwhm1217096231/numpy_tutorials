#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np

##################基本数据类型#######################
'''
数据类型	描述
bool_	    布尔（True或False），存储为一个字节
int_	    默认整数类型（与C long相同；通常为int64或int32）
intc	    与C int（通常为int32或int64）相同
intp	    用于索引的整数（与C ssize_t相同；通常为int32或int64）
int8	    字节（-128到127）
int16	    整数（-32768到32767）
int32	    整数（-2147483648至2147483647）
int64	    整数（-9223372036854775808至9223372036854775807）
uint8	    无符号整数（0到255）
uint16	    无符号整数（0到65535）
uint32	    无符号整数（0至4294967295）
uint64	    无符号整数（0至18446744073709551615）
float_	    float64的简写
float16	    半精度浮点：符号位，5位指数，10位尾数
float32	    单精度浮点：符号位，8位指数，23位尾数
float64	    双精度浮点：符号位，11位指数，52位尾数
complex_	complex128的简写
complex64	复数，由两个32位浮点（实数和虚数分量）
complex128	复数，由两个64位浮点（实数和虚数分量）
'''
# 上面的类型都可以在创建 ndarray 时通过参数 dtype 来指定
a = np.array([1, 2, 3, 4], dtype=np.float32)
print(a)
print(a.dtype)
# 类型转换
# 要转换数组的类型，可以使用.astype()方法
""".astype()每次返回一个新的数组，即使转换的类型是相同的"""
a = np.array([0, 1, 2], dtype=np.float16)
print(a)
print(a.astype(np.bool_))
print(a.astype(np.float16) is a)
