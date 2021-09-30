import pandas as pd

df = pd.read_csv('./data/sample_pandas_normal.csv', index_col=0)
print(df)
#          age state  point
# name
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.index.values)
# ['Alice' 'Bob' 'Charlie' 'Dave' 'Ellen' 'Frank']

print(df.columns.values)
# ['age' 'state' 'point']

'''at，iat：选择，获取和更改单个元素的值'''
print(df.at['Bob', 'age'])
print(df.at['Dave', 'state'])
# 42
# TX

df.at['Bob', 'age'] = 60
print(df.at['Bob', 'age'])
# 60

print(df.iat[1, 0])
print(df.iat[3, 1])
# 60
# TX

df.iat[1, 0] = 42
print(df.iat[1, 0])
# 42
'''loc，iloc：选择，获取和更改单个和多个元素的值'''
###选择单个元素的值
print(df.loc['Bob', 'age'])
print(df.iloc[3, 1])
# 42
# TX

df.loc['Bob', 'age'] = 60
print(df.loc['Bob', 'age'])
# 60

df.iloc[1, 0] = 42
print(df.iloc[1, 0])
# 42

###选择多个元素值
print(df.loc['Bob':'Dave', 'age'])
print(type(df.loc['Bob':'Dave', 'age']))
# name
# Bob        42
# Charlie    18
# Dave       68
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.loc[:'Dave', ['age', 'point']])
print(type(df.loc[:'Dave', 'age':'point']))
#          age  point
# name
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:3, [0, 2]])
print(type(df.iloc[:3, [0, 2]]))
#          age  point
# name
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[::2, 0])
print(type(df.iloc[::2, 0]))
# name
# Alice      24
# Charlie    18
# Ellen      24
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.iloc[1::2, 0])
print(type(df.iloc[1::2, 0]))
# name
# Bob      42
# Dave     68
# Frank    30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df.loc['Bob':'Dave', 'age'])
# name
# Bob        20
# Charlie    30
# Dave       40
# Name: age, dtype: int64

###选择行/列
print(df['Bob':'Ellen'])
#          age state  point
# name
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88

print(df[:3])
#          age state  point
# name
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70

print(df['age'])
# name
# Alice      24
# Bob        20
# Charlie    30
# Dave       40
# Ellen      24
# Frank      30
# Name: age, dtype: int64

print(df[['age', 'point']])
#          age  point
# name
# Alice     24     64
# Bob       20     92
# Charlie   30     70
# Dave      40     70
# Ellen     24     88
# Frank     30     57

print(df.loc['Bob'])
print(type(df.loc['Bob']))
# age      20
# state    CA
# point    92
# Name: Bob, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[[1, 4]])
print(type(df.iloc[[1, 4]]))
#        age state  point
# name
# Bob     20    CA     92
# Ellen   24    CA     88
# <class 'pandas.core.frame.DataFrame'>

print(df.loc[:, 'age':'point'])
print(type(df.loc[:, 'age':'point']))
#          age state  point
# name
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[:, [0, 2]])
print(type(df.iloc[:, [0, 2]]))
#          age  point
# name
# Alice     24     64
# Bob       20     92
# Charlie   30     70
# Dave      40     70
# Ellen     24     88
# Frank     30     57
# <class 'pandas.core.frame.DataFrame'>

'''当行名和列名具有重复值时'''
df_state = pd.read_csv('./data/sample_pandas_normal.csv', index_col=2)
print(df_state)
#           name  age  point
# state
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57

print(df_state.index.values)
# ['NY' 'CA' 'CA' 'TX' 'CA' 'NY']

print(df_state.at['NY', 'age'])
print(type(df_state.at['NY', 'age']))
# [24 30]
# <class 'numpy.ndarray'>

print(df_state.loc['NY', 'age'])
print(type(df_state.loc['NY', 'age']))
# state
# NY    24
# NY    30
# Name: age, dtype: int64
# <class 'pandas.core.series.Series'>

print(df_state.loc['NY', ['age', 'point']])
print(type(df_state.loc['NY', ['age', 'point']]))
#        age  point
# state
# NY      24     64
# NY      30     57
# <class 'pandas.core.frame.DataFrame'>

print(df_state.iat[0, 1])
# 24

print(df_state.index.is_unique)
# False

print(df_state.columns.is_unique)
# True

'''通过数字和标签指定位置'''
print(df)
#          age state  point
# name
# Alice     24    NY     64
# Bob       20    CA     92
# Charlie   30    CA     70
# Dave      40    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.index[2])
# Charlie

print(df.columns[1])
# state

print(df.at[df.index[2], 'age'])
# 30

print(df.loc[['Alice', 'Dave'], df.columns[1]])
# name
# Alice    NY
# Dave     TX
# Name: state, dtype: object

print(df['age'][2])
# 30

print(df.age[2])
# 30

print(df.loc[['Alice', 'Dave']].iloc[:, 1])
# name
# Alice    NY
# Dave     TX
# Name: state, dtype: object

'''在pandas.Series中选择行时的隐式类型转换'''
df_mix = pd.DataFrame({'col_int': [0, 1, 2], 'col_float': [0.1, 0.2, 0.3]}, index=['A', 'B', 'C'])
print(df_mix)
#    col_int  col_float
# A        0        0.1
# B        1        0.2
# C        2        0.3

print(df_mix.dtypes)
# col_int        int64
# col_float    float64
# dtype: object

print(df_mix.loc['B'])
# col_int      1.0
# col_float    0.2
# Name: B, dtype: float64

print(type(df_mix.loc['B']))
# <class 'pandas.core.series.Series'>

print(df_mix.loc['B']['col_int'])
# 1.0

print(type(df_mix.loc['B']['col_int']))
# <class 'numpy.float64'>

print(df_mix.at['B', 'col_int'])
# 1

print(type(df_mix.at['B', 'col_int']))
# <class 'numpy.int64'>
print(df_mix.loc[['B']])
#    col_int  col_float
# B        1        0.2

print(type(df_mix.loc[['B']]))
# <class 'pandas.core.frame.DataFrame'>

print(df_mix.loc[['B']].dtypes)
# col_int        int64
# col_float    float64
# dtype: object