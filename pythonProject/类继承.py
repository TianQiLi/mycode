# 类继承,默认从python3 开始，默认继承object，多继承的话，逗号隔开
# pass 关键字 就是什么也不做，只是为了防止语法错误
# 如果继承多个类，那么优先继承第一个类的同名属性和方法
# 重写：子类重写父类，调用子类的重写方法
# 查看类继承关系方法：类.__mro__

# 子类对象如何调用父类的重名函数
# # 调用父类同名方法，为了保证调用到的也是父类的属性，必须在调用父类方法之前调用父类的初始化方法
# # 如果先调用父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，必须先调用子类自己的初始化方法

# super 关键字，super 会自动查找父类
# # super 有参数写法 super(当前类，self)  ；类的改动需要维护，比较麻烦，建议无参数写法
# # super 无参数写法 super()

# 私有属性，方法声明，用前缀__ 表示 ，子类不会继承，不可以访问



class Cooker(object):
    def __init__(self):
        self.time = 1
        self.status = ''
        self.name = '师傅'
        # 私有属性
        self.__age = 20
        # 私有方法

    def __isCouple(self):
        print("是否有对象")

    def cooking(self, time):
        self.time += time
        if self.time < 10:
            self.status = '不熟了'
            # print('不熟了')
        elif self.time <= 10:
            self.status = '半熟了'
        else:
            self.status = "输了，可以吃了"

    def eat(self):
        print(f'{self.name}.父类eat')

    def __str__(self):
        return f'self.time ={self.time},状态={self.status},age = {self.__age},有对象？={self.__isCouple()}'

    def __del__(self):
        print("对象销毁")


# 派生类
class SecondCooker(Cooker):
    # pass
    # def __init__(self):
    #     # self.name = "徒弟"

    def test(self):
        print('tset')

    def eat(self):
        # super(SecondCooker, self).eat()
        # super().eat()
        self.__init__()
        print(f'{self.name}.子类eat')

    # 注意形参self
    def eatForsuper(self):
        Cooker.__init__(self)
        Cooker.eat(self)


test2 = SecondCooker()
# test2.cooking(30)
# test2.eat()
# test2.eatForsuper()
# test2.eat()
# test2.__isc
print(test2)

