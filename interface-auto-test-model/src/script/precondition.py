import unittest,requests,hashlib,hmac,base64,json
'''
unittest单元测试框架
执行用例时，更改测试使用的运营商，例如：QY-001018  领科测试企业1
                                SUPV9TB9OS 领科测试企业1.1
                                测试环境：
                                QY-001018  领科测试企业1
                                SU4JJX5PDN  领科测试企业2
激活订单请求修改 商品id(productId)
查看余量修改 订单编号(orderCode)

'''
#操作前处理,请求基础
class APITestBase:
    def __init__(self, path, method, partner_code):
        self.path = path
        self.method = method
        self.partner_code = partner_code

    # 获取测试企业的密钥对
    def generate_secret_key(self):
        get_key_url = "https://lk-api-v1.linksfield.net/mp/debug/secret/generateSecretKey"
        headers = {"Accept-Language": "en-US", "Content-Type": "application/json"}
        params = {"partnerCode": self.partner_code}

        response = requests.get(get_key_url, headers=headers, params=params)
        data = response.json().get('data', {})

        return data.get('accessKey'), data.get('secretKey')

    #签名
    def create_signature(self, access_key, secret_key, header=''):
        str_to_sign = f"{self.method}\n{self.path}\n{header}\n{access_key}\n\nAccept-Language:en-US\nContent-Type:application/json\n"
        sign = base64.b64encode(hmac.new(secret_key.encode(), str_to_sign.encode(), hashlib.sha256).digest()).decode('utf-8')
        return sign

    def make_request(self, method, headers, url, **kwargs):
        response = requests.request(method, url, headers=headers, **kwargs)
        response_str = json.dumps(response.json(), indent=4)
        print(response_str)

#接口逻辑处理
class APITEST(APITestBase):
    def headers_parmas(self,access_key, signature):
        headers = {
            "X-HMAC-ALGORITHM": "hmac-sha256",
            "X-HMAC-ACCESS-KEY": access_key,
            "X-HMAC-SIGNED-HEADERS": "Accept-Language;Content-Type",
            "Accept-Language": "en-US",
            "Content-Type": "application/json",
            "X-HMAC-SIGNATURE": signature
        }
        return headers
    #获取商品请求
    def productList(self, access_key, signature):
        url = "https://lk-api-v1.linksfield.net" + self.path
        headers = self.headers_parmas(access_key, signature)
        self.make_request('GET', headers, url)

    #激活订单请求
    def activationCode(self, access_key, signature, productId, iccid, price, activateFlag):
        url = "https://lk-api-v1.linksfield.net" + self.path
        headers = self.headers_parmas(access_key, signature)
        requests_body = {
            "productId": productId,
            "iccid": iccid,
            "price": price,
            "activateFlag": activateFlag
        }
        body = json.dumps(requests_body)
        self.make_request('POST', headers, url, data=body)

    #查看余量请求
    def queryTraffic(self, access_key, signature, orderCode):
        url = "https://lk-api-v1.linksfield.net" + self.path
        headers = self.headers_parmas(access_key, signature)
        params = {"orderCode": orderCode}
        self.make_request('GET', headers, url, params=params)
