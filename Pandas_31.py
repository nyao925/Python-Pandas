import numpy as np
import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a_df = df.values
print(a_df)
# [[1 2 3]
#  [4 5 6]]

print(type(a_df))
# <class 'numpy.ndarray'>

print(a_df.dtype)
# int64

s = df['a']
print(s)
# 0    1
# 1    4
# Name: a, dtype: int64

a_s = s.values
print(a_s)
# [1 4]

print(type(a_s))
# <class 'numpy.ndarray'>

print(a_s.dtype)
# int64

df_f = pd.DataFrame([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
print(df_f)
#      0    1    2
# 0  0.1  0.2  0.3
# 1  0.4  0.5  0.6

a_df_f = df_f.values
print(a_df_f)
# [[0.1 0.2 0.3]
#  [0.4 0.5 0.6]]

print(type(a_df_f))
# <class 'numpy.ndarray'>

print(a_df_f.dtype)
# float64

df_multi = pd.read_csv('./data/sample_pandas_normal.csv')
print(df_multi)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

a_df_multi = df_multi.values
print(a_df_multi)
# [['Alice' 24 'NY' 64]
#  ['Bob' 42 'CA' 92]
#  ['Charlie' 18 'CA' 70]
#  ['Dave' 68 'TX' 70]
#  ['Ellen' 24 'CA' 88]
#  ['Frank' 30 'NY' 57]]

print(type(a_df_multi))
# <class 'numpy.ndarray'>

print(a_df_multi.dtype)
# object

a_df_int = df_multi[['age', 'point']].values
print(a_df_int)
# [[24 64]
#  [42 92]
#  [18 70]
#  [68 70]
#  [24 88]
#  [30 57]]

print(type(a_df_int))
# <class 'numpy.ndarray'>

print(a_df_int.dtype)
# int64

print(a_df_int.T)
# [[24 42 18 68 24 30]
#  [64 92 70 70 88 57]]

a_df_int = df_multi.select_dtypes(include=int).values
print(a_df_int)
# [[24 64]
#  [42 92]
#  [18 70]
#  [68 70]
#  [24 88]
#  [30 57]]

print(type(a_df_int))
# <class 'numpy.ndarray'>

print(a_df_int.dtype)
# int64

import numpy as np
import pandas as pd

a = np.arange(4)
print(a)
# [0 1 2 3]

s = pd.Series(a)
print(s)
# 0    0
# 1    1
# 2    2
# 3    3
# dtype: int64

index = ['A', 'B', 'C', 'D']
name = 'sample'
s = pd.Series(data=a, index=index, name=name, dtype='float')
print(s)
# A    0.0
# B    1.0
# C    2.0
# D    3.0
# Name: sample, dtype: float64

a = np.arange(12).reshape((4, 3))
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# s = pd.Series(a)
# print(s)
# Exception: Data must be 1-dimensional

s = pd.Series(a[2])
print(s)
# 0    6
# 1    7
# 2    8
# dtype: int64

s = pd.Series(a.T[2])
print(s)
# 0     2
# 1     5
# 2     8
# 3    11
# dtype: int64

a = np.arange(12).reshape((4, 3))
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

df = pd.DataFrame(a)
print(df)
#    0   1   2
# 0  0   1   2
# 1  3   4   5
# 2  6   7   8
# 3  9  10  11

index = ['A', 'B', 'C', 'D']
columns = ['a', 'b', 'c']
df = pd.DataFrame(data=a, index=index, columns=columns, dtype='float')
print(df)
#      a     b     c
# A  0.0   1.0   2.0
# B  3.0   4.0   5.0
# C  6.0   7.0   8.0
# D  9.0  10.0  11.0

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a_values = df.values
print(a_values)
# [[1 2 3]
#  [4 5 6]]

print(np.shares_memory(a_values, df))
# True

a_values[0, 0] = 100
print(a_values)
# [[100   2   3]
#  [  4   5   6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

df_if = pd.DataFrame(data=[[1, 0.1], [2, 0.2]], columns=['int', 'float'])
print(df_if)
#    int  float
# 0    1    0.1
# 1    2    0.2

print(df_if.dtypes)
# int        int64
# float    float64
# dtype: object

a_values_if = df_if.values
print(a_values_if)
# [[1.  0.1]
#  [2.  0.2]]

print(np.shares_memory(a_values_if, df_if))
# False

a_values_if[0, 0] = 100
print(a_values_if)
# [[100.    0.1]
#  [  2.    0.2]]

print(df_if)
#    int  float
# 0    1    0.1
# 1    2    0.2

print(df[['a', 'c']].values)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df[['a', 'c']].values, df))
# False

print(df.iloc[:, ::2].values)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df.iloc[:, ::2].values, df))
# True

a_values_copy = df.values.copy()
print(a_values_copy)
# [[100   2   3]
#  [  4   5   6]]

print(np.shares_memory(a_values_copy, df))
# False

a_values_copy[0, 0] = 10
print(a_values_copy)
# [[10  2  3]
#  [ 4  5  6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
# [[1 2 3]
#  [4 5 6]]

df_a = pd.DataFrame(a, columns=['a', 'b', 'c'])
print(df_a)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

print(np.shares_memory(a, df_a))
# True

a[0, 0] = 100
print(a)
# [[100   2   3]
#  [  4   5   6]]

print(df_a)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

df_a.iat[1, 0] = 10
print(df_a)
#      a  b  c
# 0  100  2  3
# 1   10  5  6

print(a)
# [[100   2   3]
#  [ 10   5   6]]

df_a_copy = pd.DataFrame(a.copy(), columns=['a', 'b', 'c'])
print(df_a_copy)
#      a  b  c
# 0  100  2  3
# 1   10  5  6

a[0, 0] = 1
print(a)
# [[ 1  2  3]
#  [10  5  6]]

print(df_a_copy)
#      a  b  c
# 0  100  2  3
# 1   10  5  6

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(df)
#    a  b  c
# 0  1  2  3
# 1  4  5  6

a = df.to_numpy()
print(a)
# [[1 2 3]
#  [4 5 6]]

print(type(a))
# <class 'numpy.ndarray'>

print(np.shares_memory(df, a))
# True

a[0, 0] = 100
print(a)
# [[100   2   3]
#  [  4   5   6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a_copy = df.to_numpy(copy=True)
print(a_copy)
# [[100   2   3]
#  [  4   5   6]]

print(np.shares_memory(df, a_copy))
# False

a_copy[0, 0] = 10
print(a_copy)
# [[10  2  3]
#  [ 4  5  6]]

print(df)
#      a  b  c
# 0  100  2  3
# 1    4  5  6

a_cols = df[['a', 'c']].to_numpy()
print(a_cols)
# [[100   3]
#  [  4   6]]

print(np.shares_memory(df, a_cols))
# False

a_f = df.to_numpy(dtype=float)
print(a_f)
# [[100.   2.   3.]
#  [  4.   5.   6.]]

print(np.shares_memory(df, a_f))
# False