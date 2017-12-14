
DEBUG = True

SECRET_KEY ='you-will-never-guess'

SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:yoenchen@127.0.0.1:3306/flaskr'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True



SQLALCHEMY_TRACK_MODIFICATIONS = True

