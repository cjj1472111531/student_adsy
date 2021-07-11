# coding=gbk
# @file:student_manager_system.py
# @data:2021/7/11 17:12
# Editor:clown
import sdudent as xuesheng


class studentMangerSystem(object):
    def __init__(self):
        self.stu_dicts = {}

    # 因为没有用到实例属性，所以用到静态方法
    @staticmethod
    def show():
        print("1.添加学生")
        print("2.删除学生")
        print("3.修改学生信息")
        print("4.查看单个学生信息")
        print("5.查询所有学生信息")
        print("6.退出系统")

    def insert_student(self):
        # 用input获取学生信息
        stu_id = input("请输入学号")
        name = input("请输入学生姓名")
        # 代码优化  判断学生信息是否存在 学号是否存在。
        if stu_id in self.stu_dicts:
            print("====添加学生操作失败====")
            return
        age = input("请输入年龄")
        gender = input("请输入性别")
        # 创建学生信息，创建学生对象 student是字典
        student = xuesheng.Student(stu_id, name, age, gender)
        # 将学生信息对象添加的字典 字典['key']=数据值
        # 字典中值的存储
        self.stu_dicts[stu_id] = student
        # 根据一开始的字典 将字典进行存储

    def delete_student(self):
        s_id = input("请输入删除的学号")
        if s_id in self.stu_dicts:
            del self.stu_dicts[s_id]
            print("输入学号已经删除")
        else:
            print("学生信息没有存在")

    def up_student(self):
        s_id = input("请输入更新学生的学号")
        if s_id in self.stu_dicts:
            # 修改对象的属性 对象.属性名=属性值
            stu = self.stu_dicts[s_id]
            # 得到的就是学生对象 所以可以这么修改
            stu.name = input("请修改学生信息:")
            stu.age = input("请修改学生年龄:")
            stu.gender = input("请修改学生性别:")
            stu.std_id = input("请修改学生学号:")
            print("学生信息已经修改")
        else:
            print("更新信息：学生信息没有存在")

        # 自己写的
        # for i in self.stu_dicts.keys:
        #     if s_id==i:
        #         del self.stu_dicts[s_id]
        #         print("输入学号已经删除")

    def search_student(self):
        s_id = input("请输入学生的学号")
        if s_id in self.stu_dicts:
            # 修改对象的属性 对象.属性名=属性值
            stu = self.stu_dicts[s_id]
            print(f"学生信息：{stu}")
        else:
            print("查看个人信息：学生信息没有存在")

    def show_allinfo(self):
        # for stu in self.stu_dicts.values():
        #     print(stu)

        # 自己写的
        for i in self.stu_dicts:
            print(f"学生个人简介信息：{self.stu_dicts[i]}")

    def save(self):
        f = open('student.txt', "w", encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')
            # 点睛之笔   就是因为str函数起作用
            # 所以会自动打印student类中的str函数
        f.close()

    # 读取 读取文件，一行内容就是一个学生信息
    # readlines 读取所有行
    # ['11,12,18,16\n','12,15,48,15\n']这是存在student.txt中
    def load_infp(self):
        try:
            f = open('student.txt', 'r', encoding="utf-8")
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # 去掉所谓的\n
                info_list = buf.split(',')  # 列表
                # 创建对象
                # lala=xuesheng.Student(info_list[0],info_list[1],
                #                       info_list[2],info_list[3])
                # 把列表变量逐个给到形参
                lala = xuesheng.Student(*info_list)
                #将对象添加到字典中
                stu_id=info_list[0]
                self.stu_dicts[stu_id]=lala #把对象放进去
            f.close()
        except Exception:
            pass


    def start(self):
        # 这样做的意义就是在于 管理系统可以重复读取连的数据
        # 将每次输入的数据进行保存
        # 从而达到多次使用
        # read_file()  # 用一次代码 每次用只读取里面内容
        self.load_infp()
        while True:
            self.show()
            num = input("请输入的服务:")
            if num == '1':
                print("1.添加学生")
                self.insert_student()
                # tianjia()
            elif num == '2':
                print("2.删除学生")
                # shanchu()
                self.delete_student()
            elif num == '3':
                print("3.修改学生信息")
                # w_xiugai()
                self.up_student()
            elif num == "4":
                print("4.查询单个学生信息")
                # w_search()
                self.search_student()
            elif num == "5":
                print("5.查询所有学生信息")
                self.show_allinfo()
                # chakan()
            elif num == "6":
                print("欢迎下次使用")
                self.save()
                # save()  # 保存文件
                break
            else:
                print("输入有误")
                continue

            input("....回车键继续操作.....")
