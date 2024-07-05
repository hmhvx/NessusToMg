import pandas as pd
import openpyxl

if __name__ == '__main__':
    df = pd.read_excel("xxk_漏洞文件.xlsx")
    for index, row in df.iterrows():
        with open("Name.txt", "a") as f:
            f.write(str(df.loc[index, 'Name']).replace("\n", "").replace("\r", "") + "\n")

    for index, row in df.iterrows():
        with open("Solution.txt", "a") as f:
            f.write(str(df.loc[index, 'Solution']).replace("\n", "").replace("\r", "") + "\n")
