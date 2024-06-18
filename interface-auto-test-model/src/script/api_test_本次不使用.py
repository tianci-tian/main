#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 11:42
# @Author  : 朱宽
# @File    : api_test_本次不使用.py
# @Software: Win10、Python3.8.5 and Pycharm
# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

from ddt import ddt,data # 调用ddt模块，用于数据驱动
from src.public.ddtInput import EveryTestCaseFlag # 用于给ddt输入指定TestCaseFlag的值
from src.utils import GetLog
import unittest
import sys
from src.script.precondition import APITestBase,APITEST
file_name='testdata.xlsx'

# current_file_name  为要测试的文件,获取文件名称
current_file_name = 'test_1'
testLogger = GetLog.Logger(current_file_name).getlog()



'''
        @data中是调用EveryTestCaseFlag类中的get_every_TestCaseFlag函数;
        file_name是指定的测试数据的文件名称；
        TestCaseFlag是指定的同一类测试用例，只是测试数据不同，属于正确和错误的测试用例数据；
        data是依据TestCaseFlag筛选的结果；

        如果TestCaseFlag设为空，则ddt加载的数据为空，就不会执行UnitTest()这个类
'''

@ddt
class UnitTest(unittest.TestCase):

    def setUp(self):
        pass

    @data(*EveryTestCaseFlag(file_name=file_name,TestCaseFlag='wifiGroup').get_every_TestCaseFlag())
    def test_1_test1(self,data):
        '''
        测试用例Flag：wifiGroup；
        :param data--标记为wifiGroup的测试用例；
        '''
        testLogger.info('{}.{}已测试；结果为：；测试数据为：{}'.format(self.__class__.__name__,sys._getframe().f_code.co_name,data))

    @data(*EveryTestCaseFlag(file_name=file_name,TestCaseFlag='delete_wifigroup').get_every_TestCaseFlag())
    def test_1_test2(self,data):
        testLogger.info('{}.{}已测试；结果为：；测试数据为：{}'.format(self.__class__.__name__,sys._getframe().f_code.co_name,data))

    # 执行用例
    def test_api_productList(self):
        api_test = APITEST("/mp-api/api/esim/v2/productList", "GET", "SU4JJX5PDN")
        access_key, secret_key = api_test.generate_secret_key()
        signature = api_test.create_signature(access_key, secret_key)
        api_test.productList(access_key, signature)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()



