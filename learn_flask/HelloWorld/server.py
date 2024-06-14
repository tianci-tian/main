from flask import Flask, request
# Flask不允许返回None,出现500错误
# 解决方法很简单，1、先判断下它是不是None  2、设置默认值，也就是取不到数据时用这个值
app = Flask(__name__)

# 变量app是一个Flask实例,当客户端访问/时，将响应hello_world()函数返回的内容
# Hello World!只是HTTP响应报文的实体部分，状态码等信息既可以由Flask自动处理，也可以通过编程来制定。
@app.route('/')
def hello_world():
    # 浏览器传给我们的Flask服务的数据长什么样子呢？可以通过request.full_path和request.path来看一下：
    print(request.path)
    print(request.full_path)
    # return request.args.__str__()

    # 要获取键info对应的值
    # return request.args.get('info')
    # 函数request.args.get的第二个参数用来设置默认值return request.args.get('info','HelloWorld')
    # 先判断下它是不是None
    r = request.args.get('info')
    if r == None:
        # do something
        return '输入错误'
    return r

if __name__ == '__main__':
    app.run(port=5000, debug=True)