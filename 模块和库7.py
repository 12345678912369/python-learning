#Python自带很多模块，直接import就能用
#随机模块
import random
#随机生成1到10的数字
num = random.randint(1,10)
print("随机生成的数字是："+str(num))
 
 #从列表里随机选一个元素
names = ["张三","李四","王五","赵六"]
name = random.choice(names)
print("随机选中的名字是："+name)


#时间模块
import datetime
now = datetime.datetime.now()  #获取当前时间
print("当前时间是："+str(now))
print("当前年份是："+str(now.year))
print("现在是："+str(now.hour)+"点"+str(now.minute)+"分")


#猜数字游戏
import random
num = random.randint(1,100)  #随机生成1到100的数字
count = 0  #猜的次数
while True:
    guess = input("请输入你猜的数字（输入'exit'退出）：")
    count += 1
    if guess == "exit":
        print("游戏结束，正确答案是："+str(num))
        print("你总共猜了"+str(count)+"次")
        break
    guess = int(guess)
    if guess < num:
        print("太小了！")
    elif guess > num:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        print("你总共猜了"+str(count)+"次")
        break