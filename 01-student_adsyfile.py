# coding=gbk
# @file:01-student_adsyfile.py
# @data:2021/7/5 17:53
# Editor:clown
import os
#���ַ��������е�ѧ����Ϣ���浽�ļ���  '[{},{},{}....]'
def show():
    print("1.���ѧ��")
    print("2.ɾ��ѧ��")
    print("3.�޸�ѧ����Ϣ")
    print("4.�鿴����ѧ����Ϣ")
    print("5.��ѯ����ѧ����Ϣ")
    print("6.�˳�ϵͳ")

#input �������л�ȡѧ����Ϣ������������
# ��ѧ����Ϣת��Ϊ�ֵ� ��ѧ���ֵ���ӵ��б���
#ͬ�������������ظ����
def tianjia():
    student={'name':input("����:"),'age':int(input("����:")),'�Ա�':input("�Ա�:")}
    i1=0#�ж��Ƿ����ظ�����
    for i in all_student:
        if i['name']==student['name']:
            i1=1
            break
        else:
            continue
    if i1==0:
        all_student.append(student)
        print("==========ѧ����Ϣ��ӳɹ�==============")
    else:
        print("ѧ�������Ѵ���")
        print("==========ѧ����Ϣ���ʧ��==============")


def chakan():
    if len(all_student)>0:
        for stu in all_student:
            # print(stu)
            print(f"name:{stu['name']},age:{stu['age']},�Ա�:{stu['�Ա�']}")
    else:
        print("Ŀǰû��ѧ����Ϣѽ")

# ���ѧ���������� ��ɾ��/�޸�/��ѯ
# �ж�ѧ����Ϣ�Ƿ����
# ѧ������ ��ɾ �ɲ� ���޸�  ������ ���Խ���
def w_remove():
    zz=input("��������")
    for i in all_student:
        if i['name']==zz:
            all_student.remove(i)
            break
    else:
        print("=============�б���û�и�ѧ��==========")

def w_xiugai():
    zz=input("��������")
    for i in all_student:
        if i['name']==zz:
            i['name']=input("���޸�����")
            i['age']=int(input("���޸�����"))
            i['�Ա�']=input("���޸��Ա�")
            break
    else:
        print("============��ѧ�������ڣ��޷��޸�==========")

def w_search():
    zz=input("��������")
    for i in all_student:
        if i['name']==zz:
            print(f"name:{i['name']},age:{i['age']},�Ա�:{i['�Ա�']}")
            break
    else:
        print("============��ѧ�������ڣ��޷��޸�==========")


def shanchu():
    zz=input("��������")
    z=0 #�ж���û�и�ѧ����Ϣ
    for i in all_student:
        if i['name']==zz:
            all_student.remove(i)
            z=1
            break
        else:
            continue
    if z== 0:
        print("=============�б���û�и�ѧ��==========")
    else:
        print("==========ɾ���ɹ�==============")

def save():
    #1.���ļ�
    f=open('student.txt','w',encoding='utf-8')
    #ת��Ϊ�ַ�����ԭ����� write����ֻ����д�ַ���
    f.write(str(all_student))
    ##eval����������������
    f.close()

def read_file():
    global all_student
    #os.path.exists�����ǲ��Ǵ��� ���ھ�if ִ�� ������ ������
    if os.path.exists('student.txt'):
        f=open('student.txt','rb')
        # buf=eval(f.read())
        buf=f.read()
        if os.path.exists('student.txt'):                  #��ֹtxt�ļ�Ϊ��
            all_student=eval(buf) #eval����������������ַ���
            print(all_student)


all_student=[]

def main():
    #������������������� ����ϵͳ�����ظ���ȡ��������
    # ��ÿ����������ݽ��б���
    #�Ӷ��ﵽ���ʹ��
    read_file()#��һ�δ��� ÿ����ֻ��ȡ��������
    while True:
        show()
        num = input("������ķ���:")
        if num == '1':
            print("1.���ѧ��")
            tianjia()
        elif num == '2':
            print("2.ɾ��ѧ��")
            shanchu()
        elif num == '3':
            print("3.�޸�ѧ����Ϣ")
            w_xiugai()
        elif num == "4":
            print("4.��ѯ����ѧ����Ϣ")
            w_search()
        elif num == "5":
            print("5.��ѯ����ѧ����Ϣ")
            chakan()
        elif num == "6":
            print("��ӭ�´�ʹ��")
            save()  #�����ļ�
            break
        else:
            print("��������")
            continue


        input("....�س�����������.....")


main()
# save()  #��������
print("���´�����Ŷ�ٺ���ô��")