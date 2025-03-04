import os #os: 这是 Python 的标准库模块，用于与操作系统交互。在这里，它可能用于读取环境变量或处理文件路径。
class Config:#Config: 这是一个配置类，用于存储 Flask 应用程序的配置项。通过将配置集中在一个类中，可以更方便地管理和维护。
    SECRET_KEY = "your_secret_key"#SECRET_KEY: 这是 Flask 应用程序的密钥，用于加密会话数据、生成 CSRF 令牌等。
    #sqlite:///users.db 表示使用 SQLite 数据库，数据库文件名为 users.db，存储在当前工作目录中。
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@localhost/flask_auth_db"#SQLALCHEMY_DATABASE_URI: 这是 SQLAlchemy 的配置项，用于指定数据库的连接 URI。
    SQLALCHEMY_TRACK_MODIFICATIONS = False#SQLALCHEMY_TRACK_MODIFICATIONS: 这是 SQLAlchemy 的配置项，用于禁用对象修改跟踪。
    #如果设置为 True，SQLAlchemy 会跟踪对象的修改并发出信号。这会导致额外的性能开销，通常不需要启用。
