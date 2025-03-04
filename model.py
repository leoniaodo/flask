# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# db = SQLAlchemy()  # 这里要正确初始化 SQLAlchemy

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(200), nullable=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
db=SQLAlchemy()
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password_hash=db.Column(db.String(200),nullable=False)
    def set_password(self, password):#作用：使用 Werkzeug 库对密码进行哈希加密。加密方式：默认使用 PBKDF2 进行哈希，生成一个不可逆的密码哈希值。
        self.password_hash=generate_password_hash(password)#123456加密为pbkdf2:sha256:260000$k84JnA6D$21a3f913...
    def check_password(self, password):#用 check_password_hash(存储的哈希, 用户输入的密码) 进行比对,如果匹配，返回 True，否则返回 False
        return check_password_hash(self.password_hash, password)
