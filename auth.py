# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
# from model import db, User

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():#get_json(): 这是 request 对象的一个方法，用于解析请求体中的 JSON 数据，并将其转换为 Python 字典（dict）或列表（list）。
#     data = request.get_json()#request: 这是 Flask 提供的一个全局对象，表示当前 HTTP 请求。
#     username = data.get('username')
#     password = data.get('password')
#     if User.query.filter_by(username=username).first():
#         return jsonify({"message": "User already exists"}), 400
#     user = User(username=username)
#     user.set_password(password)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"message": "User registered successfully"}), 201
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     user=User.query.filter_by(username=username).first()
#     if not user or not user.check_password(password):
#         return jsonify({"message": "Invalid credentials"}), 401
#     access_token=create_access_token(identity=username)
#     return jsonify({"access_token":access_token})
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from model import db, User
#蓝图作为一个框架，你可以通过这个变量来注册路由、模板等。
#Blueprint 是一种用于组织和管理应用程序路由、模板、静态文件等的方式。它允许你将应用程序拆分为多个模块，从而使代码更易于维护和扩展。
auth_bp=Blueprint('auth',__name__)#'auth': 这是蓝图的名称，__name__: 这是蓝图的导入名称，通常传入 __name__，表示当前模块的名称。
@auth_bp.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')
    if User.query.filter_by(username=username).first():#filter_by(username=username) 是一个过滤条件，
        #User 是一个 SQLAlchemy 模型类，表示数据库中的用户表。query 是 SQLAlchemy 提供的查询接口，用于对数据库进行查询。
        #jsonify() 是 Flask 提供的一个函数，用于将 Python 字典转换为 JSON 格式的 HTTP 响应。400 是 HTTP 状态码，
        return jsonify({"message": "User already exists"}), 400
    user=User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}),201
@auth_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')
    user=User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401
    access_token=create_access_token(identity=username)
    return jsonify({"access_token":access_token})