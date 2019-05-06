#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-6-19 15:30
# @Author  : Leo.Liu
# @Site    : 
# @File    : ch5_pandas.py
# @Software: PyCharm Community Edition

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Series 是一种类似于一维数组的对象，由一组数据及一组与之相关的数据标签（即索引）组成。
obj = Series([4, 7, -5, 3])

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj2[obj2 > 0]

obj2 * 2

np.exp(obj2)

# 可以通过字典来创建Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)

# isnull, notnull
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()


# DataFrame
# DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型

# 最常用的一种构建DataFrame方法是直接传入一个由等长列表或NumPy数组组成的字典
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

# 如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
DataFrame(data, columns=['year', 'state', 'pop'])


# 如果传入的列在数据中找不到，就会产生NA值
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
frame2['state']

frame2.year

# 行也可以通过位置或名称的方式进行获取
frame2.ix['three']

# 列可以通过赋值的方式进行修改
frame2['debt'] = 16.5
frame2['debt'] = np.arrange(5.)

# 将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val

# 为不存在的列赋值会创建出一个新列
frame2['eastern'] = frame2.state == 'Ohio'

# 关键字del用于删除列
del frame2['eastern']


# 另一种常见的数据形式是嵌套字典（字典中的字典）
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)

# 转置
frame3.T


# 索引对象
# pandas的索引对象负责管理轴标签和其他元数据（比如轴名称）。构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个index
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index





# 基本功能

# 重新索引 reindex
# 创建一个适应新索引的新对象
# 参数 : index, mothod, fill_value, limit, level, copy
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)

# 丢弃指定轴上的项
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')

# 删除任意轴上的索引
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data.drop(['Colorado', 'Ohio'])

# 索引、选取和过滤
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj['b']
obj[1]

obj[2:4]
obj[['b', 'a', 'd']]

obj[[1, 3]]
obj[obj < 2]

obj[obj['c'] > 2]

obj < 5
obj[obj < 2] = 0

# 索引字段 ix
data.ix['Colorado', ['two', 'three']]

# 算术运算和数据对齐
# 自动的数据对齐操作在不重叠的索引处引入NA值
df1 + df2

# 在运算中填充
df1.add(df2, fill_value=0)

# 类似的，在对series 或 DataFrame重新索引时，也可以指定填充值
df1.reindex(columns=df2.columns, fill_value=0)

# 函数应用和映射
np.abs(frame)

# apply方法实现将函数应用到各列或各行所形成的一维数组上
f = lambda x: x.max() - x.min()
frame.apply(f)

frame.apply(f, axis=1)

# 排序和排名
# sort_index()对某个轴上的索引排序
obj.sort_index()

obj.sort_index(axis=1)

obj.sort_index(axis=1, ascending=False)

# order() 对Series按值进行排序
obj.order()

# 汇总和计算描述统计

调用DataFrame的sum方法将会返回一个含有列小计的Series
df.sum()

传入axis=1将按行进行求和运算

