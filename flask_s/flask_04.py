"""
作者   ：bjx
创建时间   ：2020/12/20  3:15 下午 
文件名称   ：flask04.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask import Flask,url_for,redirect,request,render_template
from jinja2.utils import generate_lorem_ipsum
from jinja2 import escape
app = Flask(__name__)
@app.route('/foo')
def foo():
    return '<h1> foo page</h1><a href="%s">Do something</a>'%url_for('do_s')

@app.route('/bar')
def bar():
    return '<h1> bar page</h1><a href="%s">Do something and rr</a>'%url_for('do_s',next = request.full_path)
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return '<h1>hello,%s</h1>'%escape(name)

@app.route('/do_s')
def do_s():
    return redirect(request.referrer or url_for('hello'))
@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)

@app.route('/')
def index():
    return render_template('test01.html')
if __name__ == "__main__":
    app.run(debug=True)

