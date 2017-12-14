
# script  通过命令行操作flask

from flask_script import Manager
from index import web

manager = Manager(web)

#和数据库相关的操作，我都放在一起
@manager.command
def runserver():
	print('服务器跑起来了')


if __name__ == '__main__':
	manager.run()


'''from exts import db
from flask13_demo import app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
#导入数据模型
import models

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()'''