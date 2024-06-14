import subprocess
'''
使用python调用pgp加密jar包
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
plain_address = "D:\\项目\\DP+\\实施部署API\\Pre环境\\profile_apiTest_45407_002.inp"
public_key_address = "D:\\项目\\DP+\\实施部署API\\正式环境\\links_LINKSFIELD_PM_publickey.asc"
Private_key_address = "D:\桌面\TTCPrivateKeys.asc"
passwords = "123456"
output_address = "D:\\项目\\DP+\\实施部署API\\Pre环境\\profile_apiTest_45407_002.txt"
jar_path = "D:\\downloads\\encrypt-1.0-SNAPSHOT(2).jar"
run = run_java_jar(plain_address, public_key_address, Private_key_address,passwords,output_address, jar_path)
print(run)



'''
