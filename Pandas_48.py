import array
import numpy as np
import pandas as pd

l = ['apple', 100, 0.123]
print(l)
# ['apple', 100, 0.123]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l[1])
# 100

print(l_2d[1])
# [3, 4, 5]

print(l_2d[1][1])
# 4

print(l[:2])
# ['apple', 100]


arr_int = array.array('i', [0, 1, 2])
print(arr_int)
# array('i', [0, 1, 2])

arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
# array('f', [0.0, 0.10000000149011612, 0.20000000298023224])

# arr_int = array.array('i', [0, 0.1, 2])
# TypeError: integer argument expected, got float

print(arr_int[1])
# 1

print(sum(arr_int))
# 3

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

print(arr[1])
# 1

print(arr_2d[1, 1])
# 4

print(arr_2d[0, 1:])
# [1 2]

print(np.sqrt(arr_2d))
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.dot(arr_1, arr_2))
# [[ 9 12 15]
#  [19 26 33]]

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df['sex'] = ['Female', 'Male', 'Male', 'Male', 'Female', 'Male']
print(df)
#          age state  point     sex
# name
# Alice     24    NY     64  Female
# Bob       42    CA     92    Male
# Charlie   18    CA     70    Male
# Dave      68    TX     70    Male
# Ellen     24    CA     88  Female
# Frank     30    NY     57    Male

print(df.mean())
# age      34.333333
# point    73.500000
# dtype: float64

print(df.pivot_table(index='state', columns='sex', aggfunc='mean'))
#          age        point
# sex   Female  Male Female  Male
# state
# CA      24.0  30.0   88.0  81.0
# NY      24.0  30.0   64.0  57.0
# TX       NaN  68.0    NaN  70.0