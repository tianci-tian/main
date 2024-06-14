#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 10:03
# @Author  : 朱宽
# @File    : Run_threads不稳定.py
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
from tomorrow import threads
from config import globalConfig
from src.utils.DingDelivery import PushDataForDingDing
from config.globalConfig import test_script_path

# 获取路径，用于构建run()函数中的log_path
report_path = globalConfig.test_report_path


def add_case():
    '''
    加载所有的测试用例
    '''
    test_suite_mine = unittest.defaultTestLoader.discover(test_script_path, pattern='test*.py')  # python中的discover函数
    return test_suite_mine


'''
# 线程数量设置要符合规律，N核服务器，通过执行业务的单线程分析出本地计算时间为x，
等待时间为y，则工作线程数（线程池线程数）设置为 N*(x+y)/x，能让CPU的利用率最大化。
'''


@threads(5)
def run(test_suite):
    '''
    多线程运行测试报告
    :param test_suit:
    :return:
    '''
    result = BeautifulReport(test_suite)  # 将测试集合传给Beautiful Report
    # 调用report()方法并传参生成报告
    result.report(filename='自动化测试报告--多线程运行', description="测试报告", log_path=report_path)


if __name__ == "__main__":
    '''
    多线程运行；
    不稳定的原因，多线程执行时，由于结束时间不一样，不能按照脚本加载顺序写入测试报告中；
    暂无能力修改BeautifulReport源码；
    其他数据暂无发现不妥之处。
    '''
    # 用例集合
    cases = add_case()
    for i in cases:  # TestScript中必须要有测试脚本，没有的话，for循环不运行
        run(i)

    send_report = PushDataForDingDing()  # 实例化钉钉发送报告类
    send_report.post_message()  # 调用发送函数


