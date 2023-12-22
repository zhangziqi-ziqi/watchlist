from flask import Flask # 从flask包导入flask类
from flask import url_for
from markupsafe import escape

app = Flask(__name__) #实例化flask创建一个程序对象app

@app.route('/')
def hello():
    return 'Hello'
@app.route('/user/<name>') #q1:name变量从输入网址中读入#装饰器，绑定url，用户访问该url会触发该函数hello(),将返回值显示到窗口
def user_page(name):
    return f'<h1>Welcome to My Watchlist!{escape(name)}</h1><img src="http://helloflask.com/totoro.gif">'#以HTML、格式解析
#补充：程序发现机制 $ export FLASK_APP=hello.py  > set FLASK_APP=hello.py
#开启调试模式(env) $ flask run --debug

@app.route('/test')
def test_url_for():
    #print 函数的 返回值均在命令行查看
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'test'
