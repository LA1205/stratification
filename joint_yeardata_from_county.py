import pandas as pd
import os

# 读取Excel文件
file_path = r'D:\BaiduSyncdisk\Work_Space\KB\Projetcs\hotan\和田项目已筛选地块面积统计表.xlsx'
xls = pd.ExcelFile(file_path)

# 获取文件所在目录
file_dir = os.path.dirname(file_path)

# 创建一个字典来存储相同后缀的工作表数据
sheets_dict = {}

# 遍历所有工作表
for sheet_name in xls.sheet_names:
    suffix = sheet_name[-4:]
    if suffix not in sheets_dict:
        sheets_dict[suffix] = []
    df = pd.read_excel(xls, sheet_name=sheet_name)
    sheets_dict[suffix].append(df)

# 创建一个新的Excel文件来保存汇总数据
output_file_path_temp = os.path.join(file_dir, 'summarized_workbook.xlsx')
with pd.ExcelWriter(output_file_path_temp) as writer:
    for suffix, dfs in sheets_dict.items():
        # 将所有相同后缀的工作表数据合并
        combined_df = pd.concat(dfs, ignore_index=True)
        # 将合并后的数据写入新的工作表
        combined_df.to_excel(writer, sheet_name=suffix, index=False)

print("数据汇总完成！")

import pandas as pd

# 读取Excel文件
excel_file = pd.ExcelFile(output_file_path_temp)

# 创建一个空的字典来存储处理后的数据
processed_data = {}

# 遍历所有工作表
for sheet_name in excel_file.sheet_names:
    # 读取工作表
    df = pd.read_excel(output_file_path_temp, sheet_name=sheet_name)
    
    # 合并重复的树种行，并对面积进行求和
    df_grouped = df.groupby('种', as_index=False).agg({'面积（亩）': 'sum'})
    
    # 将处理后的数据存储到字典中
    processed_data[sheet_name] = df_grouped

# 将处理后的数据写回到一个新的Excel文件
output_file_path =  os.path.join(file_dir, '逐年造林树种面积统计.xlsx')
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, df in processed_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("数据合并完成！")

