import subprocess

def run_java_jar(plain_address, public_key_address, output_address, jar_path):
    # 构建命令
    command = ["C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath\\java.exe", "-jar", jar_path]

    # 启动子进程并打开标准输入流
    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        # 向标准输入流传递地址信息
        input_data = f"{plain_address}\n{public_key_address}\n{output_address}\n"
        output, error = process.communicate(input=input_data)
    with open(output_address, "r", encoding='utf-8') as f:  # 打开文本
        data = f.read()  # 读取文本
        return data

