# -*- coding: utf-8 -*-
# @Project : AuTestModel--非UI
# @File    : 测试用例模板.py
# @Author  : 朱宽
# @Time    : 2021/4/6 15:16
# @Software: Win10 / Python3 / Pycharm
from ddt import ddt,data # 调用ddt模块，用于数据驱动
from src.public.ddtInput import EveryTestCaseFlag # 用于给ddt输入指定TestCaseFlag的值
from src.utils import GetLog
import unittest
import sys

file_name='testdata.xlsx'# 测试数据名称，放在testdata文件下。测试数据模板请看“接口数据模板解析”

# current_file_name  为要测试的文件,获取文件名称
current_file_name = 'test_1'
testLogger = GetLog.Logger(current_file_name).getlog()# 将测试用例脚本名称加载在日志模块中，打印日志时，会带上。



'''
        @ddt 使用ddt
        
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

    def tearDown(self):
        pass



if __name__=="__main__":
    unittest.main()



