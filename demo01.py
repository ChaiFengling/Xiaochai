# '''print("hello world!")   #字符串
# print(233)    #整数
# print(2.333)   #小数
# print(False)   #布尔值
# print(())      #元祖
# print([])       #数组
# print({})       #字典



# print("哈哈","2333")   #print可以同时输出多个数据
# print("哈哈"+"嘻嘻")    #字符串的拼接，但必须是同一类型
# print("哈哈"*100)      #打印100个哈哈
# print(2<3)             #布尔值，用与判断

# #变量
# #赋值
# name="张三"     #把张三的值赋值给名叫name的变量
# print(name)'''


# # a=input("请输入：")
# # b=input("请输入: ")
# # print("input获取的内容:",a+b)  #input输入的都是字符串

# #数据格式的转变,type()
# # print(type("哈哈"))
# # print(type(2333))
# # print(type(2.333))
# # print(type(True))
# # print(type(()))
# # print(type([]))
# # print(type({}))

# # a=float(input("请输入:"))
# # b=float(input("请输入:"))
# # print("input获取的内容:",a+b)

# # a="hahhahah"
# # print(len(a))  #len  获取字符串的长度

# #练习：通过代码获取两端内容，并且计算他们长度的和。
# a=input("请输入一个字符串:")
# b=input("请输入另一个字符串:")
# print("input获取的内容:",a+b)
# print(len(a+b))

# # print("两段字符串和的长度为:",len(a)+len(b))    #另一种方式











                  #元组  下表从0开始编号
# a=(1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈","哈哈",True,False)
# print(a)
# print(a[5])

#a.index("哈哈")     #index：寻找某个值的下标，如有多个则就近原则
#a.count("哈哈")     #count：统计某个值的的个数
# print(a.index("哈哈"))
# print(a.count("哈哈"))

#切片：取多个值
# a=(1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈","哈哈",True,False)
# print(a[0:4])    #左闭右开，不包括4
# print(a[4:9])
# print(a[9:])



                   #二维元组
# a=(1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈","哈哈",True,False)
# b=(a,"哈哈","嘻嘻")
# print(b)
# print(b[1])
# print(b[0][3])


#元组一旦写好好不能进行修改，而数组可以修改












                    #数组
# a=[1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈","哈哈",True,False]
# a.append("插入的数据1")
# a.append("插入的数据2")         #append()：往数组中追加数据 固定插入在末尾
# print(a)
# a.insert(0,"插入的数据3")       #insert():往数组中指定的位置添加数据，设置下标即可
# print(a)
# a.pop(6)                       #pop()：剪切数据，将下标为5的元素取出来
# print(a)
# b=a.pop(1)                     #将a.pop(1)的值赋给b
# c=a.pop(1)                     #将a.pop(1)的值赋给c
# print(b+c)

# d=["插入的数据4"]
# a.extend(d)                    #entend()：作用与append类似，可以添加数组
# print(a)                       #可直接print(a+d)

# a.remove("插入的数据4")          #remove()：删除数组中某个元素
# print(a)

# a.clear()                      #clear()：清空数组
# print(a)


"""
python语法
所有的方法都是小括号结尾。比如,print(),input(),len()
元组、数组、字典的取值、都是用中括号，比如a[0]
元组、数组、字典的定义、分别是()[]{}
"""











                  #字典
"""
字典的特点 
1、字典中的值没有顺序。
2、字典的结构必须是   键值对的结构。  key:value
"""

# a={"name":"张三","sex":"男","age":25}

# print(a["name"])         #取值

# a["high"]="190cm"        #新增
# print(a)

# a["name"]="李四"         #修改
# print(a)


# b=a.get("name")      #get():取值
# print(b)

# b=a.pop("sex")       #pop()：剪切
# print(a)
# print(b)

# a.update(sex="女")    #update 修改或者新增
# print(a)

# print("----------------------")
# print(a.get("name"))           #两种取值方法的区别：正常情况下一样若果是输入错误的情况get()返回空值None，a["name"]则报错
# print(a["name"])
# print(a.get("sex11"))
# print(a["sex11"])


#字典和数组的删除
# del a["name"]
# print(a)

#del a[0]  数组删除方法


"""
联系：获取用户输入的信息并储存在字典中，信息包括name age sex
"""

# a={"name":"张三","age":"18","sex":"男"}
# print(a)

# name=input("请输入你的姓名:")
# age=input("请输入你的年龄:")
# sex=input("请输入你的性别:")
# userinfo={}
# userinfo.update(name=name,age=age,sex=sex)
"""userinfo=["name"]=name
userinfo=["age"]=age
userinfo=["sex"]=sex
另一种方式"""
# print(userinfo)