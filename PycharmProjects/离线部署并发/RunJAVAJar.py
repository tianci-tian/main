import subprocess

def RunJAVAJar(jar_path):
    # 构建命令
    command = ["C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath\\java.exe", "-jar", jar_path]

    # 启动子进程
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        output, error = process.communicate()
    return output


if __name__ == '__main__':
    RunJAVAJar('D:\\DPprofile\\encrypt-1.0-SNAPSHOT.jar')