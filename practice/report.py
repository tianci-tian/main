import openpyxl
import matplotlib.pyplot as plt

def read_test_results(file_path, column_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    column_index = None
    test_results = []

    # 查找指定列的索引
    for idx, cell in enumerate(sheet[1], start=1):
        if cell.value == column_name:
            column_index = idx
            break

    if column_index is None:
        raise ValueError(f"未找到列: {column_name}")

    # 获取指定列的所有值
    for row in sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
        test_results.append(row[0])

    return test_results

def calculate_success_rate(test_results):
    total = len(test_results)
    success = test_results.count('成功')  # 假设成功的结果标识为“成功”
    fail = total - success
    return success, fail

def plot_pie_chart(success, fail):
    labels = '成功', '失败'
    sizes = [success, fail]
    colors = ['#4CAF50', '#FF5733']
    explode = (0.1, 0)  # 突出显示成功的部分

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    plt.title('测试结果成功占比')
    plt.axis('equal')  # 保证饼图是圆的
    plt.show()

# 文件路径
excel_file_path = 'D:\\项目\\FMS\\FMS测试报告.xlsx'
html_report_path = 'D:\\项目\\FMS\\FMS测试报告.html'

# 读取测试结果
test_results = read_test_results(excel_file_path, html_report_path)

# 计算成功率
success, fail = calculate_success_rate(test_results)

# 生成并显示饼状图
plot_pie_chart(success, fail)
