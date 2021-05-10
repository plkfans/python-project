# -*- codeing = utf-8 -*-
# @Time : 2021/5/10 9:29
# @File : managerSystem.py
# @software : PyCharm
from Student import *
class StudentManeger(object):
    #列表用于存储数据
    def __init__(self):
        self.student_list = []


    #程序入口
    def run(self):
        # 加载现有数据
        self.load_student()
        for i in self.student_list:
            print(i)
        # 显示菜单
        self.menu(self)
        while True:
            # 输入序号，选择功能
            menu_num = int(input('请选择功能：'))
            # 4 根据⽤用户输⼊入的功能序号执⾏行行不不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 0:
                # 退出系统
                print('退出系统成功')
                break
    #系统功能
    @staticmethod
    def menu(self):
        print('-' * 20)
        print('欢迎登录学员管理理系统')
        print('1: 添加学员')
        print('2: 删除学员')
        print('3: 修改学员信息')
        print('4: 查询学员信息')
        print('5: 显示所有学员信息')
        print('6:保存学员信息')
        print('0: 退出系统')
        print('-' * 20)

    def add_student(self):
        """添加学员"""
        new_name = input("请输入姓名：")

        for i in self.student_list:
            if new_name == i.name:
                print('添加失败，用户已存在。')
                break
        else:
            new_gender = input("请输入性别：")
            new_tel = input("请输入电话")
            student1 = Student(new_name,new_gender,new_tel)
            self.student_list.append(student1)
            print('添加成功。')
            for i in self.student_list:
                print(i)

    def del_student(self):
        """删除学员"""
        del_name = input('请输入要删除的学员姓名：')

        #如果用户输入的学员存在则删除学员对象，否则提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                # 删除该学员对象
                self.student_list.remove(i)
                print('删除成功。')
                break
        else:
            print('查无此人！')

    def modify_student(self):
        """修改学员信息"""
        mod_name = input('请输入要修改的学员姓名：')

        for i in self.student_list:
            if mod_name == i.name:
                i.name = input('请输入新名字：')
                i.gender = input('请输入性别：')
                i.tel = input('请输入新电话：')
                print('修改成功')
                break
        else:
            print('查无此人')

    def search_student(self):
        """查询学员信息"""
        # 1. 用户输入目标学员姓名
        search_name = input('请输入您要搜索的学员姓名：')

        # 2. 遍历列表。如果学员存在打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名是{i.name}, 性别是{i.gender}, 手机号是{i.tel}')
                break
        else:
            print('查无此人！')

    def show_student(self):
        """显示所有学员信息"""
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}, {i.gender}, {i.tel}')

    def save_student(self):
        """保存学员信息"""
        # 1. 打开文件
        f = open('student.data', 'w')
        # 2. 文件写入数据
        # 2.1 [学员对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.student_list]
        # 2.2 文件写入 字符串数据
        f.write(str(new_list))
        # 3. 关闭文件
        f.close()
        print('保存成功')

    def load_student(self):
        # 1. 打开文件：尝试r打开，如果有异常w
        try:
           f = open('student.data','r')
        except:
           f = open('student.data','w')
        else:
            # 2. 读取数据：文件读取出的数据是字符串还原列表类型；[{}] 转换 [学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        # 3. 关闭文件
        finally:
            f.close()