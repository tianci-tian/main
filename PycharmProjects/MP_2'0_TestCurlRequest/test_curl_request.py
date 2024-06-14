import requests
import unittest
from parameterized import parameterized

class TestCurlRequest(unittest.TestCase):

    @parameterized.expand([
        ('https://lk-api-v2.linksfield.net/mp/debug/secret/generateSecretKey?partnerCode=CN00000890',
         {'Accept-Language': 'en-US', 'Content-Type': 'application/json'}),
        #使用@parameterized.expand装饰器
        #可以添加更多元组，每个元组包含一个不同的 url 和对应的 headers
    ])
    def test_curl_request(self, url, headers):
        # 调用方法并传递参数
        response = self.make_request(url, headers)

        # 断言响应状态码为 200（OK）
        self.assertEqual(response.status_code, 200)

        # 打印响应内容
        print("Response Content:")
        print(response.text)

    def make_request(self, url, headers):
        # 发送请求并返回响应
        return requests.get(url, headers=headers)

if __name__ == '__main__':
    unittest.main()
