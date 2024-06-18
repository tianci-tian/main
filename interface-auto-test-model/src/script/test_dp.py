# -*- coding: utf-8 -*-
# @Project : AuTestModel--非UI
# @File    : test_dp.py
# @Author  : 朱宽
# @Time    : 2021/4/6 15:16
# @Software: Win10 / Python3 / Pycharm
from ddt import ddt,data,unpack# 调用ddt模块，用于数据驱动
from src.public.ddtInput import EveryTestCaseFlag # 用于给ddt输入指定TestCaseFlag的值
from src.utils import GetLog
import unittest,requests,json,sys,os
item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 获取该项目的根目录
sys.path.append(item_path) # 将该项目的根目录（/interface-auto-test-model）临时添加在 系统的环境变量 中

#file_name='testdata_dp.xlsx'# 测试数据名称，放在testdata文件下。测试数据模板请看“接口数据模板解析”
file_name = 'testdata_dp.xlsx'
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

    @data(*EveryTestCaseFlag(file_name).get_every_TestCaseFlag('profileQuery'))
    @unpack
    def testOne(self,**testdata):
        '''
        测试用例Flag：profileQuery；
        :param data--根据iccid查询；
        '''
        response = requests.request(method=testdata["Method"], url=(testdata["Url"] + testdata["SendData"]['path']), headers=testdata["headers"],
                                    params=testdata["SendData"]['params'])
        # 将响应内容解析为 JSON，并禁用 ASCII 编码
        response_json = response.json()
        response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
        try:
            self.assertEquals(response_json['code'], testdata['AssertInfo']['code'])
            msg = True
        except AssertionError:
            msg = False
        testLogger.info('{}.{}已测试；结果为：{}；测试数据为：{}'.format(self.__class__.__name__,sys._getframe().f_code.co_name,msg,response_str))

    def tearDown(self):
        pass



if __name__=="__main__":
    unittest.main()




