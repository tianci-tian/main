import requests
import concurrent.futures
import pandas as pd
import time
'''
max_workers控制请求并发数量
测试数据从profile.xlsx读取,请求参数存储到列表中,向并发请求传参
计算请求数量、用时数据
'''
# CA 证书文件路径
custom_ca_path = 'D:\\downloads\\lk-ca.crt'

# 客户端证书文件路径和私钥文件路径
client_cert_path = 'D:\\downloads\\linksfield_pm.crt'
client_key_path = 'D:\\downloads\\private.key'
Passphrase = '123456'

# API 地址
host = 'dppoapiproxy.linksfield.net'
endpoint = '/apiProxy/deployAndProduceQr'
api_url = f'https://{host}{endpoint}'

# 请求参数
name = "LINKSFIELD_PM"

# 从Excel文件读取 pgp_file_content
excel_file_path = 'D:\\项目\\DP+\\实施部署API\\Pre环境\\profile.xlsx'
excel_data = pd.read_excel(excel_file_path)
pgp_file_contents = excel_data['pgp_file_content'][0:].tolist()
# 从Excel文件读取 profile_type_name
excel_file_path = 'D:\\项目\\DP+\\实施部署API\\Pre环境\\profile.xlsx'
excel_data = pd.read_excel(excel_file_path)
profile_type_name = excel_data['profile_type_name'][0:].tolist()
# 从Excel文件读取 iccid->sequenceId
excel_file_path = 'D:\\项目\\DP+\\实施部署API\\Pre环境\\profile.xlsx'
excel_data = pd.read_excel(excel_file_path)
iccids = excel_data['iccid'][0:].tolist()
'''
print(profile_type_name)
print(pgp_file_contents)
'''


# CA 证书
verify = custom_ca_path
cert = (client_cert_path, client_key_path,Passphrase)
# 发送请求成功次数计数
count = 1
def send_request(iccid, profile_type_name, pgp_file_content):
    global count
    payload = {
        "sequenceId": iccid,
        "name": name,
        "profileTypeName": profile_type_name,
        "pgpfile": pgp_file_content
    }

    with requests.Session() as session:
        session.verify = verify
        session.cert = cert
        start_time = time.time()
        response = session.post(api_url, json=payload, verify=False)
        print(response.text)
        print(count)
        count += 1
        elapsed_time = time.time() - start_time

        try:
            result = response.json()
            if "rsp-0001.linksfield.net" in result.get("data", {}).get("qrCode", "").lower():
                print(f"ICCID: {iccid}, 响应时间: {elapsed_time:.4f} 秒")
                return True, elapsed_time
            else:
                print(f"ICCID: {iccid}, 请求失败，响应时间: {elapsed_time:.4f} 秒")
                return False, elapsed_time
        except Exception as e:
            print(f"ICCID: {iccid}, 解析响应时出错: {e}")
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
with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
    # 使用 submit 方法提交任务
    futures = [
        executor.submit(send_request,iccid, profile_type_name, pgp_file_content)
        for iccid,profile_type_name, pgp_file_content in zip(iccids,profile_type_name, pgp_file_contents)
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


