"""
作者   ：bjx
创建时间   ：2020/12/20  1:09 下午 
文件名称   ：flask_03.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask import Flask,session,redirect,url_for,g,request
app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'
@app.route('/hello')
def hello():

    return '<h1>hello,</h1>'
@app.route('/login')
def login():
    session['login_in'] = True#写入session
    return redirect(url_for('hello'))

@app.before_request
def get_name():
    g.name = request.args.get('name')

if __name__ == "__main__":
    app.run()