# # 写入文件
#
# # 1.打开文件
# f=open('a.txt','w',encoding='utf-8')
# # 2.写入文件
# f.write("好好学习\n天天向上")
# # 3.关闭文件
# f.close()

# 追加文件(每运行一次增加一个添加的内容)
with open("a.txt","a",encoding="utf-8")as f:
    f.write("good good study\nday day up\n")