# -*- coding: utf-8 -*-
# @Project : RedisUtils.py
# @File    : dynamicData.py
# @Author  : 朱宽
# @Time    : 2021/9/9 11:25
# @Software: Win10 / Python3 / Pycharm
# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

from src.utils.HttpCommonRequest import HttpRequests

class  dynamicData():
    '''
        主要用于提取动态数据；
        （1）cookie
    '''
    def extract_cookie(self,data):
        '''
        （1）主要用于提取cookie内的值
        :param data:登录接口的相关数据

                data = {
                            "Method": "get",
                            "Uri": "/api/regdc",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "SendData": {
                                "ver": "1",
                                "method": "login",
                                "account": "jimitest",
                                "password": "106|105|109|105|49|50|51",
                                "language": "zh"
                            }
                }
        :return:
        '''
        http_requests=HttpRequests()
        res=http_requests.send_request(data)

        res_cookies=res.cookies.items() # res_cookies --> [(a,a1),(b,b1)] 列表套元组
        cookie_str=''
        for key,value in res_cookies:
            ''' for 循环针对列表；key,value 取元组中的值 '''
            #print(res_cookies,type(res_cookies))
            cookie_str=cookie_str+key+'='+value+';'

        return cookie_str

if __name__=="__main__":
    data={
            "Method": "get",
            "Uri": "/api/regdc",
            "Content-Type": "application/x-www-form-urlencoded",
            "SendData": {
                "ver": "1",
                "method": "login",
                "account": "jimitest",
                "password": "106|105|109|105|49|50|51",
                "language": "zh"
                        }
    }

    test=dynamicData()
    cookie=test.extract_cookie(data)
    print(cookie,type(cookie))

