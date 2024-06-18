# -*- coding: utf-8 -*-
# @Project : APITestModel
# @File    : ddtInput.py
# @Author  : 朱宽
# @Time    : 2021/4/1 9:28
# @Software: Win10 / Python3 / Pycharm

# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
import sys
import os
from openpyxl import load_workbook
item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 获取该项目的根目录
sys.path.append(item_path) # 将该项目的根目录（/interface-auto-test-model）临时添加在 系统的环境变量 中

from src.utils.ReadTestData import ReadExcel
class EveryTestCaseFlag():
    '''
    主要获取指定测试用例名称标记的测试用例，并将这个用例组成列表返回
    '''

    def __init__(self, file_name):

        self.ReadExcel = ReadExcel(file_name=file_name)  # 初始化这个类
        self.test_data_all = self.ReadExcel.test_data()  # 调用这个函数，得到所有的测试用例数据


    def get_every_TestCaseFlag(self,TestCaseFlag):
        self.TestCaseFlag = TestCaseFlag  # 全局化这个参数
        '''
        主要实现，在所有测试数据中筛选指定TestCaseFlag的用例数据
        :return:
        '''
        try:
            test_case_flag = []
            for i in range(0, len(self.test_data_all)):

                if self.TestCaseFlag == self.test_data_all[i]['TestCaseFlag']:
                    test_case_flag.append(self.test_data_all[i])

            return test_case_flag

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import json

    test = EveryTestCaseFlag(file_name='testdata_dp.xlsx', TestCaseFlag='profileQuery')
    #print(json.dumps(test.test_data_all, indent=4, ensure_ascii=False))
    print('*' * 200)
    print(json.dumps(test.get_every_TestCaseFlag(), indent=4, ensure_ascii=False))
