# 类属性就是类  所拥有的的属性，被类的所有实例属性所共享
# 类属性可以使用类对象 或实例属性 访问
# 类属性只能通过类对象修改，不能通过实例对象修改；通过实例修改类属性其实就是定义了一个实例变量


# 类属性优点
# 记录某一项属性保持不变时，则定义类属性
# 实例属性要求每个对象单独开辟一份内存空间 来记录数据，而类属性为全类所共有，仅占一份内存，节省空间

# 类方法
# 方法前面用@classmethod 修饰
# 和类属性配合使用，如访问私有类属性

class Bird(object):
    # 类属性
    age = 100
    # 私有类属性
    __isAnimal = True
    # 实例属性

    def __init__(self):
        self.name = '鸟'

    @classmethod
    def isAnimal(cls):
        return cls.__isAnimal


bird = Bird()
print(f'类访问-类属性{Bird.age}')
print(f'实例访问-类属性{bird.age}')
print(f'实例属性  {bird.name}')

# 类方法
print(bird.isAnimal())

# 修改类属性
Bird.age = 200
print(f'修改类属性：{Bird.age}')

bird.age = 300;
print(f'实例修改类属性：{Bird.age}')
print(f'修改类属性：{bird.age}')

# open('静态方法.py','w')

