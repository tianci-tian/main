#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 10:45
# @Author  : 朱宽
# @File    : run.py
# @Software: Win10、Python3.8.5 and Pycharm
'''
    命令行执行某python文件时
    用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
'''
import sys
import os
item_path=os.path.dirname(os.path.abspath(__file__))
print(item_path)
sys.path.append(item_path)

import unittest
from src.utils.BeautifulReport import BeautifulReport
from config import globalConfig
import time
from src.utils.DingDelivery import PushDataForDingDing
from config.globalConfig import test_script_path
from src.utils.EmailDelivery import send_email

class RunClass():
    '''
    运行类
    '''

    def run(self, folder, pattern):
        '''
        运行函数
        :param folder: 测试脚本的文件夹
        :param pattern: 测试脚本；可以是指定一类脚本，也可以指定一个脚本
        :return:
        '''
        test_suite = unittest.defaultTestLoader.discover(folder, pattern=pattern)
        result = BeautifulReport(test_suite)
        report_path = globalConfig.test_report_path
        time_now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))  # 获取当前时间，用于日志名称命名
        filename = '自动化测试报告-' + time_now
        result.report(filename=filename, description="测试报告", log_path=report_path)
        # 钉钉发送
        #send_report = PushDataForDingDing()  # 实例化钉钉发送报告类
        #send_report.post_message()  # 调用发送函数
        # 邮箱发送
        html_report_path = f'testreport/{filename}.html'
        send_email(html_report_path)

if __name__ == "__main__":
    '''
    单线程运行
    '''
    my_run = RunClass()
    my_run.run(test_script_path, "test*.py")
