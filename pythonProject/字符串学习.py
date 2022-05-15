# 字符串常用函数
# find() 查找子串是否存在,不存在返回-1；存在返回下标
# index() 查找子串,存在返回下标，不存在则报错
# rfind() 从右边查找
# rindex() 从右边查找
# count('子串',开始,结束) 查找子串出现的次数


# 格式化字符串的方式：四种方式
# 1. 加号拼接
# 2. str.join() 链接:用于集合类重组为字符串，需要添加分隔符等
# 3. format 方式： 模板字符串.format(xx)
# 4. 直接拼接
# 模板字符串类型：<>^ ：对其 ，.f:精度的 ,逗号：千分位的, 字符串长度的，进制表示的:b,x,d,o,X,c
# b:二进制 ,x:十六进制, o:八进制，d：十进制，c:unicode

# 字符串去重：可以遍历用not in ，也可以用集合，集合是无序的不重复的

# 不同的进制表示法
import os

str1 = 'hello'
str2 = 'world'
print(str1 + str2)
print('*'.join([str1, str2]))
print(str1, str2)
# 格式化字符串又有三种
print('%s%s' % (str1, str2))
print(f'{str1}{str2}')
print('{0}{1}'.format(str1, str2))


# 格式化
a = 12
print('{0:b}'.format(a))
print('{0:b},{0:o},{0:x},{0:c},{0:d},{0:X}'.format(a))
# 浮点数小数
a = 1.123345
print('{0:.2f}'.format(a))
# 字符串取固定长度的
a = 'helloworld'
print('{0:3}'.format(a))
# 千分位
a = 123456
print('{0:,}'.format(a))
# 对齐
print('{0:#<10}'.format(a))
print('{0:*>10}'.format(a))


a = 'hello123你好'


#
# open('正则.py','w')
# os.remove('字符串编解码')

