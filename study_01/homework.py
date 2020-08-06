#01.输出一段字符串：
print('This is my first python program')
#02.定义一个变量，并输出大写，小写，首字母大写形式
name='Mr jonh james'
print(name.upper())
print(name.lower())
print(name.title())
#03.去除字符串首位空格、末尾空格、首位空格
address=' Beijin '
print('|'+address+'|')
print('|'+address.lstrip()+'|')
print('|'+address.rstrip()+'|')
print('|'+address.strip()+'|')
#04.定义列表集合，输出集合中的第一个、最后一个，修改其中某一个，删除其中一个元素
names=['zzl','bob','jonh','alice']
print(names[0])
print(names[-1])
names.append('tom') #追加元素
names.append('bruce') 
del names[-1]  #删除最后一个元素
names[0]='zzl_01' #修改第一个元素
#排序:永久排序--->通过集合对象调用排序方法;临时排序:Sorted
beforeSort=names.copy()
print(names)
beforeSort.sort()
print(beforeSort)
print(sorted(names))
print('names len='+str(len(names)))
#05.定义一个数字集合
numbers=list(range(1,30,2))
print(numbers)
#倒序输出
numbers.reverse()
#循环输出列表集合中的元素
for n in numbers:
    print(n)
#输出最大、最小、求和、平均值
print('max='+str(max(numbers)))
print('min='+str(min(numbers)))
print('sum='+str(sum(numbers)))
print('avg='+str(sum(numbers)/len(numbers)))
#计算每个数的平方和
sequarNumbers=[]
for x in numbers:
    sequarNumbers.append(x**2)
print(sequarNumbers)