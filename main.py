import pandas as pd
from tkinter import filedialog


# 读取CSV文件并转换成EXECL文件
def read_write_csv_xlsx(input_file, output_file):
    df = pd.read_csv(input_file)
    num = 1
    for index, row in df.iterrows():
        df.loc[index, 'Plugin ID'] = num
        num += 1
    df.to_excel(output_file, index=False)


if __name__ == '__main__':
    # 获取文件路径
    input_file_path = filedialog.askopenfilename()
    # 获取保存文件名
    filename = filedialog.asksaveasfilename()
    # 示例用法
    # read_write_csv_xlsx(input_file_path, filename + '_源文件.xlsx')
