from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from model import db
from auth import auth_bp
app=Flask(__name__)
app.config.from_object(Config)
#@app.route() 是 Flask 的路由装饰器，用于将 URL 规则与视图函数绑定。
@app.route('/')  # 处理访问 http://127.0.0.1:5000/ 的请求,Flask 应用程序默认运行在 http://127.0.0.1:5000
def home():#当用户访问根路径 / 时，Flask 会调用 home() 函数，并返回 "Hello, Flask!" 作为响应。
    return "Hello, Flask!"

db.init_app(app)#这行代码的作用是将 Flask 应用程序实例 (app) 与 SQLAlchemy 数据库实例 (db) 绑定。
jwt=JWTManager(app)#这是 Flask-JWT-Extended 提供的类，用于管理 JWT（JSON Web Token）的创建、验证和解析。
app.register_blueprint(auth_bp,url_prefix='/auth')
if __name__=='__main__':
    with app.app_context():#Flask 应用程序上下文是一个运行时环境，允许访问 Flask 应用程序的配置、数据库连接等。
        db.create_all()#with 语句用于创建一个上下文管理器，确保在代码块执行完毕后自动清理资源。
    app.run(debug=True)