from encrypt_jar import run_java_jar

# 调用函数
plain_address = "D:\\桌面\\profile_C9Test_24458_002.txt"
public_key_address = "D:\\桌面\\links_C9Test_publickey.asc"
private_key_address = "D:\\桌面\\TTCPrivateKeys.asc"
pwd = "123456"
output_address = "D:\\桌面\\文本文档.txt"
jar_path = "D:\\downloads\\encrypt-1.0-SNAPSHOT(2).jar"

data = run_java_jar(plain_address, public_key_address, private_key_address,pwd,output_address, jar_path)
print(data)