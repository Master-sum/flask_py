"""
作者   ：bjx
创建时间   ：2020/12/20  11:46 下午 
文件名称   ：flask_05.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask import Flask,url_for,redirect,request,render_template
app = Flask(__name__)

@app.route('/index/<name>')
def index(name):
    return render_template('index.html',name=name)

if __name__ == "__main__":
    app.run(debug=True)
