#判断  print前面的四个空格叫做锁进，表示这个语句属于上一条语句下

age=int(input("请输入你的年龄:")) 
if age>20 and age<=30:
    print("努力挣钱")
elif age>30 and age<=60:
    print("努力工作")
elif age>60:
    print("退休啦")
else:
    print("好好学习")
