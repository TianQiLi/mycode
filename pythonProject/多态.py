# 多态：是一种对象的使用方式，不同的子类调用不同的方法，返回不同的结果

# 具体用法: 定义基类，定义不同的派生类
# 另外的外部类封装公共的方法

class Bird ():
    def fly(self):
        print('基类fly')

class Duck(Bird):
    def fly(self):
        print('duck fly')

class Dove(Bird):
    def fly(self):
        print('dove fly')

class Person(object):
    def hit(self,bird):
        bird.fly()

# 实例
bird1 = Dove()
bird2 = Duck()
person = Person()
person.hit(bird1)
person.hit(bird2)


# open('类属性.py', 'w')