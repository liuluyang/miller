# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/23 9:46

# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、石家庄 2 所学校
# 2. 创建linux , python , php, go 4个课程 ， linux\go 在北京开， python\php 在石家庄开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校

# 6. 提供三个角色接口
#     6.1 学员视图， 可以注册， 交学费， 选择班级
#     6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
#     6.3 管理视图，创建讲师， 创建班级，创建课程
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里
from core.main import *
from conf import settings
from utils.get_info import get_info

school_all_info = get_info()


class BaseView(object):
    def __init__(self):
        if not hasattr(self, "operator"):
            raise ("operator must be settings")
        super().__init__()

    def handler(self):
        for ind, tu in enumerate(self.operator, 1):
            print(" %d: %s  --  %s " % (ind, tu[0], tu[1]))
        choice = input("请选择你要干啥（ 'quit' 退出）:").strip()
        if choice.isdigit():
            stt = self.operator[int(choice) - 1][0]
            if hasattr(self, stt):
                getattr(self, stt)()
        if choice == "quit":
            exit("再见")


class AdminView(BaseView):
    operator = [
        ("create_school", "创建学校",),
        ("create_classes", "创建班级"),
        ("create_course", "创建课程"),
        ("create_teacher", "创建老师")
    ]

    def select_school(self):
        li = []
        for name in school_all_info["school"]:
            li.append(name)
        print("\n".join("{}-{}".format(*i) for i in enumerate(li)))
        school_obj = school_all_info["school"][li[int(input("请选择校区:"))]]
        return school_obj

    def select_classes(self):
        li = []
        for key, val in school_all_info["classes"].items():
            li.append("{}.{}".format(val.owner.name, key))
        print("\n".join("{}-{}".format(*i) for i in enumerate(li)))
        classes_obj = school_all_info["classes"][li[int(input("请选择班级:"))].split(".")[-1]]
        return classes_obj

    def create_school(self):
        name = input("请输入学校名:").strip()
        addr = input("请输入学校地址:").strip()
        sc_type = input("请输入学校类型:").strip()
        school_obj = School(name, addr, sc_type)
        school_obj.save(school_all_info)

    def create_classes(self):
        school_obj = self.select_school()
        name = input("请输入班级名字:").strip()
        open_time = input("请输入开班日期:").strip()
        classes_obj = Classes(name, open_time)
        school_obj.add_classes(classes_obj)
        classes_obj.owner = school_obj
        classes_obj.save(school_all_info)

    def create_course(self):
        school_obj = self.select_school()
        classes_obj = self.select_classes()

        name = input("请输入课程名字:").strip()
        period = input("请输入课程周期:").strip()
        price = input("请输入课程价格:").strip()
        course_obj = Course(name, period, price)
        course_obj.owner = classes_obj
        school_obj.add_courses(course_obj)
        course_obj.save(school_all_info)

    def create_teacher(self):
        name = input("请输入老师名字:").strip()
        description = input("请输入对老师的描述:").strip()
        teacher_obj = Teacher(name, description)
        teacher_obj.save(school_all_info)


class TeacherView(BaseView):
    pass


class StudentView(BaseView):
    pass
