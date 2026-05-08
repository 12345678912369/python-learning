'''def greet(name):        def是定义函数的关键词
    print("你好"+name)      greet是函数名    name是参数
greet("张三")
greet("李四")
greet("王五")
greet("赵六")'''



'''def square(num):
    print(num**2)   **2表示平方
square(8)
square(12)'''



'''def square(num):                                return和print的区别：                
    return num ** 2                                print 只是显示，结果用完就没了
                                                   return 把结果交出来，可以存到变量里继续用
result = square(8)
print("8的平方是：" + str(result))

# 也可以直接用
print("12的平方是：" + str(square(12)))'''



'''def add(num1,num2):
    return num1+num2
result = add(6,5)
print("之和是" + str(result))
print("之和是" + str(add(8,10)))'''


#列表就是把一堆数据放在一起
#列表增删操作
'''students = ["张三","李四","王五"]
students.append("赵六")#添加到末尾
print(students)
students.remove("李四")#删除指定元素
print(students)
print(len(students))#列表长度'''


#列表就是把一堆数据放在一起
'''students = ["张三", "李四", "王五", "赵六"]
print(students)        # 打印整个列表
print(students[0])     # 打印第一个，索引从0开始
print(students[-1])    # 打印最后一个  负数从尾数'''


#列表+循环
'''scores = [34,55,78,89,90]
for score in scores:  #把scores列表里的每个元素，一个一个取出来，每次放到score变量里
    if score>=60:
        print(str(score)+"及格")
    else:
        print(str(score)+"不及格")'''


#综合小项目:成绩管理小程序
names = []
scores = []
for i in range(3):
    name = input("请输入学生名字：")
    score = int(input("请输入成绩："))
    names.append(name)
    scores.append(score)
    if score>=60:
        print(str(name)+str(score)+"及格")
    else:
        print(str(name)+str(score)+"不及格")