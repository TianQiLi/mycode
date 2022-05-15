# 静态方法 用装饰器@staticmethod 修饰，静态方法不需要传递类对象，也不需要传递实例对象，形参没有self/cls
# 静态方法能够通过 类对象 或者  实例对象访问

# 使用场景：当不需要使用实例对象，属性，也不需要使用类对象，类属性，类方法的时候
# 优点：取消不必要的参数传递，可以减少内存占用和性能消耗

class Person ():
    @staticmethod
    def eat():
        print('static method eat')

Person.eat()
person = Person()
person.eat()

# open('异常.py','w')