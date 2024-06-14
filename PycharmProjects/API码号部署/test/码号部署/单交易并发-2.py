import requests
import concurrent.futures
import pandas as pd
import time

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

# 定义请求参数
sequence_id = "123456789"
name = "LINKSFIELD_PM"
pgp_public_key = '''
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: BCPG v1.62

mI0EZVRjAwEEAKGVTZCv6UX9KruEeoOb1c/sMChPoh48YdqKoM0IKi8Z/FygnfI4
Te0QKGbEFjxCVpXeZ4+rRoHcMrD3X+S4b7z8h/0wgeutZ90A6CEk0p78nCSM2cRG
Uob8iE/XR2h9so7XcQOGvfH2c9InbbFJX98iupL6SsvpsA/+6vxQ9CEhABEBAAG0
CkxpbmtzRmllbGSInAQQAQIABgUCZVRjAwAKCRA3S563U/zNUiBTA/40mOIQZbvG
452SkiwL5tYrgodQxOkjEtm8aVbMVpaTrtNmir9cRjwhYacZGnLn8JzXOl5PMWtn
+HnOp4E28zxqo/KNuAL2Y1dnKIt1Lxmm1YR+7GHUMcZz7uQ0NeWvWq9a+/AiQQlY
Zy8rSj6jLbELphAoepvlhDzjiR2w4mLcqg==
=02yK
-----END PGP PUBLIC KEY BLOCK-----
'''

# 从Excel文件读取 pgp_file_content
excel_file_path = 'D:\\项目\\DP+\\实施部署API\\测试环境\\profile.xlsx'
excel_data = pd.read_excel(excel_file_path)
pgp_file_contents = excel_data['pgp_file_content'][0:].tolist()
# 从Excel文件读取 profile_type_name
excel_file_path = 'D:\\项目\\DP+\\实施部署API\\测试环境\\profile.xlsx'
excel_data = pd.read_excel(excel_file_path)
profile_type_name = excel_data['profile_type_name'][0:].tolist()
'''
print(profile_type_name)
print(pgp_file_contents)
'''


# 使用自定义的 CA 证书
verify = custom_ca_path
cert = (client_cert_path, client_key_path)
# 函数用于发送请求并检查成功
def send_request(profile_type_name,pgp_file_content):
    payload = {
        "sequenceId": sequence_id,
        "name": name,
        "profileTypeName": profile_type_name,
        "pgpPublickey": pgp_public_key,
        "pgpfile": pgp_file_content
    }

    with requests.Session() as session:
        session.verify = verify
        session.cert = cert
        start_time = time.time()
        response = session.post(api_url, json=payload, verify=False)
        print(response.text)
        elapsed_time = time.time() - start_time

        try:
            result = response.json()
            if "success" in result.get("data", {}).get("msg", "").lower():
                return True, elapsed_time
            else:
                return False, elapsed_time
        except Exception as e:
            print(f"解析响应时出错: {e}")
            return False, elapsed_time


# 跟踪成功请求和总耗时
successful_requests = 0
total_elapsed_time = 0

# 处理结果并计算指标的函数
def process_result(result):
    global successful_requests, total_elapsed_time
    success, elapsed_time = result
    total_elapsed_time += elapsed_time
    if success:
        successful_requests += 1


# 记录开始时间以测量总耗时
start_time_total = time.time()

# 并发发送100个请求
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # 使用 submit 方法提交任务
    futures = [
        executor.submit(send_request, profile_type_name, pgp_file_content)
        for profile_type_name, pgp_file_content in zip(profile_type_name, pgp_file_contents)
    ]

    # 处理结果
    for future in concurrent.futures.as_completed(futures):
        process_result(future.result())

# 计算指标
total_requests = len(pgp_file_contents)
end_time_total = time.time()
total_elapsed_time_total = end_time_total - start_time_total
time_per_request = total_elapsed_time_total / total_requests
requests_per_second = total_requests / total_elapsed_time_total
# 输出结果
print(f"任务数量: {total_requests}")
print(f"总耗时(秒): {total_elapsed_time_total:.2f}")
print(f"每次请求耗时(秒): {time_per_request:.4f}")
print(f"每秒承载请求数: {requests_per_second:.2f}")
print(f"通过数量: {successful_requests}")