import requests

url = "http://127.0.0.1:5000/auth/register"
data = {"username": "testuser", "password": "123456"}

response = requests.post(url, json=data)

print("状态码:", response.status_code)  # 打印 HTTP 状态码
print("返回数据:", response.text)  # 打印返回的 JSON 数据
