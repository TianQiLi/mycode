# 文件夹操作：需要引入系统库os
# 创建目录file
# 移动file 学习相关文件到file
# 重名test.text 为test1.text ；之后恢复原文件名test.text

#学习要点: os 模块是文件操作的基础模块：os.xxx
# os.mkdir(名称) 创建文件夹
# os.rmdir(名称) 删除文件夹
# os.getcwd() 获取当前文件目录
# rename('oldname','newname') 重命名
# chdir(目录) 改变默认目录
# 获取文件当前目录
# remove(文件名) 删除文件
# os.chdir(目录) 改变当前文件的操作目录到其他目录
# os.listdir(目录)  获取文件下的目录列表
import os
# os.mkdir('file')
# os.chdir('')

# os.renames('test.text','test1.text')
#os.renames('test1.text', 'test.text')
# open('test1.text', 'w')
# os.remove('test1.text')

# open('字符串学习.py', 'w')
# os.remove('stringLearn')
l = os.getcwd()
fils = os.listdir(l)
for x in fils:
    if x.find('.') == -1:
        print(f'文件：{x}')
    else:
        print(f'是py{x}')
print(os.listdir(l))
# print(os.getcwd( ))


# open('类学习.py', 'w')

# 在文件夹aa 里面创建文件夹bb
# os.mkdir('aa')
# os.chdir('aa')
# os.mkdir('bb')
# os.rmdir('bb')

# os.chd