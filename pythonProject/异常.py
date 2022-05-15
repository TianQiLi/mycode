# 异常语法 ： try: except: else: finally:
# Exception 是所有异常的基类 ，可以用这个去获取不同类型的异常
# time 库 ，time.sleep() 用于执行停留
# 自定义Error 需要继承Exception 基类，重写__str__方法
# 代码1
try:
    print(name)
except Exception  as results :
    print(f'异常except捕获f{results}')
else:
    print('没有异常执行的代码')
finally:
    print('final 最终都会执行的代码，可以用于文件关闭')

# 代码1
import time
try:
    f = open('test.text')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            else:
                time.sleep(1)
                print(con)

    except Exception as error:
        print(f'子层except{error}')
    finally:
        f.close()


except Exception as error:
    print(f'外层except{error}')


class CustomError(Exception):
    def __str__(self):
        print()

# open('导入_包.py','w')