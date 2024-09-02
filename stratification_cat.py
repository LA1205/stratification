import pandas as pd

# 读取CSV文件，指定编码格式为ANSI
file_path = r'D:\BaiduSyncdisk\Work_Space\KB\Projetcs\stratification.csv'
df = pd.read_csv(file_path, encoding='ANSI')

# 创建一个新的列'stra_group'并初始化为None
df['stra_group'] = None

# 使用groupby对'A', 'B', 'C'列进行碳层分组，并为每组分配唯一的stra_group值
sid = 1
for _, group in df.groupby(['植苗年份', '定植模式', '树种', '类型', '苗木规格', '混交比例', '种植密度']):
    df.loc[group.index, 'stra_group'] = sid
    sid += 1

# 创建一个新的列'stra_id',用于存储将'植苗年份'和'stra_group'连接后的值
df['stra_id'] = df['植苗年份'] + '_' + df['stra_group']

# 保存处理后的CSV文件
newfile_path = file_path[:-4] + '_grouped' + file_path[-4:]
df.to_csv(newfile_path, index=False, encoding='ANSI')

print("处理完成, 结果已保存到: " + newfile_path)