import pandas as pd

df = pd.read_csv('./data/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
'''行的提取（选择）方法'''
mask = [True, False, True]
df_mask = df[mask]
print(df_mask)
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

'''完全匹配'''
### ==
print(df['state'] == 'CA')
# 0    False
# 1     True
# 2     True
# Name: state, dtype: bool

print(df[df['state'] == 'CA'])
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

'''部分匹配'''
### str.contains()：包含一个特定的字符串
print(df['name'].str.contains('li'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.contains('li')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

### 参数na：缺少值NaN处理
df_nan = df.copy()
df_nan.iloc[2, 0] = float('nan')
print(df_nan)
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 2    NaN   18    CA     70

print(df_nan['name'].str.contains('li'))
# 0     True
# 1    False
# 2      NaN
# Name: name, dtype: object

# print(df_nan[df_nan['name'].str.contains('li')])
# ValueError: cannot index with vector containing NA / NaN values

print(df_nan['name'].str.contains('li', na=False))
# 0     True
# 1    False
# 2    False
# Name: name, dtype: bool

print(df_nan['name'].str.contains('li', na=True))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

### 参数case：大小写我的处理
print(df['name'].str.contains('LI'))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool

print(df['name'].str.contains('LI', case=False))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

### 参数regex：使用正则表达式模式
print(df['name'].str.contains('i.*e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.contains('i.*e', regex=False))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool

df_q = df.copy()
df_q.iloc[2, 0] += '?'
print(df_q)
#        name  age state  point
# 0     Alice   24    NY     64
# 1       Bob   42    CA     92
# 2  Charlie?   18    CA     70

# print(df_q['name'].str.contains('?'))
# error: nothing to repeat at position 0

print(df_q['name'].str.contains('?', regex=False))
# 0    False
# 1    False
# 2     True
# Name: name, dtype: bool

print(df_q['name'].str.contains('\?'))
# 0    False
# 1    False
# 2     True
# Name: name, dtype: bool

### str.endswith（）：以特定字符串结尾
print(df['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.endswith('e')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

### str.startswith（）：以特定的字符串开头
print(df['name'].str.startswith('B'))
# 0    False
# 1     True
# 2    False
# Name: name, dtype: bool

print(df[df['name'].str.startswith('B')])
#   name  age state  point
# 1  Bob   42    CA     92

### str.match（）：匹配正则表达式模式
print(df['name'].str.match('.*i.*e'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df[df['name'].str.match('.*i.*e')])
#       name  age state  point
# 0    Alice   24    NY     64
# 2  Charlie   18    CA     70

print(df['name'].str.match('.*i'))
# 0     True
# 1    False
# 2     True
# Name: name, dtype: bool

print(df['name'].str.match('i.*e'))
# 0    False
# 1    False
# 2    False
# Name: name, dtype: bool