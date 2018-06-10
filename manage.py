from flask import Flask
from db import db
from src.contorller import indexs

app = Flask(__name__)
app.register_blueprint(indexs) ##注册蓝图
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/ronxinyuan?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db.init_app(app)

if __name__ == '__main__': ##初始化flask中的web服务器，一般用于测试使用
    app.run()