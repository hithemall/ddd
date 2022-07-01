"""
目标：open 与 with open区别
     1.共同点：打开文件
     2.不同点：with open = 执行打开操作 + 关闭操作

"""
"""
f = None
try:
    f = open("../report/text.txt","r",encoding="utf-8")
    print(f.read())


except:
    pass
finally:
    f.close()
    
  """



"""with open 极力推荐 """
#打开
#with open("../report/text.txt","r",encoding="utf-8") as f:
    #f.read()

#写入
with open("../report/text.txt","a",encoding="utf-8") as f:
    data = f.read()
    print(data)
"""文件流：打开指定写入的文件"""
