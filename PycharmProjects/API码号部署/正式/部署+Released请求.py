import requests
import time
'''
单iccid码号部署
变量参数pgpfile在接口请求外部定义
'''
# CA 证书文件路径
custom_ca_path = 'D:\\downloads\\lk-ca.crt'

# 客户端证书文件路径和私钥文件路径
client_cert_path = 'D:\\downloads\\linksfield_pm.crt'
client_key_path = 'D:\\downloads\\private.key'
Passphrase = '123456'
# API 地址、参数
host = 'dppoapiproxy.linksfield.net'
endpoint = '/apiProxy/deployAndProduceQr'
api_url = f'https://{host}{endpoint}'
pgp_file_content = '''
-----BEGIN PGP MESSAGE-----
Version: BCPG v1.62

hIwDHbUIJ/QWl3YBA/9yVaCP27ySpvi3WE+jBMTw0y5btGVLqPzvYw8jFhRUOSWk
dVLTAvqwGdzm7KLQud55dTKGwI7zR7j/7/+OcNHqd47t6VWJMDEQgN0u3XYAk7gy
idgmHFJuzfPpHopHrh0eKkx+ZoSIEidsGqw9hG04cFqQqqFxWH5yJd1cY8F4K9LB
NwEHfOB1let5tWJaulvlOOWIDRne6L8rYMl1mOh/mplkwRX73z/PuWhXyKq1t4an
pK669irNauYQ5KO1b8O+r107+qlGmm4UW3AYGEyHJTN34KFU5fDkA7SK/YybOcyB
8Af8LMc4/ngUxo0+rPmsVpVe2ZQtTVKUPW5tRDVpxaRLQztPthxRuMtc+mKJa+f6
uU7BYCaJ4Z63efivRQt7ZISXuU8Cj+oWTpa1WLVaMdZd0zMtRvvyn3KCK8S/Re/M
kZ6WkgaP4bCVsQ3mJX8ioGLM8PPpQZdGXmDHKgbbf8mdOMl8+YKHS18+tHm8jP/K
8Tlb7VBdwhkeL2Jls63vN1J6aodTKrMTyEeWzTn9M2B29sWcnf2k7JY+4HcaspDq
okmve5C/9dhuJcvdeRcsT6J+OzkFIcy2XSmFSFVsS0CdvWEZ3Zawfy73KGqvfqzX
AzlBFPAyYmv65oOmf2bqL7sfTsu0l0uYglMi8bpK9xMd2hFgiPO6TSeUyPoJZQTw
u0NQAcl61twGZW4zClQMfBB6S53FT1GNB5gI2zZvZNoE1ddYRzqKYv6u6ea9qqDD
W2oLpnjT1NYR/pPtogZh34CgZMe63yV/DzJEpm191pMosEFeJ1HMBQjTPqh1FHsY
R3EhMlgCF+7XevNGyabWWD5APnrrKXps
=zEF9
-----END PGP MESSAGE-----
'''
# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "name": "LINKSFIELD_PM",
    "profileTypeName": "profile_LINKSFIELD_PM_45407_003",
    "pgpfile" : pgp_file_content
}

session = requests.Session()

# 使用自定义的 CA 证书
session.verify = custom_ca_path

session.cert = (client_cert_path, client_key_path,Passphrase)
#发出API请求之前获取时间戳
request_time = time.time()
response = session.post(api_url, json=payload ,verify=False)
#计算API请求的持续时间
duration = time.time() - request_time
print(f"API Response: {response.text}")
print(f"API Request Duration: {duration} seconds")


