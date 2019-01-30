from flask import Flask, abort, redirect, g

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')

@app.route('/')
def hello_world():
    # 如果在视图函数执行过程中，出现了异常错误，我们可以使用abort函数立即终止视图函数的执行。通过abort函数，
    # 可以向前端返回一个http标准中存在的错误状态码，表示出现的错误信息。
    # 使用abort抛出一个http标准中不存在的自定义的状态码，没有实际意义。如果abort函数被触发，
    # 其后面的语句将不会执行。其类似于python中raise。执行abort后会去执行对应状态码的视图函数
    abort(500)
    return 'Hello World!'


@app.route('/user/<int:id>')
def get_one_user(id):
    # return后面可以自主定义状态码(即使这个状态码不存在)。当客户端的请求已经处理完成，
    # 由视图函数决定返回给客户端一个状态码，告知客户端这次请求的处理结果。
    print(id)
    return 'hello user= {}'.format(id), 500


@app.errorhandler(500)
def error_500_handler(e):
    return '哈哈哈500 e= {}'.format(e)


@app.errorhandler(404)
def error_404_handler(e):
    # 在Flask中通过装饰器来实现捕获异常，errorhandler()接收的参数为异常状态码。视图函数的参数，返回的是错误信息。
    return '您访问的页面不存在e= {}'.format(e)


@app.route('/redirect', endpoint='hahah')  # 如果不加endpoint那么endpoint默认=函数名
def redirect_baidu():
    from flask import url_for
    url = url_for('hahah')
    # 重定向
    return redirect('https://www.baidu.com')


@app.route('/set_cookie')
def set_cookie():
    # 创建response
    from flask import make_response
    my_response = make_response('set cookie')
    my_response.set_cookie('username', 'itcast')
    return my_response


@app.route('/get_cookie')
def get_cookie():
    from flask import request
    cookie_name = request.cookies.get('itcast')
    return 'cookie_name={}'.format(cookie_name)


@app.route('/response_body')
def return_response_body():
    from flask import request, jsonify, render_template, url_for, make_response
    # 响应体
    # return 'hahah'  # 返回字符串
    # return jsonify(dict(name='dashuiage'))  # 返回json字符串,其实执行jsonify()返回一个response对象
    # hh = render_template('hy.html')  # 返回模板，其实是一个字符串，render_template()将模板转换成了字符串
    # hh = redirect(url_for('hahah'))  # 重定向，redirect()返回一个response对象
    # return hh
    # 定制响应头
    response_obj = make_response(render_template('hy.html'))  # 参数str或response对象,或者不传。返回一个response对象，可以对其设置headers等等
    response_obj.headers['xxxx'] = 'hahahah'
    response_obj.set_cookie('123', '123')
    return response_obj


@app.route('/huanying')
def huanying():
    from flask import render_template
    return render_template('hy.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    from flask import render_template, request, url_for, session

    if request.method == 'POST':
        user_name = request.form.get('user', '')
        pwd = request.form.get('pwd', '')
        if user_name == '123' and pwd == '123':
            # 写入到session，然后加密后写入到cookie返回给浏览器如
            # cookie=session=eyJ1c2VyIjoiMTIzIn0.XEU5eg.DI3uLdKwuFT6YDz9lF8EzMPVSyk;....
            # 然后下次请时浏览器携带cookie到flask，flask解析cookie中的值，获取session然后解密封装成session对象
            session['user'] = user_name
            return redirect(url_for('huanying'))
    return render_template('login.html')


@app.route('/login_auth')
def login_auth():
    from flask import session, url_for
    if not session.get('user', ''):
        return redirect(url_for('login'))
    return redirect(url_for('huanying'))

# 登陆验证原理：1、当用户发送账号密码进行登陆时，从数据库进行账号密码验证，账号密码错误返回登陆界面。
# 账号密码验证ok设置session，session['user'] = user
# 2、然后对session进行加密以key-value形式存入cookie，响应给浏览器
# 3、下次访问时请求中携带cookie，flask取出session那部分key-value进行解密，封装成session对象
# 4、对session.get('user', '')进行验证

# # 登陆验证方式一
# @app.route('/look_data')
# def look_data():
#     from flask import session, url_for, render_template
#     user = session.get('user', '')
#     if user:
#         return render_template('login_after.html')
#     return redirect(url_for('login'))


# # 登陆验证方式二
# import functools
# from flask import session, redirect, url_for
#
#
# def my_login_auth(func):
#     @functools.wraps(func)  # 将inner函数名命名成func的名称
#     def inner(*args, **kwargs):
#         if not session.get('user', ''):
#             return redirect(url_for('login'))
#         return func(*args, **kwargs)
#     return inner
#
#
# @app.route('/look_data')
# @my_login_auth
# def look_data():
#     from flask import render_template
#     return render_template('login_after.html')

# 登陆验证方式三
from flask import request, redirect, url_for, session
@app.before_request
def my_login_auth():
    except_path = ['/login', '/favicon.ico', '/remove_cookie_session']
    if request.path in except_path:
        return None
    if not session.get('user'):
        return redirect(url_for('login'))
    return None


@app.route('/look_data')
def look_data():
    from flask import render_template
    return render_template('login_after.html')


@app.route('/remove_cookie_session')
def remove_cookie_session():
    """
    将登陆的存在cookie中的session清除
    :return:
    """
    from flask import request, make_response
    if request.cookies.get('session', ''):
        response_obj = make_response('删除cookie中的session')
        response_obj.delete_cookie('session')
        return response_obj  # 必须返回这个response，不然对response的所有设置无效
    return '还没有登陆过'


@app.route('/set_flash')
def set_flash():
    from flask import session, flash
    flash('12345678', 'myself')  # 其实是对session的操作
    flash('asdfg', 'myself')
    flash('zzzzz', 'hehe')
    return 'set flush'


@app.route('/get_from_flash')
def get_from_flash():
    """
    闪现，在session中存储一个数据，读取时通过pop将数据移除。
    :return:
    """
    from flask import session, flash, get_flashed_messages
    list_info = get_flashed_messages(category_filter=['myself', 'hehe'])
    return 'get from flash'


@app.route('/test_url_for/<int:nid>')
def test_url_for(nid):
    print(nid)
    return "zzzz"


@app.route('/test_url_for2')
def test_url_for2():
    url = url_for('test_url_for', nid=222)
    return redirect(url)


if __name__ == '__main__':
    app.run()
