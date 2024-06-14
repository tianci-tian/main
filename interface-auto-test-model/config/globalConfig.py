#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 9:27
# @Author  : 朱宽
# @File    : globalConfig.py
# @Software: Win10、Python3.8.5 and Pycharm
'''
定义一些配置信息，例如：文件路径、数据库信息、账户密码等
'''
import os

# 获取当前项目根目录文件夹绝对路径（即项目名称在系统中的路径）
project_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_directory_path)

# 测试数据存储位置
test_data_path = project_directory_path + '/testdata/'
# print(test_data_path)

# 日志文件存储位置
test_log_path = project_directory_path + '/log/'
# print(test_log_path)

# 测试报告存储位置
test_report_path = project_directory_path + '/testreport/'
# print(test_report_path)

# 测试脚本位置
test_script_path=project_directory_path + '/src/script/'
print(test_script_path)
# http请求地址、端口
'''
    1、当 http_host 开头为[a-zA-Z]时，代码会自动忽略http_port，直接使用http_protocol和http_host构建URL头部。
    2、当 http_host 开头为[0-9]时，代码会使用 http_protocol、http_host、http_port 构建URL头部。
'''
http_host = 'tujunsat.jimicloud.com'
#http_host = '172.26.10.113'
http_port = '9080'
http_protocol = 'http'

# Mysql数据库相关信息
mysql_host = '172.26.10.45'
mysql_port = 3306
mysql_user = 'root'
mysql_pw = '123456'
mysql_db = 'console_tenancy'

# Mongo数据库相关信息


# Redis数据库相关信息
redis_host = '172.26.10.113'
redis_port = 6379
redis_user = None
redis_password = 'jimi@123'
redis_db = 4  # redis的数据库中 第N库 设置应使用数字标记为第几个

# Cassandra数据库相关信息
cassandra_contact_points = ['172.16.10.113']  # Cassandra集群IP，列表形式存储
cassandra_port = 9042
cassandra_user = 'root'
cassandra_pw = 'tracker@cassandra'

# 钉钉机器人连接
ding_url='https://oapi.dingtalk.com/robot/send?access_token=d827fa540b78c0192fd6ed11cfa7132d6fc1d1947e362a61491186a52cf83620'

# 自动化测试代码存放的   服务器IP  /  端口  /   nginx配置的uri（就是：report124）
auto_test_server_host_url_head='http://heytrack.i-jimi.com.cn/report124/'

if __name__=='__main__':
    pass