import requests
'''
循环上传单iccid撤销部署
'''
# CA 证书文件路径
custom_ca_path = 'D:\\downloads\\lk-ca.crt'

# 客户端证书文件路径和私钥文件路径
client_cert_path = 'D:\\downloads\\client.crt'
client_key_path = 'D:\\downloads\\client.key'

# API 地址
host = 'dppoapiproxyp.linksfield.net'
endpoint = '/apiProxy/cancelQr'
api_url = f'https://{host}{endpoint}'

iccid = "24051400000000000000"

# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "iccidList": [iccid]
}

session = requests.Session()

# 使用自定义的 CA 证书
session.verify = custom_ca_path
session.cert = (client_cert_path, client_key_path)

# 发送请求
response = session.post(api_url, json=payload, verify=False)

print(f"ICCID: {iccid}, Response: {response.text}")
