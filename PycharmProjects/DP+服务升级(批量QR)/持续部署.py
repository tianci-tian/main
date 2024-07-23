import requests
import subprocess
'''
准备数据
'''
import openpyxl

# 生产 5w 数据,存储 txt
def ModifyFileContent(file_path, num_iterations):
    iccidList = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    line_12 = lines[12]
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

    # 修改完后删除第11、12行
    #最后面插入12行数据
    del lines[11:13]
    lines.extend(line_12)

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

'''
加密
'''
def run_java_jar(plain_address, public_key_address, Private_key_address,passwords,output_address, jar_path):
    # 构建命令
    command = ["C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath\\java.exe", "-jar", jar_path]

    # 启动子进程并打开标准输入流
    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True) as process:
        # 向标准输入流传递地址信息
        input_data = f"{plain_address}\n{public_key_address}\n{Private_key_address}\n{passwords}\n{output_address}\n"
        output, error = process.communicate(input=input_data)
    with open(output_address, "r", encoding='utf-8') as f:
        data = f.read()
        return data

'''
部署
'''
def UpProfile(data):
    # 指定 CA 证书文件路径
    custom_ca_path = 'D:\\downloads\\lk-ca.crt'

    # 指定客户端证书文件路径和私钥文件路径
    client_cert_path = 'D:\\downloads\\client(1).crt'
    client_key_path = 'D:\\downloads\\client(1).key'
    # 定义 API 地址
    host = 'dppoapiproxyt.linksfield.net'
    port = '444'
    endpoint = '/apiProxy/operPgpFile'
    api_url = f'https://{host}:{port}{endpoint}'
    pgp_file_content = data
    # 定义请求参数
    payload = {
        "sequenceId": "123456789",
        "name": "LINKSFIELD_PM",
        "profileTypeName": "profile_test_1130",
        "pgpfile": str(pgp_file_content)
    }
    # 创建一个 Session 对象
    session = requests.Session()

    # 使用自定义的 CA 证书
    session.verify = custom_ca_path

    session.cert = (client_cert_path, client_key_path)

    response = session.post(api_url, json=payload ,verify=False)

    print(response.text)






ModifyFileContent('D:\\桌面\\profile_test_1130.inp', 10000)
# 调用函数
plain_address = "D:\\桌面\\profile_test_1130.inp"
public_key_address = "D:\\项目\\DP+\\实施部署API\\测试环境\\新建文件夹\\links_LINKSFIELD_PM_publickey.asc"
private_key_address = "D:\\桌面\\TTCPrivateKeys.asc"
pwd = "123456"
output_address = "D:\\桌面\\1130.pgp"
jar_path = "D:\\downloads\\encrypt-1.0-SNAPSHOT(2).jar"

data = run_java_jar(plain_address, public_key_address, private_key_address,pwd,output_address, jar_path)
# print(data)
UpProfile(data)
