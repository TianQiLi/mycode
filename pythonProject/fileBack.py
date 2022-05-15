# 文件备份操作
# 输入备份文件test.text
# 打开，读取文件内容
# 重命名备份文件
# 打开备份文件，写入上面读取到的数据
# 关闭两个文件

# 学习要点1：input() 函数，接收输入内容， open 打开文件 ，read() 读取，close()关闭文件
# 学习要点2：文件的查找函数find(),rfind() ,字符串切片语法[start:end ,step]

# 代码如下
fileName = input('请输入你要备份的文件')
file = open(fileName, 'r')
text = file.read()
file.close()
#
index = fileName.rfind('.')
# 处理备份文件名称，用到了字符串的切片
fileBkName = fileName[:index] + '[备份文件]' + fileName[index:]

fileBk = open(fileBkName, 'w')
fileBk.write(text)
fileBk.close()


