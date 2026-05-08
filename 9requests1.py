#requests是Python和互联网之间的桥梁，爬虫、API调用、自动化都靠它
'''import requests
response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.text)'''
'''访问的网址
返回内容
普通网页（Google、百度）
HTML源代码
API接口
JSON数据（结构化数据）
天气API
天气文字
图片链接
图片二进制数据'''


'''import requests
response = requests.get('https://wttr.in/Beijing?format=3')#访问天气API，获取北京的天气信息，format=3表示只返回简洁的天气信息
print(response.text)'''


#解析JSON数据
'''import requests
response = requests.get('https://httpbin.org/json')
data = response.json()  #把返回的JSON数据解析成Python字典
print(data)
print(type(data))  #查看数据类型，应该是字典'''


import requests
reqonse = requests.get('https://open.er-api.com/v6/latest/USD')  #访问汇率API，获取美元的最新汇率信息
data = reqonse.json()  #把返回的JSON数据解析成Python字典
print("美元对人民币的汇率是："+str(data["rates"]["CNY"]))
print("美元对欧元的汇率是："+str(data["rates"]["EUR"]))
print("美元对日元的汇率是："+str(data["rates"]["JPY"]))