from API码号部署.test.encrypt_jar import run_java_jar

# 调用函数
plain_address = "D:\\项目\\DP+\\实施部署API\\测试环境\\profile_test_1130.inp"
public_key_address = "D:\\项目\\DP+\\实施部署API\\测试环境\\links_LINKSFIELD_PM_publickey.asc"
output_address = "D:\\项目\\DP+\\实施部署API\\测试环境\\profile_test_1130.txt"
jar_path = "D:\\downloads\\encrypt-1.0-SNAPSHOT.jar"

data = run_java_jar(plain_address, public_key_address, output_address, jar_path)
print(data)