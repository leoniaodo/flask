import sys
import requests
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
# Flask 服务器地址
BASE_URL = "http://127.0.0.1:5000/auth"
class ShopWindow(QDialog):
    def __init__(self):
        super(ShopWindow, self).__init__()
        loadUi("movie.ui", self)  # 载入 Qt 设计的 UI
class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)  # 加载 Qt Designer 设计的 UI
    # 绑定按钮事件
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.register)
    def login(self):
        username =self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            print("请输入用户名和密码")
            return
        response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
            token = response.json().get("access_token")
            print(f"登录成功！Token: {token}")
            # **登录成功后，跳转到购物页面**
            self.shop_window = ShopWindow()
            self.shop_window.show()
            self.close()  # 关闭登录窗口
        else:
            print("登录失败，用户名或密码错误")
    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            print("请输入用户名和密码")
            return

        response = requests.post(f"{BASE_URL}/register", json={"username": username, "password": password})
        if response.status_code == 201:
            print("注册成功！请登录")
        else:
            print("注册失败，用户名已存在")
if __name__ == '__main__':
    app = QApplication(sys.argv)#创建 QApplication 对象，负责 管理整个应用程序的事件循环，比如处理用户的点击、输入等。
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())#app.exec_() 启动 Qt 事件循环（Event Loop），程序会一直运行，直到窗口关闭。sys.exit() 确保程序优雅退出，避免资源泄漏。