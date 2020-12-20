"""
作者   ：bjx
创建时间   ：2020/12/4  11:34 下午 
文件名称   ：run.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
from app import create_app
app = create_app()
if __name__ == "__main__":
    app.run()