# -*- coding: utf-8 -*-
# @Project : APITestModel
# @File    : Mock.py
# @Author  : 朱宽
# @Time    : 2021/4/1 15:53
# @Software: Win10 / Python3 / Pycharm

# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

from unittest import mock


class Mock():
    '''
    mock模块的封装
    '''

    def mock(self, data):
        '''
        模拟调用功能
        :param data: 传入测试数据
        :return:返回结果
        '''
        method = data['Method'].lower()  # 请求方式
        uri = data['Uri']  # uri，此处省略ip的添加
        send_data = data['SendData']  # 发送数据
        header = {'Content-Type': data['Content-Type']}  # http数据包头部构建
        mock_return_data = data['MockData']  # mock返回的数据

        mock_method = mock.Mock(return_value=mock_return_data)
        result = mock_method(method, uri, send_data, header)

        return result


if __name__ == "__main__":
    data = {'TestCaseFlag': 'delete_wifigroup', 'CorrectFlag': None, 'Method': 'delete', 'Uri': '/api/config/wifiGroup',
            'Content-Type': 'multipart/form-data',
            'SendData': {'requestId': 'test', 'imei': '202011110000000', 'd': '555', 'appId': 'TUQIANG'},
            'AssertInfo': {'code': 100000, 'msg': '成功'}, 'CaseDescription': '考勤点-删除Wifi分组', 'Rely': 'no',
            'Extract': None, 'MockFlag': None, 'MockData': {'code': 100000, 'msg': '成功'}}
    test = Mock()
    result = test.mock(data=data)
    print(result)
