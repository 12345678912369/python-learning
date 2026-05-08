import random


users = {
    "13800138000": {
        "name": "小明",
        "code": ""
    }
}


def show_menu():
    print("\n===== 手机号验证码登录 =====")
    print("1. 注册手机号")
    print("2. 发送验证码")
    print("3. 验证码登录")
    print("4. 退出程序")


def register():
    phone = input("请输入手机号：")

    if phone in users:
        print("这个手机号已经注册过了。")
        return

    name = input("请输入昵称：")
    users[phone] = {
        "name": name,
        "code": ""
    }
    print("注册成功！")


def send_code():
    phone = input("请输入手机号：")

    if phone not in users:
        print("手机号不存在，请先注册。")
        return

    code = str(random.randint(1000, 9999))
    users[phone]["code"] = code
    print("验证码已发送：" + code)


def login():
    phone = input("请输入手机号：")

    if phone not in users:
        print("手机号不存在，请先注册。")
        return

    code = input("请输入验证码：")

    if code == users[phone]["code"]:
        print("登录成功，欢迎你：" + users[phone]["name"])
        users[phone]["code"] = ""
    else:
        print("验证码错误，登录失败。")


while True:
    show_menu()
    choice = input("请选择功能：")

    if choice == "1":
        register()
    elif choice == "2":
        send_code()
    elif choice == "3":
        login()
    elif choice == "4":
        print("程序已退出。")
        break
    else:
        print("输入错误，请输入 1-4。")
