# -*- coding: utf-8 -*-
# @Project : APITestModel
# @File    : HttpCommonRequest.py
# @Author  : 朱宽
# @Time    : 2021/4/6 9:59
# @Software: Win10 / Python3 / Pycharm

# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

import requests
from config import globalConfig
import re

class HttpRequests():
    '''
    http请求的公共调用方式。后续遇到更多请求方式时，请依据软件工程中“高内聚，低耦合”的原则进行扩展。
    '''

    def __init__(self):
        self.protocol = globalConfig.http_protocol
        self.host = globalConfig.http_host

        if re.match('[a-zA-Z].*',self.host)!=None:
            ''' 当配置文件中的 http_host 的开头为字母时，执行if  '''
            self.url_header = self.protocol + "://" + self.host
        else:
            self.port = globalConfig.http_port
            self.url_header = self.protocol + "://" + self.host + ":" + self.port
        #print(self.url_header)

        self.path = globalConfig.project_directory_path + '/HttpCommonRequest'

    def send_request(self, data):
        '''
        封装发送RestFul风格的http请求。get、post、put、delete、patch
        :param data:<ReadTestData.py 自动转换为下列模式>

                # Cookie 在其他接口输入数据的时候，调用提取Cookie的公共方法，然后自行添加至该字典中

                                data = {
                                    "Cookie":"d55f1116-a279-49f4-afe3-bfdc3d6f8ba8",
                                    "Method": "get",
                                    "Uri": "/api/regdc",
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "SendData": {
                                        "ver": "1",
                                        "method": "getdate",
                                        "account": "jimitest",
                                        "password": "106|105|109|105|49|50|51",
                                        "language": "zh"
                                    }


        :return:
        '''
        try:
            result = None

            url = self.url_header + data['Uri']
            method = data['Method'].lower()
            header = {'Content-Type': data['Content-Type']}  # http数据包头部构建

            for i in data.keys():
                if re.match('cookie.*',i.lower())!=None: #当key中存在cookie字样，则执行if内的语句
                    header['cookie']=data['cookie']
                    break

            send_data = data['SendData']  # 发送数据

            if method == 'get':  # get请求
                if send_data != None:
                    result = requests.get(url, params=send_data, headers=header)  # get带参数请求
                else:
                    result = requests.get(url, headers=header)  # get不带参数请求

            elif method == 'post':  # post请求
                if header['Content-Type'] == 'application/x-www-form-urlencoded':
                    if send_data != None:
                        result = requests.post(url, data=send_data, headers=header)
                    else:
                        result = requests.post(url, headers=header)

                elif header['Content-Type'] == 'text/xml':
                    if send_data != None:
                        result = requests.post(url, json=send_data, headers=header)
                    else:
                        result = requests.post(url, headers=header)

                elif header['Content-Type'] == 'application/json':
                    if send_data != None:
                        result = requests.post(url, json=send_data, headers=header)
                    else:
                        result = requests.post(url, headers=header)

                elif header['Content-Type'] == 'multipart/form-data':
                    if send_data != None:
                        result = requests.post(url, data=send_data, headers=header)
                    else:
                        result = requests.post(url, headers=header)

                else:
                    print('post方式不存在这种传递模式，请在下面位置扩展：', self.path, '--56行')

            elif method == 'put':  # put请求
                if header['Content-Type'] == 'application/x-www-form-urlencoded':
                    if send_data != None:
                        result = requests.put(url, data=send_data, headers=header)
                    else:
                        result = requests.put(url, headers=header)

                elif header['Content-Type'] == 'text/xml':
                    if send_data != None:
                        result = requests.put(url, json=send_data, headers=header)
                    else:
                        result = requests.put(url, headers=header)

                elif header['Content-Type'] == 'application/json':
                    if send_data != None:
                        result = requests.put(url, json=send_data, headers=header)
                    else:
                        result = requests.put(url, headers=header)

                elif header['Content-Type'] == 'multipart/form-data':
                    if send_data != None:
                        result = requests.put(url, data=send_data, headers=header)
                    else:
                        result = requests.put(url, headers=header)

                else:
                    print('put方式不存在这种传递模式，请在下面位置扩展：', self.path, '--68行')

            elif method == 'delete':  # delete请求
                if header['Content-Type'] == 'application/x-www-form-urlencoded':
                    if send_data != None:
                        result = requests.delete(url, data=send_data, headers=header)
                    else:
                        result = requests.delete(url, headers=header)

                elif header['Content-Type'] == 'text/xml':
                    if send_data != None:
                        result = requests.delete(url, json=send_data, headers=header)
                    else:
                        result = requests.delete(url, headers=header)

                elif header['Content-Type'] == 'application/json':
                    if send_data != None:
                        result = requests.delete(url, json=send_data, headers=header)
                    else:
                        result = requests.delete(url, headers=header)

                elif header['Content-Type'] == 'multipart/form-data':
                    if send_data != None:
                        result = requests.delete(url, data=send_data, headers=header)
                    else:
                        result = requests.delete(url, headers=header)

                else:
                    print('delete方式不存在这种传递模式，请在下面位置扩展：', self.path, '--80行')

            elif method == 'patch':  # patch请求
                result = requests.patch(url, headers=header)

            else:
                print('不存在这种方法，请在下面位置扩展：', self.path, '--74行')
            return result
        except Exception as e:
            print(self.path, '  ', e)


if __name__ == "__main__":
    data = {'TestCaseFlag': 'delete_wifigroup', 'CorrectFlag': None, 'Method': 'post',
            'Uri': '/robot/send?access_token=3f5ffb3f22f471b405ee05a3dd9e51502fb7b2d37e3c16956672c067653fa685',
            'Content-Type': 'application/json',
            'SendData': {
                "msgtype": "text",
                "text": {
                    "content": "缺陷汇报者--初代，与python脚本通信成功！"
                }
            },
            'AssertInfo': {'code': 100000, 'msg': '成功'}, 'CaseDescription': '考勤点-删除Wifi分组', 'Rely': 'no',
            'Extract': None, 'MockFlag': None, 'MockData': {'code': 100000, 'msg': '成功'}}
    test = HttpRequests()
    result = test.send_request(data)
    print(re)
