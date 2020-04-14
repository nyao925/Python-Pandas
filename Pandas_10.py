'''str.split（）：用定界符分割'''
###pandas.Series
import pandas as pd

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com', 'ddd'], index=['A', 'B', 'C', 'D'])
print(s_org)
print(type(s_org))
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# D            ddd
# dtype: object
# <class 'pandas.core.series.Series'>

s = s_org.str.split('@')
print(s)
print(type(s))
# A    [aaa, xxx.com]
# B    [bbb, yyy.com]
# C    [ccc, zzz.com]
# D             [ddd]
# dtype: object
# <class 'pandas.core.series.Series'>

df = s_org.str.split('@', expand=True)
print(df)
print(type(df))
#      0        1
# A  aaa  xxx.com
# B  bbb  yyy.com
# C  ccc  zzz.com
# D  ddd     None
# <class 'pandas.core.frame.DataFrame'>

###pandas.DataFrame
print(df)
#   local   domain
# A   aaa  xxx.com
# B   bbb  yyy.com
# C   ccc  zzz.com
# D   ddd     None

print(df['domain'].str.split('.', expand=True))
#       0     1
# A   xxx   com
# B   yyy   com
# C   zzz   com
# D  None  None

df2 = pd.concat([df, df['domain'].str.split('.', expand=True)], axis=1).drop('domain', axis=1)
print(df2)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc   zzz   com
# D   ddd  None  None

df3 = pd.concat([df['local'], df['domain'].str.split('.', expand=True)], axis=1)
print(df3)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc   zzz   com
# D   ddd  None  None

'''str.extract()：按正则表达式拆分'''
import pandas as pd

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com', 'ddd'], index=['A', 'B', 'C', 'D'])
print(s_org)
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# D            ddd
# dtype: object

df = s_org.str.extract('(.+)@(.+)\.(.+)', expand=True)
print(df)
#      0    1    2
# A  aaa  xxx  com
# B  bbb  yyy  com
# C  ccc  zzz  com
# D  NaN  NaN  NaN

df = s_org.str.extract('(.+)@(.+)\.(.+)', expand=False)
print(df)
#      0    1    2
# A  aaa  xxx  com
# B  bbb  yyy  com
# C  ccc  zzz  com
# D  NaN  NaN  NaN

df_single = s_org.str.extract('(\w+)', expand=True)
print(df_single)
print(type(df_single))
#      0
# A  aaa
# B  bbb
# C  ccc
# D  ddd
# <class 'pandas.core.frame.DataFrame'>

s = s_org.str.extract('(\w+)', expand=False)
print(s)
print(type(s))
# A    aaa
# B    bbb
# C    ccc
# D    ddd
# dtype: object
# <class 'pandas.core.series.Series'>

df_name = s_org.str.extract('(?P<local>.*)@(?P<second_LD>.*)\.(?P<TLD>.*)', expand=True)
print(df_name)
#   local second_LD  TLD
# A   aaa       xxx  com
# B   bbb       yyy  com
# C   ccc       zzz  com
# D   NaN       NaN  NaN