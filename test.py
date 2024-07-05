import pandas as pd


# 转换CSV文件为XLSX文件
def csv_to_xlsx(csv_file_path, xlsx_file_path):
    # 使用pandas读取CSV文件
    data_frame = pd.read_csv(csv_file_path)

    # 检查"Plugin ID"列是否存在，如果存在则重新编号，否则提醒用户
    if "Plugin ID" in data_frame.columns:
        # 重置"Plugin ID"列，从1开始计数
        data_frame["Plugin ID"] = range(1, len(data_frame) + 1)
    else:
        print("警告: 'Plugin ID' 列未在CSV文件中找到。")

    # 将数据帧保存为XLSX文件
    data_frame.to_excel(xlsx_file_path, index=False)


def process_and_output_csv(input_file_path, output_file_path):
    # 读取CSV文件
    df = pd.read_csv(input_file_path)

    # 去除"Risk"列值为空的行
    df = df.dropna(subset=['Risk'])

    # 设置指定列为字符串类型
    cols_to_str = ['Risk', 'Host', 'Protocol', 'Port', 'Name']
    df[cols_to_str] = df[cols_to_str].astype(str)

    # 保留每种Risk-Host-Protocol-Port-Name组合的第一次出现的行
    df = df.drop_duplicates(subset=cols_to_str, keep='first')
    df['Plugin ID'] = range(1, len(df) + 1)
    # 输出到XLSX文件
    df.to_excel(output_file_path, index=False)

def process_csv(input_file_path, output_file_path):
    """
    读取CSV文件，设置指定列为字符串类型，保留Host-Port组合第一次出现的行，
    如果"Name"列值为"Ping the remote host"，则所在行的"Plugin Output"设为"Down"，否则设为"Up"，
    最后输出到新的CSV文件。

    参数:
    - input_file_path (str): 输入CSV文件的路径。
    - output_file_path (str): 输出CSV文件的路径。
    """
    # 读取CSV文件
    df = pd.read_csv(input_file_path)

    # 设置指定列为字符串类型
    cols_to_str = ['Host', 'Protocol', 'Port', 'Name', 'Plugin Output']
    df[cols_to_str] = df[cols_to_str].astype(str)

    # 保留Host-Port组合第一次出现的行
    df = df.drop_duplicates(subset=['Host', 'Port'], keep='first')

    # 根据"Name"列的值设定"Plugin Output"列
    df.loc[df['Name'] == 'Ping the remote host', 'Plugin Output'] = 'Down'
    df.loc[df['Name'] != 'Ping the remote host', 'Plugin Output'] = 'Up'

    # 输出到新的CSV文件
    df.to_excel(output_file_path, index=False)



if __name__ == '__main__':
    # 示例用法
    input_file_path = '儿科DMZ同侧.csv'
    output_file_path = 'output.xlsx'
    process_csv(input_file_path, output_file_path)

