import pandas as pd
from tkinter import filedialog


# 读取CSV文件并转换成EXECL文件
def read_csv_write_xlsx(input_file, output_file):
    # 使用pandas读取CSV文件
    data_frame = pd.read_csv(input_file)
    # 设置"Plugin ID"列的值为从1开始的整数
    data_frame["Plugin ID"] = range(1, len(data_frame) + 1)
    # 将数据帧保存为XLSX文件
    data_frame.to_excel(output_file, index=False)


# 读取CSV文件并输出漏洞XLSX文件
def read_csv_write_vuln(input_file, output_file):
    # 从指定的CSV文件中读取数据，创建一个DataFrame对象
    df = pd.read_csv(input_file)
    # 删除数据框中‘Risk’列的缺失值
    df = df.dropna(subset=['Risk'])
    # 设置"Plugin ID"列的值为从1开始的整数
    df["Plugin ID"] = range(1, len(df) + 1)
    # 将DataFrame数据导出到Excel文件
    df.to_excel(output_file, index=False)


# 读取CSV文件并输出高危端口TXT文件
def filter_and_log_unique_hosts_per_port(input_file, output_file_txt):
    # 读取csv文件至DataFrame
    df = pd.read_csv(input_file)
    # 确保Port列为字符串类型，以便进行匹配
    df['Port'] = df['Port'].astype(str)
    # 筛选Port列中值为22、3389、445、135或139的行
    filtered_df = df[df['Port'].isin(['22', '3389', '445', '135', '139'])]
    # 对于Port列值相同的行，保留每种Port-Host组合的第一次出现
    # 首先按Port列排序，然后按Host列分组，选取每个分组的第一条记录
    final_df = filtered_df.sort_values(['Port', 'Host']).drop_duplicates(subset=['Port', 'Host'], keep='first')
    # 保存筛选和去重后的数据到Excel
    # 准备写入TXT的内容
    with open(output_file_txt, 'w') as txt_file:
        for port, group in final_df.groupby('Port'):
            host_list = group['Host'].tolist()
            hosts_str = ', '.join(host_list)
            txt_file.write(f"{port}:{hosts_str}\n")


# 读取CSV文件并整理出端口文件
def read_write_csv_prot(input_file, output_file):
    # 读取CSV文件
    df = pd.read_csv(input_file)
    # 使用where函数和lambda表达式更新Name列的值
    # 将Name列中值为'Ping the remote host'的行设定为'Down'
    df.loc[df['Name'] == 'Ping the remote host', 'Name'] = 'Down'
    # 使用groupby按Host列分组，收集Port列的去重值，并保留第一个Name列的值
    result = df.groupby('Host').agg({'Port': lambda x: list(set(x)), 'Name': 'first'}).reset_index()
    # 将Port列的list转换为字符串，方便保存到Excel
    result['Port'] = result['Port'].apply(lambda x: ', '.join(map(str, x)))
    # 保存结果到Excel文件
    result.to_excel(output_file, index=False)


# 读取漏洞文件并统计漏洞数量
def read_csv_count_vuln(input_file, output_file):
    # 步骤1: 读取Excel文件
    df = pd.read_excel(input_file)
    # 步骤2: 统计Host和N列值组合的出现次数
    # 这里我们不预先筛选，直接对所有行进行分组计数
    combination_counts = df.groupby(['Risk', 'Name']).size().reset_index(name='Count')
    # 步骤3: 保存统计结果到新的Excel文件
    combination_counts.to_excel(output_file, index=False)


def read_csv_write_vuln_text(input_file):
    # 翻译名称和解决方案
    df = pd.read_excel(input_file + '_漏洞文件.xlsx')
    for index, row in df.iterrows():
        with open("Name.txt", "a") as f:
            f.write(str(df.loc[index, 'Name']).replace("\n", "").replace("\r", "") + "\n")

    for index, row in df.iterrows():
        with open("Solution.txt", "a") as f:
            f.write(str(df.loc[index, 'Solution']).replace("\n", "").replace("\r", "") + "\n")


if __name__ == '__main__':
    # 获取文件路径
    input_file_path = filedialog.askopenfilename()
    # 获取保存文件名
    filename = filedialog.asksaveasfilename()
    # 示例用法
    read_csv_write_xlsx(input_file_path, filename + '_源文件.xlsx')
    read_csv_write_vuln(input_file_path, filename + '_漏洞文件.xlsx')
    read_write_csv_prot(input_file_path, filename + '_端口文件.xlsx')
    filter_and_log_unique_hosts_per_port(input_file_path, filename + '_高危端口文件.txt')
    read_csv_count_vuln(filename + '_漏洞文件.xlsx', filename + '_漏洞统计.xlsx')
    read_csv_write_vuln_text(filename)
