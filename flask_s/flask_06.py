"""
作者   ：bjx
创建时间   ：2020/12/24  11:53 下午 
文件名称   ：flask_06.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from flask_s.forms import LoginForm,Text
from flask import Flask,render_template,flash,url_for,redirect
from flask_ckeditor import CKEditor

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config["SECRET_KEY"] = '79537d00f4834892986f09a100aa1edf'

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)

@app.route('/text',methods=['GET','POST'])
def text():
    form = Text()

    if form.validate_on_submit():

        if form.save.data:
            print(form.save.data)
            flash('hello')
        elif form.submit.data:
            flash('I am flash, who is looking for me?')

        #return redirect(url_for('login'))
    return render_template('submit.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)