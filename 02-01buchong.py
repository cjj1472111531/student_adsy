def fun(*a,**b):
    print("a:",a)
    print("b:",b)
    num=0
    # for i in a:
    #     num+=i
    #
    # for j in b.values():
    #     num+=j

    print(f"求和的结果为{num}")

my_list=[1,1,3,5,2,4]
my_dict={'a':7,'b':8,'c':9,'d':10}
# fun(*my_list,**my_dict)
# print("*"*30)
# print()

# fun(my_list) #将列表作为一个数据进行传递
# print("!"*30)
# print()
#
# fun(*my_list) #列表中每一个数据作为位置参数进行传递 拆包
# print("!"*30)
# print()

fun(my_dict) #将字典作为一个位置实参进行传递
print("&"*30)
print()

fun(*my_dict) #将字典中k作为一个位置实参进行传递  元组
print("*"*30)
print()

fun(**my_dict)#字典中键值对作为实参  作为位置参数进行传递 拆包  字典


