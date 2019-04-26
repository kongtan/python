from flask import Flask
from flask import make_response
import json
from templates import douban
from templates import bee

app = Flask(__name__)

a = json.dumps({
    "a": '''<p onclick="alert(window.cookie)">111</p>
               <a href="https://www.baidu.com">超链接</a>'''
})


# 默认端口
@app.route('/')
def defaule():
    rst = make_response(a)
    return rst


# 豆瓣
@app.route('/douban')
def douban():
    rst = make_response(douban.getDouBanReMen())
    # rst = make_response(a)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    # rst.headers['Access-Control-Allow-Credentials'] = True
    return rst


# 蜜蜂电影
@app.route('/bee')
def beeMovie():
    rst = make_response(bee.getMovie())
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst;


if __name__ == '__main__':
    app.run(debug=True, port='5052', host='0.0.0.0')
