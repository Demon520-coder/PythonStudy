print('Hello world!')
message='This is my first python program'
print(message)
message='my love'
#单词首字母大写
print(message.title())
#所有字母小写
print(message.lower())
#所有字母大写
print(message.upper())
message='my love '
#去掉字符串末尾空格
print(message.rstrip())
flag=' python '
message="\n\tmessage-->'"+flag+"'"
print(message)
flag=flag.rstrip()
message="message-->'"+flag+"'"
print(message)
#去掉字符串前导空格
flag=flag.lstrip()
message="message-->'"+flag+"'"
print(message)
flag=' python '
#去掉字符串前导和末尾空格
flag=flag.strip()
message="message-->'"+flag+"'"
print(message)
message='message-->"message"'
print(message)
#python的类型可以任意指定，此举可能会引起数据类型问题？
message=123
print(message)
#定义一个数组,数组中可以存储不同类型的数据
students=['zzl','jonh','bob','jim']
#输出数组
print(students)
#集合中添加新的元素
students.append('tom')
students.append(['lucy','ok'])
print(students)
#输出计集合最后一个元素
print(students[-1])
students.append(123)
print(students)
#删除指定元素
students.remove(students[-1])
print(students)
students.remove(students[-1])
print(students)
#插入元素到指定位置
students.insert(0,'insert_0')
print(students)
students.insert(-1,'insert_-1')
print(students)
#反转集合中的元素
students.reverse()
print(students)
age=23
#注意：python中,字符串不能和其他非字符串类型混合连接，必须要把其他类型的转换为字符串，通过str()函数
msg='Today is my '+str(age)+' birthday'
#修改集合中的元素
students[2]='students_2'
print(students)
#删除集合末尾元素(默认),并返回它
el=students.pop()
print(el)
#删除集合第二个元素，并返回它
el2=students.pop(1)
print(el2)
print(students)
#删除集合中的第一个元素，并且不会返回它
del students[0]
print(students)
#sort对集合的排序是永久性的，也就是说会永久改变集合中元素的顺序
students.sort()
print(students)
students.sort(reverse=True)
#sorted函数可以临时改变集合的顺序
names=['h','a','c','e','f']
print('未排序前:\n')
print(names)
print('排序后:\n')
print(sorted(names))
print('源集合:')
print(names)
#获得列表的长度
print('列表长度:'+str(len(names)))
#循环列表集合,注意最后有一个英文冒号
#python中根据代码的缩进判断前一行代码与下一行代码之间的关系
#如果下一行代码与前一行代码有关系，则应该使用缩进，在for循环中，必须指定缩进，这样python才知道for循环的下一行语句从何开始
for name in names:
    print(name)
    break
nums=range(1,20,2)
print(nums)
for i in nums:
    print(i)
for x in range(2,6):
    print(x)
#将range()返回的结果转换为列表集合    
nums=list(nums)
nums.reverse()
print(nums)
seq=list(range(1,10))
seqlist=[]
for i in seq:
    #平方
    i=i**2
    seqlist.append(i)
print(seq)
print(seqlist)    
#求列表的最大值
print(max(seqlist))
#求列表的最小值
print(min(seqlist))
#求列表集合的总和
print(sum(seqlist))
#计算列表集合的平均值
print(sum(seqlist)/len(seqlist))