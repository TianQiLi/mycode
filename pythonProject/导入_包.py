# 导入模块的两种方法
# import 模块
# from 模块 import 功能名称
# from 模块 import *  配合__all__ 系统变量

import os

# os.mkdir('cc')
# os.rmdir('cc')
# os.rmdir('bb')

def del_all_dir(path):
    if len(path) == 0:
        path = os.curdir

    try:
        list = os.listdir(path)
        for f in list:
            if os.path.isdir(f) & os.path.exists(f) == True:
                info = os.utime(f)
                info2 = os.stat(f)
                print(info)
                print(info2)
                # del_all_dir(f)
                # os.rmdir(f)
            elif os.path.isdir(f):
                # os.rmdir(f)
                print(f'移除dir:{f}')
            # else:
                # print(f'不是空{f}')
    except Exception as error:
        print(error)

del_all_dir("")
