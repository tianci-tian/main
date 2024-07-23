import paramiko

# 创建一个 SFTP 连接;服务器指定路径新建一个空文件，将内容复制到新文件里面。
def upload_file(local_path, remote_path, hostname, username, password):
    try:
        # 创建 SSH 客户端对象
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接到服务器
        ssh.connect(hostname, username=username, password=password)

        # 创建 SFTP 客户端对象
        sftp = ssh.open_sftp()

        sftp.put(local_path, remote_path)
        print(f"File uploaded successfully to {remote_path}")

        # 关闭 SFTP 和 SSH 连接
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# 调用函数上传文件
if __name__ == "__main__":

    upload_file('D:\\DPprofile\\output.pgp', '/upload/LINKSFIELD_PM/pgpfile/output.pgp', '39.99.148.148', 'mno_data', 'Links@2023')
