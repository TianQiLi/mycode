import random

# 单行注释 用# 号
'''
多行注释 三个单引号
'''
print('hello tq')

'''
基本设置：界面设置 ;file -> setting ,解释器设置
'''

# 基本类型
'''
1. 数值类型： 整形 int，浮点型 float ; 2. 字符串 str ;  3，布尔  True False  4 列表 list ,[11,222] 5. 集合 {111,222} ;6. 字典{"11":"22"} ;  7 .元组 tuple (aaa,)
'''
"""
1. 第二种多行注释
"""

# 变量 = 值   ；严格区分大小写；不能使用内置关键字
# 命名习惯：大驼峰-MyName，小驼峰-myName，下划线 my_name

lists = [1111, 1222, '8']
print(lists, type(lists))
name = 'ltq'
print(name, type(name))
test = {22, '444'}
print(test, type(test))

test = True
test = False
print(test, type(test))

# 格式化字符串; 字符串：%s ;整数 %d（08d） ;浮点：%f(%.3f 三位)  ;八进制 %o ;十六进制：%x
# 输出多个变量 () 包裹，逗号分割
# 高效格式化语法：f'{表达式} 语法
# 转义符:换行 \n ;制表符 \t
# print 默认自带换行符
# 换行符end = ""
age = 28.0
print('年龄是%08d岁' % age)
print('年龄是%.2f岁' % age)
print('年龄是%s岁' % age)
print('年龄是%s岁,\t对=%s' % (age + 1, test))
print(f'年龄是{age},\n对={test}')

print(age, test, end='\t')

# 输入 input('提示信息') 函数  ,输入内容都会作为   字符串
# name =  input('输入名字：')
# print(f'name ={name}')

# 类型转换 : int () ; str() ;repx(); tuple() ;list(); chr()- unicode  ;hex() - 十六进制 ;eval()
# print(list(age))
# print(chr(age))

# 交互式开发: 用python console

# 运算符  ： //-整除  **- 指数 %-取模
# and 运算符：只要有一个值为0，则结果为0 ，否则结果为最后一个非0 数字
# or 运算符：所有值为0 则为0, 否则结果为第一个非0 数字
# 条件语句：if 条件：
# 条件语句：if 条件： else:
# 注意嵌套if
# 随机函数random
# a = int(input())
# 三目运算符语法： 条件成立的结果 if 表达式 else 条件不成立的结果
# 循环语法：while 条件:语句块  else 循环正常结束     for 变量 in :  else 结束语句块
# 字符串引号有单引号，双引号，三引号 ；如果需要在字符串中显示引号，需要用反斜杠\ 转义
# 字符串常用函数：下标可以省略，表示从整个串
# 1.find ('子串',[起始位置]，[结束位置])   :查找子串位置， 不存在返回-1 ;
# 1.1. rfind() 从右侧查找
# 2. index('子串',[起始位置]，[结束位置]) :查找是子串位置  ；不存在会报错
# 2.1. rindex('子串',[起始位置]，[结束位置]) :从右侧查找是否存在  ；不存在会报错
# 3. count('子串',[起始位置]，[结束位置])  ： 子串出现的次数
# 4. replace(旧的,新的，次数)  ： 次数可以忽略；注意函数返回新串，原来的不变
# 5. capitalize() : 首字母大写 ;  lower (): 全部小写 ； upper() : 全部大写 ; split(): 分割
# 6 . strip ()  删除左右的首位的所有空格  ；lstrip() ;rstrip ()
# 7 . 字符对其： ljust(长度，[占位符]) ;rjust() 右对其 ; center() 中间对其;
# 8. startswith(子串，[开始位置],[结束位置]) : 是否已某个子串开始  ; endswith () 是否以某个子串结束
# 9. isalnum() 是否都是字母，  isdigit() 是否都是数字; isalnum() 字母或者数字 ; isspace() 都是空格
# 10. 元组不可以修改，但是元组里面的列表是可以修改的；列表和元组前者是可变的，后者是不可变的； 另外单个数据的元组的表示注意要加逗号，否则就不是元组了('a',)
# 11. 元组的方法：不支持修改，只支持查找； index(), count() ,len()

