import pandas as pd
import numpy as np

df = pd.read_csv('./data/06/sample_header.csv')
print(df)
#     a   b   c   d
# 0  11  12  13  14
# 1  21  22  23  24
# 2  31  32  33  34

'''指定pandas对象作为NumPy函数的参数'''
###元素的适用
print(np.sqrt(df))
#           a         b         c         d
# 0  3.316625  3.464102  3.605551  3.741657
# 1  4.582576  4.690416  4.795832  4.898979
# 2  5.567764  5.656854  5.744563  5.830952

###行/列的应用
print(np.amax(df))
# a    31
# b    32
# c    33
# d    34
# dtype: int64

print(np.mean(df, axis=1))
# 0    12.5
# 1    22.5
# 2    32.5
# dtype: float64

###pandas.DataFrame，pandas.Series方法
print(df.max())
# a    31
# b    32
# c    33
# d    34
# dtype: int64

print(df.max(axis=1))
# 0    14
# 1    24
# 2    34
# dtype: int64

'''Pandas对象方法的函数应用'''
###适用于Series的每个元素：map（），apply（）
s = df['a']
print(s)
# 0    11
# 1    21
# 2    31
# Name: a, dtype: int64

f_brackets = lambda x: '[{}]'.format(x)
print(s.map(f_brackets))
# 0    [11]
# 1    [21]
# 2    [31]
# Name: a, dtype: object

def f_str(x):
    return str(x).replace('1', 'One').replace('2', 'Two').replace('3', 'Three').replace('4', 'Four')

print(s.map(f_str))
# 0      OneOne
# 1      TwoOne
# 2    ThreeOne
# Name: a, dtype: object

###应用于DataFrame的每个元素：applymap（）
f_oddeven = lambda x: 'odd' if x % 2 == 1 else 'even'
print(df.applymap(f_oddeven))
#      a     b    c     d
# 0  odd  even  odd  even
# 1  odd  even  odd  even
# 2  odd  even  odd  even

###应用于DataFrame的每行和每列：apply（）
f_maxmin = lambda x: max(x) - min(x)
print(df.apply(f_maxmin))
# a    20
# b    20
# c    20
# d    20
# dtype: int64

print(df.apply(f_maxmin, axis=1))
# 0    3
# 1    3
# 2    3
# dtype: int64

###应用于DataFrame的特定行/列元素
df['b'] = df['b'].map(f_str)
print(df)
#     a         b   c   d
# 0  11    OneTwo  13  14
# 1  21    TwoTwo  23  24
# 2  31  ThreeTwo  33  34

df.iloc[2] = df.iloc[2].map(f_str)
print(df)
#           a         b           c          d
# 0        11    OneTwo          13         14
# 1        21    TwoTwo          23         24
# 2  ThreeOne  ThreeTwo  ThreeThree  ThreeFour

