# -*- coding: utf-8 -*-
# @Project : APITestModel
# @File    : DingDelivery.py
# @Author  : 朱宽
# @Time    : 2021/4/1 14:16
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
import json
import os
from config import globalConfig


class PushDataForDingDing():
    '''
    给钉钉机器人发送消息
    '''

    def __init__(self):
        self.server_host_url_head= globalConfig.auto_test_server_host_url_head
        self.report_url = self.create_url()
        self.content = "自动化测试报告新鲜出炉！请查看：" + self.report_url
        self.url= globalConfig.ding_url
        self.header = {'Content-Type': 'application/json'}
        self.data = {
            "msgtype": "text",
            "text": {
                "content": self.content
            }
        }

    def create_url(self):
        '''
        获取最新报告的url
        :return:
        '''
        new_report_name = self.get_last_report()
        report_url = self.server_host_url_head + new_report_name

        return report_url

    def get_last_report(self):
        '''
        获取最新测试报告
        :return:
        '''
        dirs = os.listdir(globalConfig.test_report_path)
        dirs.sort()
        dirs_html = []
        for filename in dirs:  # 找到文件夹中后缀为.html的最新的那个文件
            file, suffix = os.path.splitext(filename)
            if suffix == '.html':
                dirs_html.append(filename)
        new_report_name = dirs_html[-1]

        return new_report_name

    def post_message(self):
        '''
        发送报告
        :return:
        '''
        res = requests.post(url=self.url, headers=self.header, data=json.dumps(self.data))

        # print(res.json())


if __name__ == "__main__":
    test_class = PushDataForDingDing()
    test_class.post_message()
    print(type(test_class.get_last_report()))
