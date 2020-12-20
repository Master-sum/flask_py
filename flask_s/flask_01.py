"""
作者   ：bjx
创建时间   ：2020/12/19  12:08 上午 
文件名称   ：flask_01.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask import Flask,request,abort,redirect,url_for
from flask import Flask,make_response
import time
app = Flask(__name__)
@app.route('/h')
def hello():
    name = request.args.get('name','Flask')
    return '<h1>hello,%s</h1>'%name

@app.route('/do/<int:year>')
def go_d(year):

    return '<h1>hello,%d</h1>'%(time.time())
@app.route('/set/<name>')
def set(name):
    response = make_response(redirect(url_for('h')))
    response.set('name',name)
    return response
@app.route('/404')
def not_f():
    abort(404)
if __name__ == "__main__":
    app.run(debug=True)