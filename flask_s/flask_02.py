"""
作者   ：bjx
创建时间   ：2020/12/19  12:30 上午 
文件名称   ：flask_02.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask import Flask,make_response,request
app = Flask(__name__)

@app.route('/<name>')
def set(name):
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','baijinxing')
    return '<h1>hello,%s</h1>'%name

if __name__ == "__main__":
    app.run(debug=True)