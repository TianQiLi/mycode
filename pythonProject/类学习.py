# 类的方法：__init__  初始化方法，可以用于设置默认值参数
# 类的继承，括号内填写父类 ，默认继承object
# 类的多继承，括号内父类逗号分割，默认继承第一个父类的同名方法和参数
# 魔法方法: __str__
class Cooker():
    def __init__(self):
        self.time = 1
        self.status = ''

    def cooking(self, time):
        self.time += time
        if self.time < 10:
            self.status = '不熟了'
            # print('不熟了')
        elif self.time <= 10:
            self.status = '半熟了'
        else:
            self.status = "输了，可以吃了"

    def __str__(self):
        return f'self.time ={self.time},状态={self.status}'

    def __del__(self):
        print("对象销毁")


test = Cooker()
test.cooking(3)
print(test)
# open('魔法方法.py','w')

