#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 18:22
# @Author  : 朱宽
# @File    : GetLog.py
# @Software: Win10、Python3.8.5 and Pycharm

'''
生成日志，
调用方法为：

from public.LogHandle import GetLog

testlogger = GetLog.Logger('Test_Advanced_Application').getlog()#Test_Advanced_Application  为要测试的文件，不同文件只需要更新这个就好了。

testlogger.info("打开这个浏览器")
# '''
#
# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

import time
import logging
from config.globalConfig import test_log_path


class Logger():

    def __init__(self, name):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件将日志存入指定的文件中
        :param logger:
        '''
        # 创建一个logger
        self.logger = logging.getLogger(name=name) #初始化
        self.logger.setLevel(logging.DEBUG) #设置用例等级，低于该级别的日志消息将会被忽略

        # 创建一个handler，用于写入日志文件
        rp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) #获取当前时间，用于日志名称命名
        log_path = test_log_path # 获取存储日志文件的位置
        log_name = log_path + rp + '.log' # 按时间组装日志文件
        print('打印位置：GetLog.py--37行\n生成日志目录：',log_name)
        filehandler = logging.FileHandler(log_name)
        filehandler.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        filehandler.setFormatter(formatter)
        consolehandler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(consolehandler)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    import sys
    import os

    #sys.argv[0]获取文件绝对路径；os.path.basename获取纯文件名；
    current_file_name = os.path.basename(sys.argv[0])
    testLogger = Logger(current_file_name).getlog()
    testLogger.info('测试')


