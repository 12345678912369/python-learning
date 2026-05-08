'''#写入文件
f = open("data.txt","w")
f.write("hello world\n")
f.close()'''

#更好点的写法
with open("data.txt","w",encoding="utf-8") as f:
    f.write("hello world\n")
    f.write("你好，世界\n")#with 会自动关闭文件，不需要手动 f.close()
    


#读取文件
with open("data.txt","r",encoding="utf-8") as f:
    content = f.read()#把文件内容读到content变量里
    print(content)
