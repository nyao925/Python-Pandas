import pandas as pd
import pprint

print(pd.__version__)
# 0.23.0

print(pd.options.display.max_rows)
# 60

pd.options.display.max_rows = 100

print(pd.options.display.max_rows)
# 100

print(dir(pd.options))
# ['compute', 'display', 'html', 'io', 'mode', 'plotting']

pprint.pprint(dir(pd.options.display))
# ['chop_threshold',
#  'colheader_justify',
#  'column_space',
#  'date_dayfirst',
#  'date_yearfirst',
#  'encoding',
#  'expand_frame_repr',
#  'float_format',
#  'html',
#  'large_repr',
#  'latex',
#  'max_categories',
#  'max_columns',
#  'max_colwidth',
#  'max_info_columns',
#  'max_info_rows',
#  'max_rows',
#  'max_seq_items',
#  'memory_usage',
#  'multi_sparse',
#  'notebook_repr_html',
#  'pprint_nest_depth',
#  'precision',
#  'show_dimensions',
#  'unicode',
#  'width']

pd.describe_option()

pd.describe_option('compute')
# compute.use_bottleneck : bool
#     Use the bottleneck library to accelerate if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]
# compute.use_numexpr : bool
#     Use the numexpr library to accelerate computation if it is installed,
#     the default is True
#     Valid values: False,True
#     [default: True] [currently: True]

pd.describe_option('max_col')
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 20] [currently: 20]
# display.max_colwidth : int
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output.
#     [default: 50] [currently: 50]

pd.describe_option('max.*col')
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.
#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection.
#     [default: 20] [currently: 20]
# display.max_colwidth : int
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output.
#     [default: 50] [currently: 50]
# display.max_info_columns : int
#     max_info_columns is used in DataFrame.info method to decide if
#     per column information will be printed.
#     [default: 100] [currently: 100]


print(pd.get_option('display.max_rows'))
# 100

pd.set_option('display.max_rows', 60)

print(pd.get_option('max_r'))
# 60

pd.set_option('max_r', 100)

# pd.get_option('max')
# OptionError: 'Pattern matched multiple keys'

# pd.set_option('max', 60)
# OptionError: 'Pattern matched multiple keys'

l = ['display.max_rows', 'display.max_columns', 'display.max_colwidth']

print([pd.get_option(i) for i in l])
# [100, 20, 50]

print({i: pd.get_option(i) for i in l})
# {'display.max_rows': 100, 'display.max_columns': 20, 'display.max_colwidth': 50}

d = {'display.max_rows': 80,
     'display.max_columns': 80,
     'display.max_colwidth': 80}

[pd.set_option(k, v) for k, v in d.items()]

print({i: pd.get_option(i) for i in d.keys()})
# {'display.max_rows': 80, 'display.max_columns': 80, 'display.max_colwidth': 80}

print(pd.options.display.max_rows)
# 80

pd.reset_option('display.max_rows')

print(pd.options.display.max_rows)
# 60

print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 80
# 80

pd.reset_option('max_col')

print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 20
# 50

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100
pd.options.display.max_colwidth = 100

pd.reset_option('^display', silent=True)

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)
print(pd.options.display.max_colwidth)
# 60
# 20
# 50

pd.reset_option('all')
# html.border has been deprecated, use display.html.border instead
# (currently both are identical)
# : boolean
#     use_inf_as_null had been deprecated and will be removed in a future
#     version. Use `use_inf_as_na` instead.
# /usr/local/lib/python3.6/site-packages/pandas/core/config.py:619: FutureWarning: html.border has been deprecated, use display.html.border instead
# (currently both are identical)
#   warnings.warn(d.msg, FutureWarning)
# /usr/local/lib/python3.6/site-packages/pandas/core/config.py:619: FutureWarning:
# : boolean
#     use_inf_as_null had been deprecated and will be removed in a future
#     version. Use `use_inf_as_na` instead.
#   warnings.warn(d.msg, FutureWarning)

pd.reset_option('all', silent=True)

with pd.option_context('display.max_rows', 100):
    print(pd.options.display.max_rows)
# 100

print(pd.options.display.max_rows)
# 60

pd.options.display.max_rows = 80

with pd.option_context('display.max_rows', 100):
    print(pd.options.display.max_rows)
# 100

print(pd.options.display.max_rows)
# 80


with pd.option_context('display.max_rows', 100, 'display.max_columns', 100):
    print(pd.options.display.max_rows)
    print(pd.options.display.max_columns)
# 100
# 100

print(pd.options.display.max_rows)
print(pd.options.display.max_columns)
# 80
# 20

pd.option_context('display.max_rows', 100)

print(pd.options.display.max_rows)
# 80

