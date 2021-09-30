import pandas as pd
import numpy as np
import math

df = pd.read_csv('./data/sample_pandas_normal_nan.csv')
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

'''Pandas中缺少值NaN的介绍'''
df = pd.read_csv('./data/sample_pandas_normal_nan.csv')
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.dtypes)
# name      object
# age      float64
# state     object
# point    float64
# other    float64
# dtype: object

print(df.at[1, 'name'])
print(type(df.at[1, 'name']))
# nan
# <class 'float'>

print(df.at[0, 'point'])
print(type(df.at[0, 'point']))
# nan
# <class 'numpy.float64'>

print(pd.isnull(df.at[0, 'point']))
print(np.isnan(df.at[0, 'point']))
print(math.isnan(df.at[0, 'point']))
# True
# True
# True

'''将缺失值作为Pandas中的缺少值NaN'''
s_nan = pd.Series([None, np.nan, math.nan, pd.np.nan])
print(s_nan)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# dtype: float64

print(s_nan[0])
print(type(s_nan[0]))
# nan
# <class 'numpy.float64'>

print(s_nan.isnull())
# 0    True
# 1    True
# 2    True
# 3    True
# dtype: bool

s_nan_int = pd.Series([None, pd.np.nan, 0, 1])
print(s_nan_int)
# 0    NaN
# 1    NaN
# 2    0.0
# 3    1.0
# dtype: float64

print(s_nan_int.isnull())
# 0     True
# 1     True
# 2    False
# 3    False
# dtype: bool

s_nan_str = pd.Series([None, pd.np.nan, 'NaN', 'nan'])
print(s_nan_str)
# 0    None
# 1     NaN
# 2     NaN
# 3     nan
# dtype: object

print(s_nan_str[0])
print(type(s_nan_str[0]))
# None
# <class 'NoneType'>

print(s_nan_str.isnull())
# 0     True
# 1     True
# 2    False
# 3    False
# dtype: bool

s_nan_str_replace = s_nan_str.replace({'NaN': pd.np.nan, 'nan': pd.np.nan})
print(s_nan_str_replace)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# dtype: float64

print(s_nan_str_replace.isnull())
# 0    True
# 1    True
# 2    True
# 3    True
# dtype: bool

'''缺少值NaN的删除方法'''
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

###删除所有值均缺失的行/列
print(df.dropna(how='all'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.dropna(how='all', axis=1))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df.dropna(how='all').dropna(how='all', axis=1))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

###删除至少包含一个缺失值的行/列
df2 = df.dropna(how='all').dropna(how='all', axis=1)
print(df2)
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.dropna(how='any'))
#    name   age state  point
# 3  Dave  68.0    TX   70.0

print(df2.dropna())
#    name   age state  point
# 3  Dave  68.0    TX   70.0

print(df2.dropna(how='any', axis=1))
#       name
# 0    Alice
# 2  Charlie
# 3     Dave
# 4    Ellen
# 5    Frank

###根据不缺少值的元素数量删除行/列
print(df.dropna(thresh=3))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN
# 4  Ellen   NaN    CA   88.0    NaN

print(df.dropna(thresh=3, axis=1))
#       name   age state
# 0    Alice  24.0    NY
# 1      NaN   NaN   NaN
# 2  Charlie   NaN    CA
# 3     Dave  68.0    TX
# 4    Ellen   NaN    CA
# 5    Frank  30.0   NaN

###删除特定行/列中缺少值的列/行
print(df.dropna(subset=['age']))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN
# 5  Frank  30.0   NaN    NaN    NaN

print(df.dropna(subset=['age', 'state']))
#     name   age state  point  other
# 0  Alice  24.0    NY    NaN    NaN
# 3   Dave  68.0    TX   70.0    NaN

