import unittest
import requests
import hashlib
import hmac
import base64
import json


class APITestBase:
    def __init__(self, path, method, partner_code):
        self.path = path
        self.method = method
        self.partner_code = partner_code

    def generate_secret_key(self):
        get_key_url = "https://lk-api-v1.linksfield.net/mp/debug/secret/generateSecretKey"
        headers = {"Accept-Language": "en-US", "Content-Type": "application/json"}
        params = {"partnerCode": self.partner_code}

        response = requests.get(get_key_url, headers=headers, params=params)
        data = response.json().get('data', {})

        return data.get('accessKey'), data.get('secretKey')

    def create_signature(self, access_key, secret_key, header=''):
        str_to_sign = f"{self.method}\n{self.path}\n{header}\n{access_key}\n\nAccept-Language:en-US\nContent-Type:application/json\n"
        sign = base64.b64encode(hmac.new(secret_key.encode(), str_to_sign.encode(), hashlib.sha256).digest()).decode('utf-8')
        return sign

    def make_request(self, method, headers, url, **kwargs):
        response = requests.request(method, url, headers=headers, **kwargs)
        response_str = json.dumps(response.json(), indent=4)
        print(response_str)


class APITEST(APITestBase):
    def headers_parmas(self, access_key, signature):
        headers = {
            "X-HMAC-ALGORITHM": "hmac-sha256",
            "X-HMAC-ACCESS-KEY": access_key,
            "X-HMAC-SIGNED-HEADERS": "Accept-Language;Content-Type",
            "Accept-Language": "en-US",
            "Content-Type": "application/json",
            "X-HMAC-SIGNATURE": signature
        }
        return headers

    def productList(self, access_key, signature):
        url = "https://lk-api-v1.linksfield.net" + self.path
        headers = self.headers_parmas(access_key, signature)
        self.make_request('GET', headers, url)

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

    def queryTraffic(self, access_key, signature, orderCode):
        url = "https://lk-api-v1.linksfield.net" + self.path
        headers = self.headers_parmas(access_key, signature)
        params = {"orderCode": orderCode}
        self.make_request('GET', headers, url, params=params)


class TestAPITEST(unittest.TestCase):
    def test_api_productList(self):
        api_test = APITEST("/mp-api/api/esim/v2/productList", "GET", "SU4JJX5PDN")
        access_key, secret_key = api_test.generate_secret_key()
        signature = api_test.create_signature(access_key, secret_key)
        api_test.productList(access_key, signature)

'''
    def test_api_activationCode(self):
        api_test = APITEST("/mp-api/api/esim/v2/activationCode", "POST", "SUPV9TB9OS")
        access_key, secret_key = api_test.generate_secret_key()
        signature = api_test.create_signature(access_key, secret_key)
        api_test.activationCode(access_key, signature, productId=102, iccid='', price='', activateFlag='no')

    def test_api_queryTraffic(self):
        api_test = APITEST("/mp-api/api/esim/queryTraffic", "GET", "QY-001018")
        access_key, secret_key = api_test.generate_secret_key()
        signature = api_test.create_signature(access_key, secret_key, header='orderCode=ORDER_1752214497189199872')
        api_test.queryTraffic(access_key, signature, orderCode='ORDER_1752214497189199872')
'''

if __name__ == '__main__':
    unittest.main()
