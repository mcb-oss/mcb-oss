import pandas as pd
import sys
import os

def find_max_value_in_id_column(file_path):
    # 读取Excel文件，不设置表头，所有行作为数据
    df = pd.read_excel(file_path, header=None)
    
    # 查找第二行（索引为1）中值为'id'的列索引
    id_column = None
    for col in df.columns:
        if df.at[1, col] == 'id':
            id_column = col
            break
    
    if id_column is None:
        return "未找到'id'列"
    
    # 提取该列从第三行开始的数据并转换为数值
    data = df.loc[2:, id_column]
    numeric_data = pd.to_numeric(data, errors='coerce')
    
    # 计算最大值（跳过NaN值）
    max_value = numeric_data.max()
    
    return max_value if not pd.isna(max_value) else "列中无有效数值"

if __name__ == "__main__":
    # 自动检测当前目录下唯一的 .xlsx 文件
    default_file = None
    current_dir_files = os.listdir('.')
    excel_files = [f for f in current_dir_files if f.endswith('.xlsx')]
    
    if len(excel_files) == 1:
        default_file = excel_files[0]
    elif len(excel_files) > 1:
        print("错误：当前目录下存在多个 .xlsx 文件，请通过命令行指定具体文件路径。")
        sys.exit(1)
    else:
        print("错误：当前目录下未找到 .xlsx 文件。")
        sys.exit(1)
    
    # 优先使用命令行参数，否则使用自动检测的默认文件
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = default_file
    
    # 调用函数并输出结果
    max_value = find_max_value_in_id_column(file_path)
    print(f"最大值是: {max_value}")
    # 在你的 Python 脚本最后添加一行
input(" ")