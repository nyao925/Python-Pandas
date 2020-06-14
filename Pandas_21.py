import pandas as pd

df = pd.read_csv('./data/21/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

'''使用reset_index（）将索引重新分配给序列号'''
df.sort_values('state', inplace=True)
print(df)
#       name  age state  point
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 0    Alice   24    NY     64
# 5    Frank   30    NY     57
# 3     Dave   68    TX     70

### 基本用法
df_r = df.reset_index()
print(df_r)
#    index     name  age state  point
# 0      1      Bob   42    CA     92
# 1      2  Charlie   18    CA     70
# 2      4    Ellen   24    CA     88
# 3      0    Alice   24    NY     64
# 4      5    Frank   30    NY     57
# 5      3     Dave   68    TX     70

### 删除原始索引：参数drop
df_r = df.reset_index(drop=True)
print(df_r)
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70

### 更改原始对象：参数inplace
df.reset_index(inplace=True, drop=True)
print(df)
#       name  age state  point
# 0      Bob   42    CA     92
# 1  Charlie   18    CA     70
# 2    Ellen   24    CA     88
# 3    Alice   24    NY     64
# 4    Frank   30    NY     57
# 5     Dave   68    TX     70

'''使用reset_index（）和set_index（）将索引更改为另一列（重置）'''
df = pd.read_csv('./data/21/sample_pandas_normal.csv', index_col=0)
# print(df)
# #          age state  point
# # name
# # Alice     24    NY     64
# # Bob       42    CA     92
# # Charlie   18    CA     70
# # Dave      68    TX     70
# # Ellen     24    CA     88
# # Frank     30    NY     57

df_r = df.reset_index()
print(df_r)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_s = df.set_index('state')
print(df_s)
#        age  point
# state
# NY      24     64
# CA      42     92
# CA      18     70
# TX      68     70
# CA      24     88
# NY      30     57

df_rs = df.reset_index().set_index('state')
print(df_rs)
#           name  age  point
# state
# NY       Alice   24     64
# CA         Bob   42     92
# CA     Charlie   18     70
# TX        Dave   68     70
# CA       Ellen   24     88
# NY       Frank   30     57