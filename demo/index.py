# coding:utf-8
from flask import Flask
import flask
import config

from exts import db

from models import Role,Articles

web = Flask(__name__)
web.config.from_object(config)


db.init_app(web)





@web.route('/')
def index():

  


  return('项目结构已经搭建好了！')


@web.route('/login')
def login00():
	return('这是登录界面!')

if __name__ == '__main__':
    web.run()