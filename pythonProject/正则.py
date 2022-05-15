# 正则：次数限定符，区间限定符
# re.match() 查找符合的字符串返回match 对象
# re.search() 查找首次符合的字符串返回match 对象
# re.findall() 查找所有符合的字符串返回match 对象的列表
# > “match()和search()都只匹配一个结果,但是match()是从字符串的开头开始匹配的,如果匹配的字符不是在开头处,那么它将会报错,匹配成功返回结果,没有返回None。
# > 而search()是从头开始匹配,匹配整一个字符串得出结果。”
import re
test = 'ss{#qingteng?/tg#}iuy'

# test = '{#qingteng?/tg#}'
# pattern = '{#[a-z]+\?/[a-z]{2}#}'
pattern = '{#\w+\?/[a-z]{2}#}'
match = re.match(pattern,test)
# print(match.group())
print(re.search(pattern,test))
print(re.findall(pattern,test))