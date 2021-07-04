def show():
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生信息")
    print("4.修改单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")

#input 函数进行获取学生信息，姓名，年龄
# 将学生信息转换为字典 将学生字典添加到列表中
#同样的姓名不能重复添加
def tianjia():
    student={'name':input("姓名:"),'age':int(input("年龄:")),'性别':input("性别:")}
    i1=0#判断是否有重复姓名
    for i in all_student:
        if i['name']==student['name']:
            i1=1
            break
        else:
            continue
    if i1==0:
        all_student.append(student)
        print("==========学生信息添加成功==============")
    else:
        print("学生姓名已存在")
        print("==========学生信息添加失败==============")


def chakan():
    if len(all_student)>0:
        for stu in all_student:
            # print(stu)
            print(f"name:{stu['name']},age:{stu['age']},性别:{stu['性别']}")
    else:
        print("目前没有学生信息呀")

# 如果学生姓名存在 即删除/修改/查询
# 判断学生信息是否存在
# 学生存在 可删 可查 可修改  不存在 可以结束
def w_remove():
    zz=input("输入姓名")
    for i in all_student:
        if i['name']==zz:
            all_student.remove(i)
            break
    else:
        print("=============列表中没有该学生==========")

def w_xiugai():
    zz=input("输入姓名")
    for i in all_student:
        if i['name']==zz:
            i['name']=input("请修改姓名")
            i['age']=int(input("请修改年龄"))
            i['性别']=input("请修改性别")
            break
    else:
        print("============该学生不存在，无法修改==========")

def w_search():
    zz=input("输入姓名")
    for i in all_student:
        if i['name']==zz:
            print(f"name:{i['name']},age:{i['age']},性别:{i['性别']}")
            break
    else:
        print("============该学生不存在，无法修改==========")


def shanchu():
    zz=input("输入姓名")
    z=0 #判定有没有该学生信息
    for i in all_student:
        if i['name']==zz:
            all_student.remove(i)
            z=1
            break
        else:
            continue
    if z== 0:
        print("=============列表中没有该学生==========")
    else:
        print("==========删除成功==============")




all_student=[]

def main():
    while True:
        show()
        num = input("请输入的服务:")
        if num == '1':
            print("1.添加学生")
            tianjia()
        elif num == '2':
            print("2.删除学生")
            shanchu()
        elif num == '3':
            print("3.修改学生信息")
            w_xiugai()
        elif num == "4":
            print("4.查询单个学生信息")
            w_search()
        elif num == "5":
            print("5.查询所有学生信息")
            chakan()
        elif num == "6":
            print("欢迎下次使用")
            break
        else:
            print("输入有误")
            continue


        input("....回车键继续操作.....")

main()

print("更新代码了哦嘿嘿怎么样")