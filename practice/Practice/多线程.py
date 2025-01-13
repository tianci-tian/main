
from threading import Thread

def worker(money):
    print("开始干活")
    print(f"拿到{money}块工资")

# 通过target指定线程具体执行的工作-传入对应函数，args参数执行传入函数的参数，需要注意这里是元组类型的
#例如 (100) 这样的写法，Python 会认为它就是值 100 本身（比如用于数学运算表达式等场景中），
# 而 (100,) 才明确表示是一个元组，里面有一个元素 100。所以当给 Thread 类构造函数的 args 参数传递单个值给目标函数时，
# 也要写成这样符合元组语法的形式，来确保传递的是作为一个参数元组对象，而不是被错误解析。
thread = Thread(target=worker,args=(100,))
# 启动线程
thread.start()
# 等待线程执行结束
thread.join()