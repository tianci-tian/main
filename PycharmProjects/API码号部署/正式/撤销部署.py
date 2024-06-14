import requests
'''
循环上传单iccid撤销部署
'''
# CA 证书文件路径
custom_ca_path = 'D:\\downloads\\lk-ca.crt'

# 客户端证书文件路径和私钥文件路径
client_cert_path = 'D:\\downloads\\linksfield_pm.crt'
client_key_path = 'D:\\downloads\\private.key'
Passphrase = '123456'
# API 地址
host = 'dppoapiproxy.linksfield.net'
endpoint = '/apiProxy/cancelQr'
api_url = f'https://{host}{endpoint}'

iccid = "89011529000000001304"

# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "iccidList": [iccid]
}

session = requests.Session()

# 使用自定义的 CA 证书
session.verify = custom_ca_path
session.cert = (client_cert_path, client_key_path,Passphrase)

# 发送请求
response = session.post(api_url, json=payload, verify=False )

print(f"ICCID: {iccid}, Response: {response.text}")
