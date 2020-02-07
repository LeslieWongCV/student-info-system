# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 11:36 PM
# @Author  : Yushuo Wang
# @FileName: stu_admin.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import sys

stulist = [
    {'name': 'Adam', 'age': 20, 'class': 'class03'},
    {'name': 'Issac', 'age': 22, 'class': 'class03'},
    {'name': 'Phenix', 'age': 21, 'class': 'class01'},
    {'name': 'Lee', 'age': 20, 'class': 'class02'},
]

def showstu(stul):
    print('{3:<3} | {0:<10} | {1:<3} | {2}'.format('name', 'age', 'class', 'ID'))
    print('-'*32)
    for i in range(len(stul)):

        print('{3:<3} | {0:<10} | {1:<3} | {2} '.format(stul[i]['name'], stul[i]['age'], stul[i]['class'], i+1))

def showpage():
    print("="*10, '学生信息在线管理', '='*10)
    print('{0:<15}{1:<15}'.format('1.查看学生信息','2.添加学生信息'))
    print('{0:<15}{1:<15}'.format('3.删除学生信息','4.退出系统'))
    print('='*36)

while True:
    showpage()
    selet = input('请输入对应的选择:')
    if selet == '1':
        showstu(stulist)
        input('请按回车继续:')

    elif selet == '2':
        stuname = input('请输入姓名:')
        stuage = input('请输入年龄:')
        stuclass = input('请输入班级:')
        stulist.append({'name': stuname, 'age': stuage, 'class': stuclass})
        input('请按回车继续:')

    elif selet == '3':
        stuID = input('请输入您的ID:')
        while(len(stulist) < int(stuID)):
            print('输入错误，请重新输入:')
            sys.exit(1)
            stuID = input('请输入您的ID:')
            if len(stulist) > int(stuID):
               break
        del stulist[int(stuID)-1]
        print('已成功删除')
        input('请按回车继续:')

    elif selet == '4':
        print('再见')
        break
    else:
        print('Wrong number')





