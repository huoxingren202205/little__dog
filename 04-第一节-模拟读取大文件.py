# 如果文件读到最后返回的都是空字符串
# 读取大文件
# 方法一：
# with open("a.txt",encoding="utf-8")as f:
#     while True:
#         buf=f.readline()
#         if buf=="":
#             break
#         else:
#             print(buf,end="")
# 方法二：
with open("a.txt",encoding="utf-8")as f:
    while True:
        buf=f.readline()
        if buf:
            print(buf,end="")
        else:
            break



