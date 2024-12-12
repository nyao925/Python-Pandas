# Python-Pandas

我叫饺子大人，当然这不是我的真名，只是因为我喜欢吃饺子而已。学生时不懂python，不懂Machine Learning，更不懂人工智能。所以，工作后开始了我漫长的自学之路。我很欣赏网上那些默默奉献的人们, 分享自己所学的东西给了我很大的帮助。所以我决定我也要像那些奉献的人们一样, 将我的所学奉献给大家~

我将假设你已经有了一定的python基础，而是在日常的使用中为不知道某个函数的功能而发愁的小伙伴。在此我先总结分享出Numpy和Pandas的一些函数的使用方法。再总结个人的一些炼丹时所遭遇到坑，如scikit-learn,Tensorflow,mxnet等等。希望能够帮助到大家。

肯定有错，当然不全，但按你胃(Anyway)，成长的路上就是要不断的犯错。 

Numpy→Pandas→Machine Learning 这是我的炼丹之道。。。

01_Pandas.DataFrame的行名和列名的修改\
02_Pandas.concat连接DataFrame,Series\
03_Pandas读取csv/tsv文件（read_csv，read_table）\
04_Pandas获取和修改任意位置的值（at,iat,loc,iloc）\
05_Pandas删除，替换并提取其中的缺失值NaN \
06_Pandas中map(),applymap(),apply()函数的使用方法 \
07_pandas.DataFrame的for循环处理（迭代）\
08_Pandas提取含有指定字符串的行（完全匹配，部分匹配）\
09_Pandas从多个条件（AND，OR，NOT）中提取行 \
10_Pandas使用分隔符或正则表达式将字符串拆分为多列 \
11_Pandas.DataFrame中组合多个列的字符串来创建新列 \
12_Pandas.DataFrame删除指定行和列（drop） \
13_Pandas字符串的替换和空格处删除等方法 \
14_Pandas.DataFrame行和列的转置\
15_Pandas计算元素的数量和频率（出现的次数）\
16_Pandas.DataFrame计算统计信息并按GroupBy分组\
17_pandas.DataFrame，Series排序（sort_values，sort_index）\
18_Pandas.DataFrame，取得Series的头和尾（head和tail）\
19_Pandas随机抽取行和列的样本（sample）\
20_Pandas.DataFrame中Series行的随机洗牌\
21_Pandas.DataFrame,重置Series的索引index(reset_index)\
22_Pandas.DataFrame,重置列的行名(set_index）\
23_Pandas.DataFrame,Series中提取・删除重复行\
24_Pandas.DataFrame,Series元素值的替换（replace）\
25_Pandas从MultiIndex中选择并提取任何行和列\
26_Pandas.DataFrame时间序列数据的处理\
27_Pandas按星期，月份，季度和年份的天计算时间序列数据的总计和平均值\
28_Pandas通过index选择并获取行和列\
29_pandas.DataFrame中提取（选择）特定类型dtype的列\
30_Pandas.DataFrame提取（选择）指定行名和列名的行和列\
31_Pandas.DataFrame，Series和NumPy数组ndarray相互转换\
32_Pandas『Python Data Science Handbook』（英文的免费在线版本）\
33_Pandas.DataFrame，Series和Python标准列表的相互转换\
34_Pandas对CSV文件内容的导出和添加（to_csv）\
35_Pandas计算满足特定条件的元素的数量\
36_Pandas获取行数，列数和元素总数（大小）\
37_Pandas中Multiindex的指定，添加，取消，排序，级别的更改\
38_Pandas中Multiindex的计算每层的统计数据和样本大小\
39_Pandas.Serise用map方法替换列元素\
40_Pandas中crosstab进行交叉制表（计算每个类别的出现次数和频率）\
41_Pandas使用数据透视表计算每个类别的统计信息\
42_Pandas字符串中提取正则表达式来生成新列\
43_Pandas版本的检查（pd.show_versions）\
44_Pandas将分类变量转换为虚拟变量(get_dummies) \
45_Pandas.DataFrame计算每列之间的相关系数并用热图可视化 \
46_Pandas,Python,Seaborn热图的生成 \
47_Pandas使用cut和qcut函数进行分箱处理 \
48_Python列表和数组与numpy.ndarray的区别和使用方法 \
49_Pandas.DataFrame添加列和行（分配、追加等）\
50_Pandas读取 Excel 文件 (xlsx, xls) \
51_Pandas (to_excel) 编写 Excel 文件 (xlsx, xls) \
52_Pandas处理日期和时间列（字符串转换、日期提取等） \
53_Pandas中的条件替换值（where, mask） \
54_Pandas将DataFrame、Series转换为字典 (to_dict) \
55_Pandas.DataFrame 转换为 JSON 字符串/文件并保存 (to_json) \
56_Pandas读取 JSON 字符串/文件 (read_json) \
57_Pandas中的json_normalize将字典列表转换为DataFrame \
58_Pandas中mode获取pandas的每一行和列  \
59_Pandas中使用describe获取每列的汇总统计信息（平均值、标准差等） \
60_Pandas中是否包含判断缺失值NaN并统计个数 \
61_Pandas中将列表存储和处理为 pandas 中的元素 \
62_Pandas有条件地提取 pandas.DataFrame 的行 \
63_Pandas中数字的四舍五入 \
64_Pandas进行字符串和数字的相互转换和格式化 \
65_Pandas显示设置（小数位数、有效数字、最大行/列数等） \
66_Pandas如何检查和更改选项设置 \
66_Pandas将切片应用于字符串，以提取任意位置和长度的部分 \
68_Pandas.Series 索引和值的交换 \
69_Pandas.DataFrame获取行号和列号 \
70_Pandas中获取最大最小值的行名和列名 \
71_Pandas.DataFrame排名 \
72_Pandas.DataFrame保存并读取带pickle的系列（to_pickle、read_pickle） \
73_Pandas获取分位数/百分位数 \
74_Pandas median获取中位数 \
75_pandas.DataFrame 中查看和复制 \