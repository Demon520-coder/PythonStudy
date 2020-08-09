#python读取文件：使用with open()结构，它会在文件读取完毕自动关闭
# with open('.\\study_11\\test.txt','w',encoding='utf-8') as write_file:
#     write_file.writelines('我是中国人民解放军')
#此处注意文件的路径：1) VS Code运行时会以vs code terminal控制台cd的文件路径为当前运行路径，
# 需要根据此路径确定读取文件的路径或者直接使用绝对路径
#再python中，可以再字符前加r表示不对字符串中的'\'转义
#注意：python好像没没有局部变量啊，所有定义变量一定要慎重，避免定义的变量覆盖前面的同名变量值

try:
    with open('news.txt','r',encoding='utf-8') as read_file:
        print(read_file.read())
except FileNotFoundError:
    print('未找到文件')        

print('---------------->')

with open(r'D:\Study\python\study_11\news.txt','r',encoding='utf-8') as read_news_file:
    print(read_news_file.read())

print('------------------------------->')
with open('.\\python_work_files\\personal.txt') as read_person_file:
    print(read_person_file.read())

print('------------->')

#读取整个文件:
with open(r'study_11\index.html','r',encoding='utf-8') as read_index_file:
    print(read_index_file.read())

#逐行读取：
with open(r'study_11\index.html','r',encoding='utf-8') as read_index_on_line:
    # lines=read_index_on_line.readlines()
    # if read_index_on_line==None:
    #     print('none')
    for l in read_index_on_line:
        print(l.rstrip())
        print('===============')

for v in range(1,10):
    print(v)

print('==============')
print(v)    
print('=============')
print(l)
print('====================')
#print(lines)
with open(r'study_11\test.txt','r',encoding='utf-8') as read_test_files:
    f_lines=read_test_files.readlines()

print(f_lines)
print('===================开始写入文件==============')
numbers=[x for x in range(1,20)]
str_numbers=''
for n in numbers:
    str_numbers+=str(n)
with open(r'study_11\num.txt','w',encoding='utf-8') as write_num_files:
    write_num_files.write(str_numbers+'\n')
    write_num_files.writelines(str_numbers)    
#追加内容到指定文件:
with open(r'study_11\num.txt','a',encoding='utf-8') as write_append_files:
    write_append_files.writelines('\n这是追加的内容啊')    

with open(r'study_11\num.txt','a',encoding='utf-8') as write_append_files:
    write_append_files.writelines('这是追加的内容啊22222')    