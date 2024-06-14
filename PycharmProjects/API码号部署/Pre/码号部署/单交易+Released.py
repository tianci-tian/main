import requests
import time
'''
单iccid码号部署
变量参数pgpfile在接口请求外部定义
'''
# CA 证书文件路径
custom_ca_path = 'D:\\downloads\\lk-ca.crt'

# 客户端证书文件路径和私钥文件路径
client_cert_path = 'D:\\downloads\\client.crt'
client_key_path = 'D:\\downloads\\client.key'
# API 地址、参数
host = 'dppoapiproxyp.linksfield.net'
endpoint = '/apiProxy/deployAndProduceQr'
api_url = f'https://{host}{endpoint}'
pgp_file_content = '''
-----BEGIN PGP MESSAGE-----
Version: BCPG v1.62

hIwDPYe2aQXQyfABA/47zkCdZW4GXNM74KxLTwUXwbOinTKElhE2aTKDRsnh7les
drT5Aw4Fj/3Uggt3pwJfBnibzPdvo57NwIvnwHmyVOrALaqsrlWzTfj22WptQzgZ
3GBdh/hlNL+Y1Aii73WfnySd0bKTUJo9OvwxRIE6hAF8SHOxRdjrWm2saO7u6dLB
IwHlz++CDMRns5v5Yo3TK3vcAiQekXrShvdlVXspK40LsXfZwD0Zm2HoagxNJCJe
T0u/Th49Is8XlsuPRi8LcZPnzOmv6BW9MsGsviSXUhJ9vxsVbFk6kyZ5ZvUHPuCl
sJVAFbG1uUanXS1cAO9I0ZsLpQsvqrsoc1IIp47o4b8ZyqmvQrdYpp0JJVortk5Y
BAO+9umqNhyjjxaKUUopBpvY1IhaxylpqoxaTXo9VXuxTAm+1GPCFe7/gM+2W0sF
LxJpC7ODgUjWbZMlMOgeTvbNfomNyMLJMN0+SnAqIeF2rHVQ7gJNyszIlPqCA9T8
vPJ9SWwLSPrZYG4WRBwQf3w0GDItYXnEmtxHFzRY/3ickdGm4w/QkYHyOUSyRbLZ
a4flJMqr9CG3irHnJD8ogCBO5JDAxKnOXxZM8eIBIRikBJMFszmNgoSxBAGIhkAE
cr9IUIX/grvr7cSTbLkloF+SEiT79mFKlXvLrcy5hqDr/oC4BjFQMuVW8leD0rPX
glmigJI8SNZlAHhJPfliu4gQo8BhdJJWJNVWQz+8+Che7TG3owXPRDjE/VlMD+Mp
bTLXQ3oJovXpBVtdPEK/EMnHz/sTnzAGiVEgcGtAi4Xe1ikWD33iseoBjpb7hPEO
MGZ0DQ==
=eMk+
-----END PGP MESSAGE-----
'''
# 定义请求参数
payload = {
    "sequenceId": "123456789",
    "name": "apiTest",
    "profileTypeName": "profile_apiTest_45407_002",
    "pgpfile" : pgp_file_content
}

session = requests.Session()

session.verify = custom_ca_path# 使用自定义的 CA 证书


session.cert = (client_cert_path, client_key_path)
#发出API请求之前获取时间戳
request_time = time.time()
response = session.post(api_url, json=payload ,verify=False)
#计算API请求的持续时间
duration = time.time() - request_time
print(f"API Response: {response.text}")
print(f"API Request Duration: {duration} seconds")



