import openpyxl

# 生产 5w 数据,存储 txt
def ModifyFileContent(file_path, num_iterations):
    iccidList = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_index = 0
    while current_index < num_iterations:
        if len(lines) >= 11:
            line_to_modify = lines[11].strip()
            elements = line_to_modify.split()
            if elements:
                first_element = int(elements[0])
                first_element += 1
                elements[0] = str(first_element)
                iccidList.append(elements[0])
                lines[11] =' '.join(elements) + '\n'
                lines.append(lines[11])  # 将修改后的行添加到末尾
            current_index += 1
    with open(file_path, 'w') as file:
        file.writelines(lines)
    WriteExcel(iccidList)

# iccid 写入 excel
def WriteExcel(iccidList):
    # 创建一个新的 Excel 工作簿
    workbook = openpyxl.Workbook()
    # 获取默认的工作表
    sheet = workbook.active
    sheet['A1'] = 'iccid'  # 在 A1 位置添加固定值
    for iccid in iccidList:
        sheet.append([iccid])  # 以列表形式添加数据，实现竖着写入

    # 保存工作簿
    workbook.save('D:\\桌面\\工作表.xlsx')

ModifyFileContent('D:\\桌面\\profile_apiTest_45407_002.txt', 30000)