import pandas as pd
import os
import sys


def check_duplicates_in_id_column(file_path):
    # 读取Excel文件，不设置表头
    df = pd.read_excel(file_path, header=None)
    
    # 查找第二行（索引为1）中值为'id'的列
    id_column = None
    for col in df.columns:
        if str(df.at[1, col]).strip().lower() == 'id':
            id_column = col
            break
    
    if id_column is None:
        return "错误：未找到'id'列"
    
    # 提取该列从第三行开始的数据
    data = df.loc[2:, id_column]
    
    # 转换为数值类型（非数值会被转为NaN）
    numeric_data = pd.to_numeric(data, errors='coerce')
    
    # 过滤掉NaN值
    valid_data = numeric_data.dropna()
    
    if valid_data.empty:
        return "列中无有效数值"
    
    # 检查重复值
    duplicates = valid_data[valid_data.duplicated(keep=False)]
    
    if duplicates.empty:
        return "无重复值"
    else:
        # 统计重复值出现次数
        counts = duplicates.value_counts().reset_index()
        counts.columns = ['重复值', '出现次数']
        return counts
def find_first_xlsx():
    files = [f for f in os.listdir('.') if f.endswith('.xlsx')]
    if not files:
        print("错误：当前目录下未找到xlsx文件")
        sys.exit(1)
    return files[0]

if __name__ == "__main__":
    # 优先使用命令行参数，否则使用默认文件
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = find_first_xlsx()
        print(f"检测到文件：{file_path}")
    
    # 执行检查
    result = check_duplicates_in_id_column(file_path)
    
    # 输出结果
    if isinstance(result, str):
        print(result)
    else:
        print("发现重复值：")
        print(result.to_string(index=False))

input(" ")