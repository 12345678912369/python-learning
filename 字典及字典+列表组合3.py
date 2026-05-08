'''student = {                    #列表是用数字索引，字典是用名字来找数据
    "name": "jay",
    "age": 23,
    "score": 99
}
print(student["name"])
print(student["age"])
print(student["score"])'''


'''#增删改查
student = {"name":"jay","score":99}
#添加新键
student["age"] = 23
print(student)
#修改值
student["score"]=100
print(student)
#删除键值对
del student["age"]
print(student)'''


#遍历字典
'''student = {"name":"jay","age":23,"score":99}
for key in student:  #把student字典里的每个键，一个一个取出来，每次放到key变量里
    print(key)       #打印键
    print(student[key])  #通过键来获取对应的值并打印'''

'''student = {"name":"jay","age":23,"score":99}
for key,value in student.items():  #items()方法可以同时取出键和值
    print(key)       #打印键
    print(value)     #打印值'''

'''student = {"name":"jay","age":23,"score":99}
for key,value in student.items():
    print(str(key)+":"+str(value))  #把键和值都转换成字符串，拼接在一起打印'''


#列表+字典组合
'''students = [
    {"name":"张三","age":23,"score":99},
    {"name":"李四","age":22,"score":88},
    {"name":"王五","age":24,"score":77}
]
for student in students:  #把students列表里的每个元素，一个一个取出来，每次放到student变量里
    print(student["name"]+"的年龄是"+str(student["age"])+"，分数是"+str(student["score"]))  #通过键来获取对应的值并打印'''

'''students = [
    {"name":"张三","age":23,"score":99},
    {"name":"李四","age":22,"score":88},
    {"name":"王五","age":24,"score":77}
    ]
for student in students:
        if student["score"]>=90:
            print(student["name"]+"成绩优秀")
        elif student["score"]>=80:
            print(student["name"]+"成绩良好")
        elif student["score"]>=60:
            print(student["name"]+"成绩及格")
        else:
            print(student["name"]+"成绩不及格")'''

#小程序练习
students = []
for i in range(3):
    name = input("请输入学生名字：")
    age = input("请输入学生年龄：")
    score = int (input("请输入学生分数："))
    student = {"name":name,"age":age,"score":score}
    students.append(student)
for student in students:
    if student["score"]>=90:
        print(student["name"]+"成绩优秀")
    elif student["score"]>=80:
        print(student["name"]+"成绩良好")
    elif student["score"]>=60:
        print(student["name"]+"成绩及格")
    else:
        print(student["name"]+"成绩不及格")