import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

list_2d = [[0, 1, 2], [3, 4, 5]]

sns.heatmap(list_2d)

plt.figure()
sns.heatmap(list_2d)
plt.savefig('./data/46/seaborn_heatmap_list.png')
plt.close('all')

arr_2d = np.arange(-8, 8).reshape((4, 4))
print(arr_2d)
# [[-8 -7 -6 -5]
#  [-4 -3 -2 -1]
#  [ 0  1  2  3]
#  [ 4  5  6  7]]

plt.figure()
sns.heatmap(arr_2d)
plt.savefig('./data/46/seaborn_heatmap_ndarray.png')

df = pd.DataFrame(data=arr_2d, index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
print(df)
#    A  B  C  D
# a -8 -7 -6 -5
# b -4 -3 -2 -1
# c  0  1  2  3
# d  4  5  6  7

plt.figure()
sns.heatmap(df)
plt.savefig('./data/46/seaborn_heatmap_dataframe.png')

print(type(sns.heatmap(list_2d)))
# <class 'matplotlib.axes._subplots.AxesSubplot'>

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
sns.heatmap(list_2d, ax=ax)
fig.savefig('./data/46/seaborn_heatmap_list.png')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))
sns.heatmap(list_2d, ax=axes[0, 0])
sns.heatmap(arr_2d, ax=axes[1, 2])
fig.savefig('./data/46/seaborn_heatmap_list_sub.png')

sns.heatmap(df, annot=True)

sns.heatmap(df, cbar=False)

sns.heatmap(df, square=True)

sns.heatmap(df, vmax=10, vmin=-10, center=0)

sns.heatmap(df, cmap='hot')

sns.heatmap(df, cmap='Blues')

sns.heatmap(df, cmap='Blues_r')

current_figsize = mpl.rcParams['figure.figsize']
print(current_figsize)
# [6.0, 4.0]

plt.figure(figsize=(9, 6))
sns.heatmap(df, square=True)
plt.savefig('./data/46/seaborn_heatmap_big.png')

current_dpi = mpl.rcParams['figure.dpi']
print(current_dpi)
# 72.0

plt.figure()
sns.heatmap(df, square=True)
plt.savefig('./data/46/seaborn_heatmap_big_2.png', dpi=current_dpi * 1.5)