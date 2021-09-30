import pandas as pd

df = pd.read_csv('./data/sample_date.csv', index_col=0, parse_dates=True)
print(df)
#             val_1  val_2
# date
# 2017-11-01     65     76
# 2017-11-07     26     66
# 2017-11-18     47     47
# 2017-11-27     20     38
# 2017-12-05     65     85
# 2017-12-12      4     29
# 2017-12-22     31     54
# 2017-12-29     21      8
# 2018-01-03     98     76
# 2018-01-08     48     64
# 2018-01-19     18     48
# 2018-01-23     86     70

print(type(df.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
'''通过resample（）汇总任何期间'''
print(df.resample('W').sum())
#             val_1  val_2
# date
# 2017-11-05     65     76
# 2017-11-12     26     66
# 2017-11-19     47     47
# 2017-11-26      0      0
# 2017-12-03     20     38
# 2017-12-10     65     85
# 2017-12-17      4     29
# 2017-12-24     31     54
# 2017-12-31     21      8
# 2018-01-07     98     76
# 2018-01-14     48     64
# 2018-01-21     18     48
# 2018-01-28     86     70

print(df.resample('M').sum())
#             val_1  val_2
# date
# 2017-11-30    158    227
# 2017-12-31    121    176
# 2018-01-31    250    258

print(df.resample('Q').sum())
#             val_1  val_2
# date
# 2017-12-31    279    403
# 2018-03-31    250    258

print(df.resample('Y').sum())
#             val_1  val_2
# date
# 2017-12-31    279    403
# 2018-12-31    250    258

print(df.resample('10D').sum())
#             val_1  val_2
# date
# 2017-11-01     91    142
# 2017-11-11     47     47
# 2017-11-21     20     38
# 2017-12-01     65     85
# 2017-12-11      4     29
# 2017-12-21     52     62
# 2017-12-31    146    140
# 2018-01-10     18     48
# 2018-01-20     86     70

print(df.resample('3W').sum())
#             val_1  val_2
# date
# 2017-11-05     65     76
# 2017-11-26     73    113
# 2017-12-17     89    152
# 2018-01-07    150    138
# 2018-01-28    152    182

print(df.resample('Y').mean())
#              val_1   val_2
# date
# 2017-12-31  34.875  50.375
# 2018-12-31  62.500  64.500

print(df.resample('Y').agg(['sum', 'mean', 'max', 'min']))
#            val_1                 val_2
#              sum    mean max min   sum    mean max min
# date
# 2017-12-31   279  34.875  65   4   403  50.375  85   8
# 2018-12-31   250  62.500  98  18   258  64.500  76  48

'''星期几：weekday, dayofweek, day_name()'''
print(df.index.weekday)
# Int64Index([2, 1, 5, 0, 1, 1, 4, 4, 2, 0, 4, 1], dtype='int64', name='date')

print(df.index.dayofweek)
# Int64Index([2, 1, 5, 0, 1, 1, 4, 4, 2, 0, 4, 1], dtype='int64', name='date')

print(df.index.day_name())
# Index(['Wednesday', 'Tuesday', 'Saturday', 'Monday', 'Tuesday', 'Tuesday',
#        'Friday', 'Friday', 'Wednesday', 'Monday', 'Friday', 'Tuesday'],
#       dtype='object', name='date')

###通过指定星期几来提取行
print(df[df.index.weekday == 0])
#             val_1  val_2
# date
# 2017-11-27     20     38
# 2018-01-08     48     64

###计算一周中每一天的总数和平均值
print(df[df.index.weekday == 0].sum())
# val_1     68
# val_2    102
# dtype: int64

print(df[df.index.weekday == 0].mean())
# val_1    34.0
# val_2    51.0
# dtype: float64

print(df[df.index.weekday == 0].agg(['sum', 'mean']))
#       val_1  val_2
# sum    68.0  102.0
# mean   34.0   51.0

df_w = df.set_index([df.index.weekday, df.index])
print(df_w)
#                  val_1  val_2
# date date
# 2    2017-11-01     65     76
# 1    2017-11-07     26     66
# 5    2017-11-18     47     47
# 0    2017-11-27     20     38
# 1    2017-12-05     65     85
#      2017-12-12      4     29
# 4    2017-12-22     31     54
#      2017-12-29     21      8
# 2    2018-01-03     98     76
# 0    2018-01-08     48     64
# 4    2018-01-19     18     48
# 1    2018-01-23     86     70

df_w.index.names = ['weekday', 'date']
print(df_w)
#                     val_1  val_2
# weekday date
# 2       2017-11-01     65     76
# 1       2017-11-07     26     66
# 5       2017-11-18     47     47
# 0       2017-11-27     20     38
# 1       2017-12-05     65     85
#         2017-12-12      4     29
# 4       2017-12-22     31     54
#         2017-12-29     21      8
# 2       2018-01-03     98     76
# 0       2018-01-08     48     64
# 4       2018-01-19     18     48
# 1       2018-01-23     86     70

df_w.sort_index(inplace=True)
print(df_w)
#                     val_1  val_2
# weekday date
# 0       2017-11-27     20     38
#         2018-01-08     48     64
# 1       2017-11-07     26     66
#         2017-12-05     65     85
#         2017-12-12      4     29
#         2018-01-23     86     70
# 2       2017-11-01     65     76
#         2018-01-03     98     76
# 4       2017-12-22     31     54
#         2017-12-29     21      8
#         2018-01-19     18     48
# 5       2017-11-18     47     47

print(df_w.sum())
# val_1    529
# val_2    661
# dtype: int64

print(df_w.sum(level='weekday'))
#          val_1  val_2
# weekday
# 0           68    102
# 1          181    250
# 2          163    152
# 4           70    110
# 5           47     47

print(df_w.mean(level='weekday'))
#              val_1      val_2
# weekday
# 0        34.000000  51.000000
# 1        45.250000  62.500000
# 2        81.500000  76.000000
# 4        23.333333  36.666667
# 5        47.000000  47.000000

print(df_w.groupby(level='weekday').agg(['sum', 'mean']))
#         val_1            val_2
#           sum       mean   sum       mean
# weekday
# 0          68  34.000000   102  51.000000
# 1         181  45.250000   250  62.500000
# 2         163  81.500000   152  76.000000
# 4          70  23.333333   110  36.666667
# 5          47  47.000000    47  47.000000

'''其他属性'''
###年: year
print(df.index.year)
# Int64Index([2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2018, 2018, 2018,
#             2018],
#            dtype='int64', name='date')

df_y = df.set_index([df.index.year, df.index])
df_y.index.names = ['year', 'date']
print(df_y)
#                  val_1  val_2
# year date
# 2017 2017-11-01     65     76
#      2017-11-07     26     66
#      2017-11-18     47     47
#      2017-11-27     20     38
#      2017-12-05     65     85
#      2017-12-12      4     29
#      2017-12-22     31     54
#      2017-12-29     21      8
# 2018 2018-01-03     98     76
#      2018-01-08     48     64
#      2018-01-19     18     48
#      2018-01-23     86     70

print(df_y.sum(level='year'))
#       val_1  val_2
# year
# 2017    279    403
# 2018    250    258

###季度：quarter
df_q = df.set_index([df.index.quarter, df.index])
df_q.index.names = ['quarter', 'date']
print(df_q)
#                     val_1  val_2
# quarter date
# 4       2017-11-01     65     76
#         2017-11-07     26     66
#         2017-11-18     47     47
#         2017-11-27     20     38
#         2017-12-05     65     85
#         2017-12-12      4     29
#         2017-12-22     31     54
#         2017-12-29     21      8
# 1       2018-01-03     98     76
#         2018-01-08     48     64
#         2018-01-19     18     48
#         2018-01-23     86     70

print(df_q.sum(level='quarter'))
#          val_1  val_2
# quarter
# 4          279    403
# 1          250    258

###月：month, month_name()
df_m = df.set_index([df.index.month, df.index])
df_m.index.names = ['month', 'date']
print(df_m)
#                   val_1  val_2
# month date
# 11    2017-11-01     65     76
#       2017-11-07     26     66
#       2017-11-18     47     47
#       2017-11-27     20     38
# 12    2017-12-05     65     85
#       2017-12-12      4     29
#       2017-12-22     31     54
#       2017-12-29     21      8
# 1     2018-01-03     98     76
#       2018-01-08     48     64
#       2018-01-19     18     48
#       2018-01-23     86     70

print(df_m.sum(level='month'))
#        val_1  val_2
# month
# 11       158    227
# 12       121    176
# 1        250    258

print(df.index.month_name())
# Index(['November', 'November', 'November', 'November', 'December', 'December',
#        'December', 'December', 'January', 'January', 'January', 'January'],
#       dtype='object', name='date')

###周：week, weekofyear
df_w2 = df.set_index([df.index.week, df.index])
df_w2.index.names = ['week', 'date']
print(df_w2)
#                  val_1  val_2
# week date
# 44   2017-11-01     65     76
# 45   2017-11-07     26     66
# 46   2017-11-18     47     47
# 48   2017-11-27     20     38
# 49   2017-12-05     65     85
# 50   2017-12-12      4     29
# 51   2017-12-22     31     54
# 52   2017-12-29     21      8
# 1    2018-01-03     98     76
# 2    2018-01-08     48     64
# 3    2018-01-19     18     48
# 4    2018-01-23     86     70

print(df_w2.sum(level='week'))
#       val_1  val_2
# week
# 44       65     76
# 45       26     66
# 46       47     47
# 48       20     38
# 49       65     85
# 50        4     29
# 51       31     54
# 52       21      8
# 1        98     76
# 2        48     64
# 3        18     48
# 4        86     70

print(pd.date_range('2017-01-01', '2017-01-07').week)
# Int64Index([52, 1, 1, 1, 1, 1, 1], dtype='int64')

print(pd.date_range('2017-01-01', '2017-01-07').day_name())
# Index(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
#        'Saturday'],
#       dtype='object')

'''通过组合多个属性（星期几，月份，季度，年份等）进行处理'''
df_yw = df.set_index([df.index.year, df.index.weekday, df.index])
df_yw.index.names = ['year', 'weekday', 'date']
df_yw.sort_index(inplace=True)
print(df_yw)
#                          val_1  val_2
# year weekday date
# 2017 0       2017-11-27     20     38
#      1       2017-11-07     26     66
#              2017-12-05     65     85
#              2017-12-12      4     29
#      2       2017-11-01     65     76
#      4       2017-12-22     31     54
#              2017-12-29     21      8
#      5       2017-11-18     47     47
# 2018 0       2018-01-08     48     64
#      1       2018-01-23     86     70
#      2       2018-01-03     98     76
#      4       2018-01-19     18     48

print(df_yw.sum(level='weekday'))
#          val_1  val_2
# weekday
# 0           68    102
# 1          181    250
# 2          163    152
# 4           70    110
# 5           47     47

print(df_yw.sum(level=['year', 'weekday']))
#               val_1  val_2
# year weekday
# 2017 0           20     38
#      1           95    180
#      2           65     76
#      4           52     62
#      5           47     47
# 2018 0           48     64
#      1           86     70
#      2           98     76
#      4           18     48

print(df_yw.loc[(2017, 1), :])
#             val_1  val_2
# date
# 2017-11-07     26     66
# 2017-12-05     65     85
# 2017-12-12      4     29

print(df_yw.xs(1, level='weekday'))
#                  val_1  val_2
# year date
# 2017 2017-11-07     26     66
#      2017-12-05     65     85
#      2017-12-12      4     29
# 2018 2018-01-23     86     70

print(df_yw.loc[(2017, [0, 4]), :])
#                          val_1  val_2
# year weekday date
# 2017 0       2017-11-27     20     38
#      4       2017-12-22     31     54
#              2017-12-29     21      8

print(df_yw.loc[pd.IndexSlice[:, [0, 4]], :])
#                          val_1  val_2
# year weekday date
# 2017 0       2017-11-27     20     38
#      4       2017-12-22     31     54
#              2017-12-29     21      8
# 2018 0       2018-01-08     48     64
#      4       2018-01-19     18     48

df_yqmw = df.set_index([df.index.year, df.index.quarter, df.index.month, df.index.weekday, df.index])
df_yqmw.index.names = ['year', 'quarter', 'month', 'weekday', 'date']
df_yqmw.sort_index(inplace=True)
print(df_yqmw)
#                                        val_1  val_2
# year quarter month weekday date
# 2017 4       11    0       2017-11-27     20     38
#                    1       2017-11-07     26     66
#                    2       2017-11-01     65     76
#                    5       2017-11-18     47     47
#              12    1       2017-12-05     65     85
#                            2017-12-12      4     29
#                    4       2017-12-22     31     54
#                            2017-12-29     21      8
# 2018 1       1     0       2018-01-08     48     64
#                    1       2018-01-23     86     70
#                    2       2018-01-03     98     76
#                    4       2018-01-19     18     48

print(df_yqmw.sum(level='month'))
#        val_1  val_2
# month
# 11       158    227
# 12       121    176
# 1        250    258

print(df_yqmw.sum(level='weekday'))
#          val_1  val_2
# weekday
# 0           68    102
# 1          181    250
# 2          163    152
# 5           47     47
# 4           70    110

print(df_yqmw.sum(level=['quarter', 'weekday']))
#                  val_1  val_2
# quarter weekday
# 4       0           20     38
#         1           95    180
#         2           65     76
#         5           47     47
#         4           52     62
# 1       0           48     64
#         1           86     70
#         2           98     76
#         4           18     48

print(df_yqmw.xs(1, level='weekday'))
#                                val_1  val_2
# year quarter month date
# 2017 4       11    2017-11-07     26     66
#              12    2017-12-05     65     85
#                    2017-12-12      4     29
# 2018 1       1     2018-01-23     86     70

print(df_yqmw.xs((1, 2017), level=('weekday', 'year')))
#                           val_1  val_2
# quarter month date
# 4       11    2017-11-07     26     66
#         12    2017-12-05     65     85
#               2017-12-12      4     29

print(df_yqmw.loc[pd.IndexSlice[2017, :, :, [0, 4]], :])
#                                        val_1  val_2
# year quarter month weekday date
# 2017 4       11    0       2017-11-27     20     38
#              12    4       2017-12-22     31     54
#                            2017-12-29     21      8