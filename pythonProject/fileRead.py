# 文件读写操作
# 打开一个文件
# 写入内容
# 关闭文件

# 打开test.text
# 读取文件
# 打印输入

# import os
# 学习要点：open(),write(),read(字节长度) ，close()  ,readlines() ,readline()
# 文件读写的模式：w-写，r-读，a-追加 , w+- 读写，会覆盖原文件， r+ - 读写，会覆盖原文件 ，rb-以二进制读取文件 ，wb+ 二进制写入文件

f = open('test.text', 'w+')
f.write('aaaa,bbbb,\nccccc\nddddd')
f.close()

f = open('test.text')
# 需要注意，调用过read 之后，光标就到了最后，再次调用就会读取为空，除非手动seek() 到开头
print(f'文件内容如下:{f.read()}')
f.seek(0)
print(f'按行读取所有行{f.readlines()}')
f.seek(0)
while True:
    con = f.readline()
    if len(con) == 0:
        break
    print(f'按行读取{con}')
f.close()


