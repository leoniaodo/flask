import requests

# 登录的 URL
url = "http://127.0.0.1:5000/auth/login"

# 提供的用户名和密码
data = {"username": "testuser", "password": "123456"}

# 发送 POST 请求进行登录
response = requests.post(url, json=data)

# 打印响应状态码和返回的内容
print("状态码:", response.status_code)
print("返回数据:", response.text)
