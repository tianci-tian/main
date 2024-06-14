# -*- coding: utf-8 -*-
# @Project : 数据库插入子账户脚本
# @File    : CassandraUtils.py
# @Author  : 朱宽
# @Time    : 2021/3/18 15:11
# @Software: Win10 / Python3 / Pycharm
# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

from config import globalConfig

# 引入Cluster模块
from cassandra.cluster import Cluster
# 引入DCAwareRoundRobinPolicy模块，可用來自定义驱动程序的行为
# from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
from loguru import logger




class HandleCassandra():
    '''
    <--操作Cassandra数据库-->

    类内函数如下：

        1、初始化数据库集群相关信息
        2、连接数据库集群
        3、查询数据
        4、插入数据
        5、更新数据
        6、删除数据
        7、关闭连接
    '''

    def __init__(self):
        '''
        1、初始化数据库集群相关信息
        '''
        self.contact_points = globalConfig.cassandra_contact_points  # Cassandra数据库集群的IP
        self.port = globalConfig.cassandra_port  # 集群对应服务端口
        self.username = globalConfig.cassandra_user  # 集群登录用户名
        self.password = globalConfig.cassandra_pw  # 集群登录密码

        # 配置登录Cassandra集群的账号和密码
        self.auth_provider = PlainTextAuthProvider(username=self.username, password=self.password)

        # 连接Cassandra集群，并将cluster和 会话 全局化
        self.cluster, self.session = self.connect_cassandra()

    def connect_cassandra(self):
        '''
        2、连接数据库集群
        :return:
        '''
        try:
            # 创建一个Cassandra的cluster
            cluster = Cluster(contact_points=self.contact_points, auth_provider=self.auth_provider)
            # 连接并创建一个会话
            session = cluster.connect()

            # 打印日志
            logger.info(
                'Cassandra数据库集群{}-{}----连接成功'.format(globalConfig.cassandra_contact_points , globalConfig.cassandra_port))

            return cluster, session
        except Exception as e:
            logger.error('Cassandra数据库集群--连接失败，错误信息%s' % e)

    def select(self, cql, args=None):
        '''
        3、查询数据
        :param cql:cql语句："select * from tracker.gps_his where device_imei=%s and gps_time=%s"；
                            "tracker.gps_his"其中tracker为keyspace，gps_his为表名；
        :param args:%s对应的参数；(value1,value2),[value1,value2];使用元组或者列表传递参数

        :return:返回一个列表结果：[<class 'cassandra.io.asyncorereactor.Row'>,<class 'cassandra.io.asyncorereactor.Row'>]

                获取 数据类型 <class 'cassandra.io.asyncorereactor.Row'> 中的指定字段的信息

                result = rows._current_rows
                # Row(device_imei='200000000003679', gps_time=datetime.datetime(2020, 10, 23, 2, 34, 7, 873000), acc=1)

                方法如下：
                    1、 Rows[n].device_imei    ----》 200000000003679 ；后面加 ".字段名"
                    2、 Rows[n][0]             ----》 200000000003679 ；使用列表、元组等取值方式；还可求其长度 len(Rows[n])
        '''
        rows = self.session.execute(cql, parameters=args)
        result = rows._current_rows

        logger.info('查询数据成功')
        return result

    def insert(self, cql, args=None):
        '''
        4、插入数据
        :param cql:
        :param args:
        :return:
        '''
        self.session.execute(cql, parameters=args)
        logger.info('插入数据成功')

    def update(self, cql, args=None):
        '''
        5、更新数据
        :param cql:
        :param args:
        :return:
        '''
        self.session.execute(cql, parameters=args)
        logger.info('更新数据成功')

    def delete(self, cql, args=None):
        '''
        6、删除数据
        :param cql:
        :param args:
        :return:
        '''
        rows = self.session.execute(cql, parameters=args)
        result = rows._current_rows

        logger.info('删除数据成功')
        return result

    def close(self):
        '''
        7、关闭连接
        :return:
        '''
        self.session.shutdown()  # 关闭会话
        self.cluster.shutdown()  # 关闭连接
        logger.info(
            'Cassandra数据库集群{}-{}----关闭连接'.format(globalConfig.cassandra_contact_points , globalConfig.cassandra_port))


if __name__ == "__main__":
    import datetime
    import time

    test_class = HandleCassandra()
    select_cql = 'select * from tracker.gps_his where device_imei=%s and gps_time=%s'
    value = ('200000000003679', datetime.datetime(2020, 10, 23, 2, 34, 7, 873000))
    result = test_class.select(select_cql, value)
    test_class.close()
    time.sleep(0.1)
    print('', '-' * 150, '\n', '*' * 150, '\n', '-' * 150, '\n')
    print(result)
    print(type(result))
    print('gps_time:',result[0].gps_time)
