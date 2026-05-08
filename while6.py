#whike 循环基础
#for 是循环固定次数，while 是条件成立就一直循环
'''count = 0
while count < 5:  #当count小于5时，循环继续
    print(count)
    count += 1  #每次循环结束，count加1 '''


'''while True:  #死循环，条件永远成立
    name = input("请输入你的名字（输入'exit'退出）：")
    if name == "exit":  #如果输入exit，跳出循环
        break
    print("你好，" + name + "！")'''


'''#小项目
while True:
    num = input("请输入一个数字（输入'0'退出）：")
    if num == "0": 
        break
    num = int(num)  #把输入的字符串转换成整数
    print(str(num)+"的平方是"+str(num**2))  #打印结果'''


#升级成绩管理程序
students = []
while True:
    print("\n1.添加学生信息")
    print("2.查看学生信息")
    print("3.退出")
    choice = input("请输入你的选择：")
    if choice == "1":
        name = input("请输入学生名字：")
        age = input("请输入学生年龄：")
        score = int(input("请输入学生分数："))
        student = {"name":name,"age":age,"score":score}
        students.append(student)
    elif choice == "2":
        for student in students:
            print(student["name"]+"年龄:"+str(student["age"])+"，分数:"+str(student["score"]))
    elif choice == "3":
        print("退出程序")
        break
    else:
        print("无效的选择，请重新输入")