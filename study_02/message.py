#列表解析：把for循环和创建元素代码合并到一行，并自动附件元素；
numbers=[value**2 for value in range(1,10)]
print(numbers)
numbers=[val for val in range(10,30,3)]
print(numbers)
numbers=[val+2 for val in range(3,20)]
print(numbers)
i=0
for x in numbers:
    print(str(i)+'\t'+str(x))
    i+=1
numbers=[val for val in range(1,1000001)]
print('sum='+str(sum(numbers)))  
#输出第一个元素到第5个元素  
print(numbers[0:5])
print(numbers[2:6])
#不指定开始元素，默认从第一个元素开始
print(numbers[:3])
#获取最后三个元素，注意从负数开始
print(numbers[-3:])
#遍历切片元素
for i in numbers[:4]:
    print(i)
for x in numbers[-4:]:
    print(x)

#复制列表：可以通过切片来复制，切片省略开始和结束索引
myfoods=['rice','noddles','dumplings']
#通过切片复制列表
firendsfoods=myfoods[:]
firendsfoods.append('chuancai')
for f in firendsfoods:
    print(f)
#元组：不可变的列表称为元组，元组中的元素一旦定义不可修改，但是元组变量可以重新赋值;
#元组中的大部分操作和列表集合类似
foods=('米饭','水饺','面条')    
for f in foods:
    print(f)
print(foods[-1])
print(foods[1:])
print(foods[-2])
#复制元组
copy_foods=foods[:]
print(copy_foods)
