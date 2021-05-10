# -*- codeing = utf-8 -*-
# @Time : 2021/5/10 11:19
# @File : text.py
# @software : PyCharm
class Student(object):
    def __init__(self,name,gender,tel):
        self.name1 = name
        self.gender1 = gender
        self.tel1 = tel
        self.student_list = ['mm', 'nan', 123]

    def load(self):
        new_list = [self.__dict__]
        print(new_list)

    def __str__(self):
        return f'{self.name1},{self.gender1},{self.tel1}'


s = Student('mm','男',132)
s.load()
# student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
# for i in student_list:
#     print(i)