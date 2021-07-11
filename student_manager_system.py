# coding=gbk
# @file:student_manager_system.py
# @data:2021/7/11 17:12
# Editor:clown
import sdudent as xuesheng


class studentMangerSystem(object):
    def __init__(self):
        self.stu_dicts = {}

    # ��Ϊû���õ�ʵ�����ԣ������õ���̬����
    @staticmethod
    def show():
        print("1.���ѧ��")
        print("2.ɾ��ѧ��")
        print("3.�޸�ѧ����Ϣ")
        print("4.�鿴����ѧ����Ϣ")
        print("5.��ѯ����ѧ����Ϣ")
        print("6.�˳�ϵͳ")

    def insert_student(self):
        # ��input��ȡѧ����Ϣ
        stu_id = input("������ѧ��")
        name = input("������ѧ������")
        # �����Ż�  �ж�ѧ����Ϣ�Ƿ���� ѧ���Ƿ���ڡ�
        if stu_id in self.stu_dicts:
            print("====���ѧ������ʧ��====")
            return
        age = input("����������")
        gender = input("�������Ա�")
        # ����ѧ����Ϣ������ѧ������ student���ֵ�
        student = xuesheng.Student(stu_id, name, age, gender)
        # ��ѧ����Ϣ������ӵ��ֵ� �ֵ�['key']=����ֵ
        # �ֵ���ֵ�Ĵ洢
        self.stu_dicts[stu_id] = student
        # ����һ��ʼ���ֵ� ���ֵ���д洢

    def delete_student(self):
        s_id = input("������ɾ����ѧ��")
        if s_id in self.stu_dicts:
            del self.stu_dicts[s_id]
            print("����ѧ���Ѿ�ɾ��")
        else:
            print("ѧ����Ϣû�д���")

    def up_student(self):
        s_id = input("���������ѧ����ѧ��")
        if s_id in self.stu_dicts:
            # �޸Ķ�������� ����.������=����ֵ
            stu = self.stu_dicts[s_id]
            # �õ��ľ���ѧ������ ���Կ�����ô�޸�
            stu.name = input("���޸�ѧ����Ϣ:")
            stu.age = input("���޸�ѧ������:")
            stu.gender = input("���޸�ѧ���Ա�:")
            stu.std_id = input("���޸�ѧ��ѧ��:")
            print("ѧ����Ϣ�Ѿ��޸�")
        else:
            print("������Ϣ��ѧ����Ϣû�д���")

        # �Լ�д��
        # for i in self.stu_dicts.keys:
        #     if s_id==i:
        #         del self.stu_dicts[s_id]
        #         print("����ѧ���Ѿ�ɾ��")

    def search_student(self):
        s_id = input("������ѧ����ѧ��")
        if s_id in self.stu_dicts:
            # �޸Ķ�������� ����.������=����ֵ
            stu = self.stu_dicts[s_id]
            print(f"ѧ����Ϣ��{stu}")
        else:
            print("�鿴������Ϣ��ѧ����Ϣû�д���")

    def show_allinfo(self):
        # for stu in self.stu_dicts.values():
        #     print(stu)

        # �Լ�д��
        for i in self.stu_dicts:
            print(f"ѧ�����˼����Ϣ��{self.stu_dicts[i]}")

    def save(self):
        f = open('student.txt', "w", encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')
            # �㾦֮��   ������Ϊstr����������
            # ���Ի��Զ���ӡstudent���е�str����
        f.close()

    # ��ȡ ��ȡ�ļ���һ�����ݾ���һ��ѧ����Ϣ
    # readlines ��ȡ������
    # ['11,12,18,16\n','12,15,48,15\n']���Ǵ���student.txt��
    def load_infp(self):
        try:
            f = open('student.txt', 'r', encoding="utf-8")
            buf_list = f.readlines()
            for buf in buf_list:
                buf = buf.strip()  # ȥ����ν��\n
                info_list = buf.split(',')  # �б�
                # ��������
                # lala=xuesheng.Student(info_list[0],info_list[1],
                #                       info_list[2],info_list[3])
                # ���б������������β�
                lala = xuesheng.Student(*info_list)
                #��������ӵ��ֵ���
                stu_id=info_list[0]
                self.stu_dicts[stu_id]=lala #�Ѷ���Ž�ȥ
            f.close()
        except Exception:
            pass


    def start(self):
        # ������������������� ����ϵͳ�����ظ���ȡ��������
        # ��ÿ����������ݽ��б���
        # �Ӷ��ﵽ���ʹ��
        # read_file()  # ��һ�δ��� ÿ����ֻ��ȡ��������
        self.load_infp()
        while True:
            self.show()
            num = input("������ķ���:")
            if num == '1':
                print("1.���ѧ��")
                self.insert_student()
                # tianjia()
            elif num == '2':
                print("2.ɾ��ѧ��")
                # shanchu()
                self.delete_student()
            elif num == '3':
                print("3.�޸�ѧ����Ϣ")
                # w_xiugai()
                self.up_student()
            elif num == "4":
                print("4.��ѯ����ѧ����Ϣ")
                # w_search()
                self.search_student()
            elif num == "5":
                print("5.��ѯ����ѧ����Ϣ")
                self.show_allinfo()
                # chakan()
            elif num == "6":
                print("��ӭ�´�ʹ��")
                self.save()
                # save()  # �����ļ�
                break
            else:
                print("��������")
                continue

            input("....�س�����������.....")
