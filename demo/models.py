#!/usr/bin/env python
# encoding: utf-8

from exts import db




class Articles(db.Model):
	__tablename__ = 'articles'
	id = db.Column(db.Integer,primary_key = True,autoincrement = True)
	title = db.Column(db.String(100),nullable = False)
	content = db.Column(db.Text)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'zeng'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    name = db.Column(db.String(64), unique=False,autoincrement = False)
    age = db.Column(db.String(64),nullable = False,autoincrement = False)
    




