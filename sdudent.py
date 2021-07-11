# coding=gbk
# @file:sdudent.py
# @data:2021/7/11 17:13
# Editor:clown
class Student(object):
    def __init__(self,std_id,name,age,gender):
        self.std_id=std_id
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return f"{self.std_id},{self.name}," \
               f"{self.age},{self.gender}"

# if __name__=='__main__':
#     stu=Student(1,'clown',18,'不详')
#     print(stu)