# 12字典,初始化方法：{} | dict()：{"a":aaa},方法：keys(); values(); items(): key:value  ；字典是可变类型，有增加修改，删除; del|del() 删除某个数据|键值对；
## clear() 清空字典
# # 字典查找方法：key 查找，如果存在返回value ,否则报错; get(key ,默认值)


# 集合：{} | set() ;注意空集合只能用set() 创建，否则会和字典冲突；集合最大的特点有去重功能
# 集合的操作方法： add(222) ； update(序列) ：追加的是序列
# 集合的删除数据方法： remove(sss)删除指定数据，不存在会报错;discard(sss) 删除指定数据，不存在不会报错; pop() 随机删除一个数据，并返回该数据
# 集合的查找数据: in 判断数据是否在集合；not in 判断是否不在

# 公共方法：
#  + 运算符支持：字符串 ,列表 ，元组  不支持字典
# * 乘号运算符类似加号
#  in | not in  运算符：字符串 ,列表 ，元组 ，字典
# len() : 个数统计
# max():序列最大值；min():序列最小
# del | del() : 删除序列对象| 删除指定数据
# range(start,end ,step) 区间数值

# 推导式：作用是简化代码
# 列表推导式：【xxx for xx in range()】
# 字典推导式：{xx:xx for xxx in xxx}
# 集合推导式：{xx for xxx in xxx}

# 函数的注释用''''; 多个返回值的情况，可以返回元组，列表，字典
# def 函数():
    # '''函数说明'''
    #return 1, 2
    #return {"aaa":"bbb"}
# 函数参数形式：位置参数，关键字参数<无顺序要求>，缺省参数; 既有位置参数又有关键字参数的时候，位置参数必须在关键字参数前面
# test(aa, 关键字=bbb)

# 函数参数形式：不定长参数:包裹位置参数,args 为元组
# def test(*args):
# 函数参数形式：不定长参数:包裹关键字参数,kwargs 为字典
# def test(**kwargs):

#拆包：元组，字典
# a,b =(11,22)
# a,b = {"key1":11,'key2':333}  //获取的是key

# 交换变量： a,b =b,a

# 可变类型：列表，字典，集合
# 不可变类型：整形，浮点型，字符串，元组
# python 中，数据的传递都是通过引用传递的

# 递归
# 函数内部自己调用自己
# 必须有出口，如果没有那么会报错，报错超过最大调用层级

# lambda 语法： lambda 参数列表：表达式
# 如果函数有一个返回值，并且只有一句代码，可以用lambda 表达式
# lambda 类似参数，是一个匿名参数；支持无参，有参，可变位置参数，可变关键字参数
# lambda 带判断的格式： lambda a, b: a if a > b : b  ;类似三目运算符
# lambda 排序应用： 列表.sort(key=lambda x :x["key"] ,reverse= True) ;默认是升序


# 高阶函数：把函数作为参数传入，这样的函数成为高阶函数，高阶函数是函数式编程的体现，函数式编程就是指这种高度抽象的编程范式
# 内置高阶函数如: 求绝对值abs() ;round() 四舍五入
# 高阶函数的作用：化简代码；提高函数的灵活性
# 内置高阶函数：map(fun,list) - 将fun 函数作用到list 里面的每个元素，并重新返回一个新的列表(python2)/迭代器(python3)
# 内置高阶函数：functools.reduce(fun,list) - 将fun 函数每次计算的结果和序列的中的下一个元素做累计计算; fun函数必须有两个参数
# 内置高阶函数：filter(fun,list) - 过滤掉不符合条件的元素，返回一个新的filter 对象，可以用list 转换filer 对象为列表