print(df.dropna(subset=['age', 'state'], how='all'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.dropna(subset=[0, 4], axis=1))
#       name state
# 0    Alice    NY
# 1      NaN   NaN
# 2  Charlie    CA
# 3     Dave    TX
# 4    Ellen    CA
# 5    Frank   NaN

print(df.dropna(subset=[0, 4], axis=1, how='all'))
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 1      NaN   NaN   NaN    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN
###pandas.Series
s = df['age']
print(s)
# 0    24.0
# 1     NaN
# 2     NaN
# 3    68.0
# 4     NaN
# 5    30.0
# Name: age, dtype: float64

print(s.dropna())
# 0    24.0
# 3    68.0
# 5    30.0
# Name: age, dtype: float64

'''替换（填充）缺失值'''
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

###用通用值统一替换
print(df.fillna(0))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    0.0
# 1        0   0.0     0    0.0    0.0
# 2  Charlie   0.0    CA    0.0    0.0
# 3     Dave  68.0    TX   70.0    0.0
# 4    Ellen   0.0    CA   88.0    0.0
# 5    Frank  30.0     0    0.0    0.0

###为每列替换不同的值
print(df.fillna({'name': 'XXX', 'age': 20, 'point': 0}))
#       name   age state  point  other
# 0    Alice  24.0    NY    0.0    NaN
# 1      XXX  20.0   NaN    0.0    NaN
# 2  Charlie  20.0    CA    0.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  20.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    0.0    NaN

s_for_fill = pd.Series(['ZZZ', 100], index=['name', 'age'])
print(s_for_fill)
# name    ZZZ
# age     100
# dtype: object

print(df.fillna(s_for_fill))
#       name    age state  point  other
# 0    Alice   24.0    NY    NaN    NaN
# 1      ZZZ  100.0   NaN    NaN    NaN
# 2  Charlie  100.0    CA    NaN    NaN
# 3     Dave   68.0    TX   70.0    NaN
# 4    Ellen  100.0    CA   88.0    NaN
# 5    Frank   30.0   NaN    NaN    NaN

###用每列的平均值，中位数，最频繁值等替换
print(df.mean())
# age      40.666667
# point    79.000000
# other          NaN
# dtype: float64

print(df.fillna(df.mean()))
#       name        age state  point  other
# 0    Alice  24.000000    NY   79.0    NaN
# 1      NaN  40.666667   NaN   79.0    NaN
# 2  Charlie  40.666667    CA   79.0    NaN
# 3     Dave  68.000000    TX   70.0    NaN
# 4    Ellen  40.666667    CA   88.0    NaN
# 5    Frank  30.000000   NaN   79.0    NaN

print(df.fillna(df.median()))
#       name   age state  point  other
# 0    Alice  24.0    NY   79.0    NaN
# 1      NaN  30.0   NaN   79.0    NaN
# 2  Charlie  30.0    CA   79.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN   79.0    NaN

print(df.fillna(df.mode().iloc[0]))
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1    Alice  24.0    CA   70.0    NaN
# 2  Charlie  24.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  24.0    CA   88.0    NaN
# 5    Frank  30.0    CA   70.0    NaN

###替换为上一个或下一个值
print(df.fillna(method='ffill'))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1    Alice  24.0    NY    NaN    NaN
# 2  Charlie  24.0    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  68.0    CA   88.0    NaN
# 5    Frank  30.0    CA   88.0    NaN

print(df.fillna(method='bfill'))
#       name   age state  point  other
# 0    Alice  24.0    NY   70.0    NaN
# 1  Charlie  68.0    CA   70.0    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

###指定连续更换的最大数量
print(df.fillna(method='bfill', limit=1))
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1  Charlie   NaN    CA    NaN    NaN
# 2  Charlie  68.0    CA   70.0    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen  30.0    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

###pandas.Series
s = df['age']
print(s)
# 0    24.0
# 1     NaN
# 2     NaN
# 3    68.0
# 4     NaN
# 5    30.0
# Name: age, dtype: float64

print(s.fillna(100))
# 0     24.0
# 1    100.0
# 2    100.0
# 3     68.0
# 4    100.0
# 5     30.0
# Name: age, dtype: float64

print(s.fillna({1: 100, 4: 0}))
# 0     24.0
# 1    100.0
# 2      NaN
# 3     68.0
# 4      0.0
# 5     30.0
# Name: age, dtype: float64

print(s.fillna(method='bfill', limit=1))
# 0    24.0
# 1     NaN
# 2    68.0
# 3    68.0
# 4    30.0
# 5    30.0
# Name: age, dtype: float64

'''提取缺失值'''
###提取特定行/列中缺少值的列/行
print(df)
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 3     Dave  68.0    TX   70.0    NaN
# 4    Ellen   NaN    CA   88.0    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df['point'].isnull())
# 0     True
# 1     True
# 2     True
# 3    False
# 4    False
# 5     True
# Name: point, dtype: bool

print(df[df['point'].isnull()])
#       name   age state  point  other
# 0    Alice  24.0    NY    NaN    NaN
# 1      NaN   NaN   NaN    NaN    NaN
# 2  Charlie   NaN    CA    NaN    NaN
# 5    Frank  30.0   NaN    NaN    NaN

print(df.iloc[2].isnull())
# name     False
# age       True
# state    False
# point     True
# other     True
# Name: 2, dtype: bool

print(df.loc[:, df.iloc[2].isnull()])
#     age  point  other
# 0  24.0    NaN    NaN
# 1   NaN    NaN    NaN
# 2   NaN    NaN    NaN
# 3  68.0   70.0    NaN
# 4   NaN   88.0    NaN
# 5  30.0    NaN    NaN

###提取至少包含一个缺失值的行/列
df2 = df.dropna(how='all').dropna(how='all', axis=1)
print(df2)
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 3     Dave  68.0    TX   70.0
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.isnull())
#     name    age  state  point
# 0  False  False  False   True
# 2  False   True  False   True
# 3  False  False  False  False
# 4  False   True  False  False
# 5  False  False   True   True

print(df2.isnull().any(axis=1))
# 0     True
# 2     True
# 3    False
# 4     True
# 5     True
# dtype: bool

print(df2[df2.isnull().any(axis=1)])
#       name   age state  point
# 0    Alice  24.0    NY    NaN
# 2  Charlie   NaN    CA    NaN
# 4    Ellen   NaN    CA   88.0
# 5    Frank  30.0   NaN    NaN

print(df2.isnull().any())
# name     False
# age       True
# state     True
# point     True
# dtype: bool

print(df2.loc[:, df2.isnull().any()])
#     age state  point
# 0  24.0    NY    NaN
# 2   NaN    CA    NaN
# 3  68.0    TX   70.0
# 4   NaN    CA   88.0
# 5  30.0   NaN    NaN