# 读取文件
# 方法一(读取完之后会自动关闭)-----推荐方法一
with open("a.txt",encoding="utf-8")as f:
    print(f.read())
# # 方法二
# f = open("a.txt",encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