# 文件读写
# f = open(xxxx,模式)  ：模式-w 写,r  读,a 追加
# # 需要注意模式 w+,r+,a+,wb,rb ,ab 集中模式的区别，主要在于光标的位置
# f.read([count 字节])  ，默认读取所有
# f.readlines() ；按行返回一个列表，每行是一个数据
# f.readline(); 每次读取一行
# f.seek(偏移量，起始位置) ; 起始位置-0 开头 - 1 当前位置，2 结尾
# f.close() 关闭文件，否则会始终占用内存

# 文件备份
# file = open('test.text', 'a')
# file.write('\nccccc')

# 文件操作:依赖os
# os.mkdir() 创建目录
# os.rmdir() 删除目录
# os.rename(old, new) 重命名，文件或者文件夹
# os.chdir() 改变当前默认操作目录
# os.listdir(path) 获取path 下的目录列表
# os.getcwd() 获取当前文件所在目录


# 面对对象
# class name ():
# 定义函数 def xxxx()
# self 表示对象自身
class person ():
    def test ():
        print("method")












# test = lambda a, b=3: a + b
# print(f'lambda 返回{test(1)}')
# test = lambda *args: args
# print(f'lambda 返回{test(1,4,3)}')
# test = lambda **kwargs: kwargs
# print(f'lambda 返回{test(name ="jay", age = 40 )}')

# lambda 排序
# students = [{'name':'zzz','age':20}, {'name':'bbb','age': 25},{'name':'cc','age': 10}]
# students.sort(key=lambda x: x['name'],reverse=True)
# print(students)

# lambda 作为参数传入
# def add_num(a, b, f):
#     return f(a) + f(b)
# print(add_num(1,3,abs))

# map()学习-
# listName = [1,2,3,4]
# def func(x):
#     return x**2
# results = map(func,listName)
# for x in results:
#     print(x)
# print(list(results))

# filter 学习
# def funcFiter(x):
#     return x%2 == 1
# results = filter(funcFiter,listName)
# print(list(results))




# def test (name,age ,sex='男'):
#     '''
#     :param name:
#     :param age:
#     :param sex:
#     :return:
#     '''
#     print("test")
#
# a = {"a":222,"b":"bbb",'c':'d'}
# b = {c: b for c,b in  a.items() }
# print(f'b= {b}')

#// 删除整个字典对象
# del(a)
# del a["c"] 删除字典中的某个键值对
# a['d'] = 'd'  字典增加数据
# print(a.get('aa','返回默认值'))
# for b in a.keys():
#     print(f'{b}')
# for b,c in a.items() :
#     {
#         print(f'{b},{c}')
#     }



# a = 'hello world '
# a.capitalize()
# a.lower().upper().ljust('3','*').split('a')
# a.startswith('hello ')
# a.endswith('hello')
# a.isalnum();
# a.isdigit()
# a.isalnum()
# a.isspace()
# a.isnumeric()
# a = 1
# if a > 10:
#     if a > 20:
#         print('>20')
#     else:
#         print('大于10')
#
# elif a == 5 or a == 4:
#     print('= 5 | 4')
# else:
#     print("小于等于10")
#
# # print('aaaa')
#
#
# b = random.randint(0, 4)
# print(b)
# c = 20
# d = c if b < c else b
# print(d)
# a = 10
# while a > 1:
#         a -= 1
#         print(a)
# else:
#     print('while end')
#
# a = 'sdfbasdfa'
# for c  in a :
#     print(c)
#
# else:
#     print('fo end')
#
# a =''' linda '''
# print(a )
# a =" linda haha "
# print(a )
# #  \转义符号
# a =" linda\' is a woman  "
# print(a )
# print('name = %s' %a)
# print(f'nama is {a}')
# print(a[2])
#
# print(a.find('da'))
# print(a.rfind('da'))
# print(a.find('daa'))
# print(a.index('daa'))
#
# print(a.lstrip())


# a = ('aaa','bbb',222)
# print(f'元组0={a[0]}')










