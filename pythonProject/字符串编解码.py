# 字符串最早的编码是美国的ASCII 码， 最多表示256 个符号，一个符号一个字节
# 中文编码：GBK ,GB2312 是我国指定的编码，英文一个字节，中文两个字节
# 中文编码：UTF-8 ，国际通用编码，英文一个字节，中文三个字节
# errors : igonre -忽略, replace- 替换，strict:严格类型，非法字符会报错
# 字符串编码解码：
# 编码：转换成二进制
# 解码：转换成字符串

a = 'hello 你好'
# 编解码
print('编码')
a_code = a.encode('UTF-8',errors='ignore')
print(a_code)
print(a.encode('GBK',errors='ignore'))
print(a.encode('GB2312',errors='ignore'))
print('解码')
print(a_code.decode('UTF-8',errors='ignore'))
print(bytes.decode(a_code,'UTF-8'))
# print(str.decode(a,'GBK',errors='ignore'))