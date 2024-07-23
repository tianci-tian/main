import pandas as pd
import MySQL_practice.connect
data = pd.read_excel('D:\\桌面\\10w工作表.xlsx')
excel_data = data['iccid']  # 假设列名为 'A1'
print(excel_data[0:5])


