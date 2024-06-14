# -*- coding: utf-8 -*-
# @Project : 数据库插入子账户脚本
# @File    : MysqlUtils.py
# @Author  : 朱宽
# @Time    : 2021/3/16 17:36
# @Software: Win10 / Python3 / Pycharm

# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

import pymysql
from config import globalConfig
from loguru import logger


class HandleMySql():
    '''
    <--MySQL数据库处理类-->

    类内函数如下：
        1、初始化数据库相关参数
        2、连接数据库
        3、查询数据
        4、插入数据
        5、删除数据
        6、更新数据
        7、关闭相关连接
    '''

    def __init__(self):
        '''
        1、初始化数据库相关参数

        '''
        self.host = globalConfig.mysql_host  # 数据库主机地址
        self.port = globalConfig.mysql_port  # 数据库对应服务端口
        self.user = globalConfig.mysql_user  # 数据库登录用户名
        self.password = globalConfig.mysql_pw  # 数据库登录密码
        self.db = globalConfig.mysql_db  # 数据库分库名称

        self.conn, self.cursor = self.connect_mysql()  # 连接数据库，返回链接 和 操作游标，并将其类内全局化

    def connect_mysql(self):
        '''
        2、连接数据库

        :return:
        '''
        try:
            # 连接数据库
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                   password=self.password, db=self.db, charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

            # 使用该连接创建并返回游标
            cursor = conn.cursor()

            # 打印日志
            logger.info(
                'Mysql数据库{}:{}/{}----连接成功'.format(globalConfig.mysql_host , globalConfig.mysql_port , globalConfig.mysql_db))

            return conn, cursor

        except Exception as e:
            logger.error('Mysql数据库--连接失败，错误信息%s' % e)

    def select(self, sql, args=None):
        '''
        3、查询数据
        :param sql: sql查询语句；'select * from tenancy_tenant where username = %s'
        :param args: 其他参数；('zktest')，元组形式
        :return: 返回结果集；

                    结果集数据结构为：

                                1、结果返回为空时，使用元组结构。()

                                2、结果返回不为空时，使用列表内嵌字典的结构。[{结果1},{结果2},{结果3}]

        '''
        self.cursor.execute(sql, args)  # 执行一个数据库的相关命令
        self.conn.commit()  # 提交当前事务
        logger.info('查询数据库成功')

        return self.cursor.fetchmany(size=self.cursor.rowcount)  # fetchmany(size):获取结果集的下几行；rowcount()：返回数据条数或影响行数

    def insert(self, sql, args=None):
        '''
        4、插入数据
        :param sql: sql查询语句
        :param args: 其他参数
        :return:
        '''
        self.cursor.execute(sql, args)  # 执行一个数据库的相关命令
        self.conn.commit()  # 提交当前事务
        logger.info('成功插入数据')

    def delete(self, sql, args=None):
        '''
        5、删除数据
        :param sql: sql查询语句
        :param args: 其他参数
        :return:
        '''
        self.cursor.execute(sql, args)  # 执行一个数据库的相关命令
        self.conn.commit()  # 提交当前事务
        logger.info('成功删除数据')

    def update(self, sql, args=None):
        '''
        6、更新数据
        :param sql: sql查询语句
        :param args: 其他参数
        :return:
        '''
        self.cursor.execute(sql, args)  # 执行一个数据库的相关命令
        self.conn.commit()  # 提交当前事务
        logger.info('成功更新数据')

    def close(self):
        '''
        7、关闭相关连接
        :return:
        '''
        self.cursor.close()  # 关闭游标对象
        self.conn.close()  # 关闭连接
        logger.info(
            'Mysql数据库{}:{}/{}----关闭连接'.format(globalConfig.mysql_host , globalConfig.mysql_port , globalConfig.mysql_db))


if __name__ == '__main__':
    from pprint import pprint

    mysql_handle = HandleMySql()
    sql = 'select * from tenancy_tenant where username = %s'
    value = ('zktest')
    select_data = mysql_handle.select(sql, value)
    print(type(select_data))
    print(type(select_data[0]))
    pprint(select_data)
    mysql_handle.close()
