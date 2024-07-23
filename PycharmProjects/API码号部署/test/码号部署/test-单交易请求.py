import requests

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
pgp_file_content = '''


'''
# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "name": "LINKSFIELD_PM",
    "profileTypeName": "profile_test_1130",
    "pgpfile": pgp_file_content
}

# 创建一个 Session 对象
session = requests.Session()

# 使用自定义的 CA 证书
session.verify = custom_ca_path

session.cert = (client_cert_path, client_key_path)

response = session.post(api_url, json=payload ,verify=False)

print(response.text)


