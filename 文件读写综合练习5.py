students = []
for i in range(3):
    name = input("请输入学生姓名：")
    score = int(input("请输入学生成绩："))
    student = {"name":name,"score":score}
    students.append(student)
    with open("students.txt","w",encoding="utf-8") as f:
        for student in students:
            f.write(student["name"]+","+str(student["score"])+"\n")  #把学生姓名和成绩写到文件里，每个学生占一行，姓名和成绩用逗号分隔
with open("students.txt","r",encoding="utf-8") as f:
    lines = f.readlines()  #把文件内容按行读到lines列表里，每行是一个元素
    for line in lines:
       parts = line.strip().split(",")  #去掉行末的换行符，然后用逗号分隔成姓名和成绩
       name = parts[0]  #姓名是分隔后的第一个元素
       score = int(parts[1])  #成绩是分隔后的第二个元素，转换成整数
       if score>=60:
        print(name+":"+str(score)+"成绩及格")
       else:
        print(name+":"+str(score)+"成绩不及格")