import time
#需要在所有这样的函数 返回字符串前面 都加上开头: 当地时间
# 完全可以 不去修改原来的函数 ，使用装饰器
# 装饰器经常被用在库和框架中， 给别的开发者使用  把增强的部分做在 装饰器函数中


# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper

@sayLocal    #语法糖，便捷写法  就等于执行了这样的一条语句：
                             #getXXXTime = sayLocal(getXXXTime)
def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())

# 装饰 getXXXTime

print (getXXXTime())








