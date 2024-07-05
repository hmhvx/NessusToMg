import pandas as pd

if __name__ == '__main__':
    # 步骤1: 读取Excel文件
    df = pd.read_excel('tongji.xlsx')

    # 步骤2: 统计Host和N列值组合的出现次数
    # 这里我们不预先筛选，直接对所有行进行分组计数
    combination_counts = df.groupby(['Host', 'N']).size().reset_index(name='Count')

    # 步骤3: 保存统计结果到新的Excel文件
    combination_counts.to_excel('host_n_combination_counts.xlsx', index=False)

    print("每对Host和N值组合的出现次数已统计完成，并保存至host_n_combination_counts.xlsx")

