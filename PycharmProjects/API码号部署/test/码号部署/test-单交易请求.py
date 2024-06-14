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
-----BEGIN PGP MESSAGE-----
Version: BCPG v1.62

hIwDig2xOEC2KCUBA/9QhkfVzNfPx4UFkphHlsQqLlLBr957QJzo1drRdf4oV2fu
UbCVqbG5LEu0jPDFlZMJKXdsTZRUvA8bTpU8pgs8ejXUL3naWGHtdjg4ktF2oZ+e
0qPJzzEgSVkBJ5K7fFjGp588KqlsOKCg1Yuo9LZ0H+rClWpg9CmdrBFPybZWVNLB
IQEkDo332WmyKg1cCzRbC5efD3hztsLU8iy9jDqYXblcG5wTE0iCsWan/Xhk+tqI
9lcwvdCIdKgOJ2Sn7wjdZLpoRXW1uYeosFV1StPC3N2daQ4pMdQNDH1cF6KXZley
J6lqgpO/mmFXnafIYYNH2ekMc2XPGhmW2YVRVKeA/f7S8R8SM9yAE8EF5X5WYUx3
kfUzAq5jDzlYfMGdl6FRsVC0ZEcF8PKqVu7bMkDOwdtUdmKCpmEz0ygqU149QkOX
1HQG5UAwabjmopLT4avvCIHI6JApb0DXsPicVjogqd8N0NLIU4hcqCl8fGF4Amtw
7JUyqTtwvv+KqRlJYJYIaO0B9hDczUISyXZNeZkYO7fs9EDCAIujhus+jtecTK1p
qh9FrTAQ/pfS2s1NhanSctGwwdS6UgnxuWAbNE569dn+zmP42Vz2XAxg1Lud3s5x
Mmo6Uw6y0ASueqTLdRnNC9obzcyKUukdCj06Y6f9CBEkdm0BwZRydblXtEOl/bv9
xB1c/tpc8CJCDyOjfBX6DRHbXFmIBRFl+BgchL17S28INR/rPDbEFTM7NKrrhBxM
6QuzLi3cV/qtCrl/+F84QmAOWBWgniJwM3qlaTcgfrfiUVrZCZzXlvXgoUqYMLtF
4pc=
=s9R6
-----END PGP MESSAGE-----
'''
# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "name": "LINKSFIELD_PM",
    "profileTypeName": "profile_test_1012",
    "pgpfile": pgp_file_content
}

# 创建一个 Session 对象
session = requests.Session()

# 使用自定义的 CA 证书
session.verify = custom_ca_path

session.cert = (client_cert_path, client_key_path)

response = session.post(api_url, json=payload ,verify=False)

print(response.text)


