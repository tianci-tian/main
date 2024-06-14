import requests
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
endpoint = '/apiProxy/operPgpFile'
api_url = f'https://{host}{endpoint}'
pgp_file_content = '''
-----BEGIN PGP MESSAGE-----
Version: BCPG v1.62

hIwDHbUIJ/QWl3YBA/9oaJkiJu8jFr9Cq+fvXo2RLa2SEW+fHD0XWN3GFmgQweZv
QTBd5oTyWwX953C0Qzcm1OlReIoKNS4MsHv1N4ojNu6Ob8Zfy3hkGxCJlOidCfw+
AATo8C+5knIZ5nSpGeD5mOYRaSY8qvPNWqu2pD0cKuoIQU2HIRsCJZdiN2psndLB
MwHybh7fJO2NfZxk7MSU/QTxF7gG6w9Yf2tvZ+Jj+lo3FCjSYk3EIjoKEI+NRYp1
ZIRfO2a04515+E4yYIvtd9w24/sVmMCNXxrRAE8syl3+QzbymEvxsS2y/arI7yMf
joUKC2tCgd9ljTB1m0TaWqemXnHp0F3LHvmbGrwYQw86AYaaqFynuOdSkV/PxmDy
gZ1D+rqVbY+5TOP4Xp4aOVqJzrOae+VFvyN8deu99ZyWB4QEHL6Mey/D2UWP4yQp
EM/GxYoANvJrJGuiQOpMPQlj+4o2CBhVfbMEhEC5hISaWCjoNllh7iOMzqHMI1sg
9led/hVo0v80OuuqUPRbyoaxudNlOqsz2tB95vTCv4HGVk5ks07Dm7o1dCBWyS1K
2uzECFVhkUJMB5E5HFm1EocI2qRfgLkH9lKT15ELaHNLj7CP5yZKG4n1xsnbFjF7
U70kNNCZhftSLnKC50g7kjFAXLf2xucHPVheWcPHyYjwzshrLfIWnLAFVWpGvRsa
lMWZvaVIUNIwMLM2U23eRUXNYyxvBwWluoopDe3Lr05QuJiN5dJlCprr2U4DbxFv
bBDg0P8u269K3PH+aAGObCtqmrT8SsUAbyyM/aipthW3MG8KDZIGL8hs0wYCgJmq
4TLMjiABF6o/u/7IO9BFWuKx7xE=
=WFZC
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

response = session.post(api_url, json=payload ,verify=False)

print(response.text)


