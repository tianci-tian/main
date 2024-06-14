# -*- coding: utf-8 -*-
# @Project : 数据库插入子账户脚本
# @File    : RedisUtils.py
# @Author  : 朱宽
# @Time    : 2021/3/18 17:01
# @Software: Win10 / Python3 / Pycharm

# '''
#     命令行执行某python文件时
#     用于将项目的路径添加到临时空间中（即工作目录），便于寻找该项目下的其他模块
# '''
# import sys
# import os
# item_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(item_path)

import redis
from config import globalConfig
from loguru import logger


class HandleRedis():
    '''
    <--Redis数据库处理类-->
    '''

    def __init__(self):
        '''
        1、初始化
        '''
        self.redis_host = globalConfig.redis_host
        self.redis_port = globalConfig.redis_port
        self.redis_password = globalConfig.redis_password
        self.redis_db = globalConfig.redis_db

        self.pool = self.connect_redis_connection_pool()


    def connect_redis_connection_pool(self):
        '''
        2、连接redis数据库;

           redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作;

           如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，
           并且默认情况下一次pipline 是原子性操作。(要与 连接池 ConnectionPool 搭配使用)

           管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。
           它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。
           (要与 连接池 ConnectionPool 搭配使用)

        :return:
        '''
        try:
            pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, password=self.redis_password,
                                        db=self.redis_db, decode_responses=True)  # decode_responses=True 自动解码
            logger.info('Redis数据库{}:{}/{}----连接池创建成功'.format(
                globalConfig.redis_host , globalConfig.redis_port ,
                globalConfig.redis_db))

            return pool

        except Exception as e:
            logger.error('Redis数据库----连接失败，错误信息%s' % e)

    def string_insert_update_set(self, name, value, ex=None, px=None, nx=False, xx=False):
        '''
        3、在Redis中设置String类型的值。默认，不存在则创建，存在则修改。
        :param name:键名
        :param value:键值
        :param ex:过期时间（秒）。设置过期时间N秒，并设置了value值，N秒后，键值就变成None。
        :param px:过期时间（毫秒）。设置过期时间M毫秒，并设置了value值，M毫秒后，键值就变成None。
        :param nx:如果设置为True，则只有name不存在时，当前set操作才执行 （新建）。
        :param xx:如果设置为True，则只有name存在时，当前set操作才执行 （修改）。
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result = connect.set(name=name, value=value, ex=ex, px=px, nx=nx, xx=xx)  # 调用set方法，写入string型数据

        if result == True:
            logger.info('string_insert_update_set：插入或更新数据成功')
        else:
            logger.info('string_insert_update_set：插入或更新数据失败')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def string_insert_setnx(self,name,value):
        '''
        4、在redis中设置string类型的值，只有name不存在时，执行设置操作（添加）
        :param name:键名
        :param value:键值
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool) # 在连接池中创建一个连接
        result=connect.setnx(name=name,value=value)

        if result==True:
            logger.info('string_insert_setnx：插入数据成功')
        else:
            logger.info('string_insert_setnx：插入数据失败')
        self.close(connect) # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def string_insert_short_s_setex(self,name, value, time):
        '''
        5、将 name-value 这一对键值变更为临时变量，经过time秒后，自动删除。
           不论 name-value 这一对键值是否已经存在于redis数据库。
                 如果存在，则修改value，并于time秒后，删除。
                 如果不存在，则插入 name-value，并于time秒后，删除。
        :param name: 键名
        :param value: 键值
        :param time: 过期时间，单位-秒
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.setex(name=name, value=value, time=time)
        logger.info('string_insert_short_s_setex：插入数据成功，{}秒后删除'.format(time))
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def string_insert_short_ms_psetex(self,name,value,time_ms):
        '''

        :param name:
        :param value:
        :param time_ms:
        :return:
        '''

        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.psetex(name=name,value=value,time_ms=time_ms)
        logger.info('string_insert_short_ms_psetex：插入数据成功，{}毫秒后删除'.format(time_ms))
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def string_select_get(self,name):
        '''

        :param name:
        :param value:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.get(name=name)
        logger.info('string_select_get：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def string_delete(self,name):
        '''

        :param name:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.delete(name)
        logger.info('string_delete：删除成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def string_insert_mget(self,keys, *args):
        '''
        批量获取string类型的数据
        :param keys:
        :param args:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.mget(keys, *args)
        logger.info('string_insert_mget：批量查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_insert_update_hset(self,name,key,value):
        '''
        单个增加hash类型数值--修改(单个取出)--没有就新增，有的话就修改
        :param name:
        :param key:
        :param value:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.hset(name=name,key=key,value=value)
        logger.info('hash_insert_update_hset：插入或修改成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def hash_insert_hsetnx(self,name,key,value):
        '''
        单个新建hash类型数值
        :param name:
        :param key:
        :param value:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.hsetnx(name=name,key=key,value=value)
        logger.info('hash_insert_hsetnx：插入成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def hash_select_hget(self,name,key):
        '''
        单个取hash的key对应的值
        :param name:
        :param key:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.hget(name=name,key=key)
        logger.info('hash_select_hget：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_select_hkeys(self,name):
        '''
         取hash中name对用的所有key
        :param name:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.hkeys(name=name)
        logger.info('hash_select_hkeys：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_insert_hmset(self,name,mapping):
        '''
        在name对应的hash中批量设置键值对
        :param name:
        :param mapping:字典形式传入
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.hmset(name=name,mapping=mapping)
        logger.info('hash_insert_hmset：批量插入成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def hash_select_hgetall(self,name):
        '''
        获取name对应hash的所有键值
        :param name:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.hgetall(name=name)
        logger.info('hash_select_hgetall：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_select_hvals(self,name):
        '''
        获取name对应的hash中所有的value的值
        :param name: hash 键名
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.hvals(name=name)
        logger.info('hash_select_hvals：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_judge_hexists(self,name,key):
        '''
        判断成员是否存在（类似字典的in）
        :param name:
        :param key:
        :return:  False 不存在 ；True 存在；
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.hexists(name=name,key=key)
        logger.info('hash_judge_hexists：查询成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def hash_delete_hdel(self,name,*keys):
        '''
        将name对应的hash中指定key的键值对删除
        :param name:
        :param keys:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.hdel(name,*keys)
        logger.info('hash_delete_hdel：删除成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_insert_lpush(self,name,*values):
        '''
        在name对应的list中添加元素，每个新的元素都添加到列表的最左边;没有就新建
        :param name:
        :param values:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.lpush(name,*values)
        logger.info('list_insert_lpush：向左插入成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_insert_rpush(self,name,*values):
        '''
        在列表的右边，依次添加44,55,66  (*values);没有就新建
        :param name:
        :param values:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.rpush(name,*values)
        logger.info('list_insert_rpush：向右插入成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_insert_linsert(self,name, where, refvalue, value):
        '''
        固定索引号位置插入元素
        :param name:
        :param where:
        :param refvalue:
        :param value:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.linsert(name, where, refvalue, value)
        logger.info('list_insert_linsert：固定索引号位置插入元素成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_update_lset(self,name, index, value):
        '''
        对name对应的list中的某一个索引位置重新赋值
        :param name:redis的name
        :param index:list的索引位置
        :param value:要设置的值
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.lset(name, index, value)
        logger.info('list_update_lset：修改指定索引号的value值成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_delete_lrem(self,name, value, num):
        '''
        在name对应的list中删除指定的值
        :param name:redis的name
        :param value:要删除的值
        :param num:
                                num=0，删除列表中所有的指定值；
                                num=2,从前到后，删除2个； num=1,从前到后，删除左边第1个
                                num=-2,从后向前，删除2个
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        connect.lrem(name, value, num)
        logger.info('list_delete_lrem：删除指定值成功')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。

    def list_select_lindex(self,name, index):
        '''
        在name对应的列表中根据索引获取列表元素
        :param name:
        :param index:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.lindex(name, index)
        logger.info('list_select_lindex：成功查询指定索引号的值')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def list_select_lrange(self,name,start,end):
        '''
        切片取出值，范围是索引号 start-end
        :param name:
        :param start:
        :param end:
        :return:
        '''
        connect = redis.StrictRedis(connection_pool=self.pool)  # 在连接池中创建一个连接
        result=connect.lrange(name,start,end)
        logger.info('list_select_lrange：成功查询指定索引范围的值')
        self.close(connect)  # 关闭该连接；释放内存，防止redis内存资源耗尽，导致宕机。
        return result

    def close(self, connect):
        '''
        关闭一个连接，释放内存。防止redis内存资源耗尽，导致宕机。
        :param connect:
        :return:
        '''
        connect.connection_pool.disconnect()
        logger.info(
            '{}----关闭该连接'.format(connect))


if __name__ == "__main__":
    test_class = HandleRedis()
    test_class.string_insert_update_set(name='zk', value='Zhu Kuan')
    #test_class.string_insert_setnx(name='zk2', value='Zhu Kuan 2')
    test_class.string_insert_short_s_setex(name='zk2', value='临时数据',time=20)
    test_class.string_select_get(name='zk')
    #test_class.string_insert_update_set(name='delete', value='Zhu Kuan')
    test_class.string_delete('delete')
    test_class.hash_delete_hdel('USER_RELATION_ANALYSE','201820182795697','201820191664751')



