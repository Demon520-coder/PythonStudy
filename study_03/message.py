#01.列表解析：
numbers=[val for val in range(0,20)]
print(numbers)
#列表切片：完整切片相当于复制
numbers2=numbers[:]
print(numbers2)
print(numbers2[-1:])
print(numbers2[1:3])
#python条件：pytho中冒号相当于c#中的花括号，表示下一条语句的开始
cars=['bmw','honda','toyoto','byd']
for c in cars:
    if c=='bmw':
        print(c.upper())
    else:
        print(c.title())
#列表解析：
cars2=[c for c in cars]
print(cars2)
for x in cars2:
    if x=='bmw' or x=='byd':
        print(x.upper())
    else:
        print(x.title())
books=['c#','javascript','python','swift','sql']
if 'c#' in books:
    print('c#')
if 'c#' not in books:    
    books.append('c#')
else:
    books.remove('c#')    
print(books)
if 'go' not in books:
    books.append('go')
print(books)    
if 'go' in books:
    books.remove('go')
    books.append('GO')
    print(books)
car='bmw'.upper()
print(car=='bmw')
print(car=='BMW')
name='zzl'
name+='01'
print(name=='zzl' and '01')
print('------->')
print(1>2 and 1==3)
print(1==0 or 1==1)
print(1>0 and 2>1)
print('------->')
ages=[18,17]
for age in ages:
    if age<18:
        print('你还未成年，无法操作')
        print('----->')
        break
ages.append(14)
ages.append(39)
ages.remove(17)
for a in ages:
    if a==18:
        print('成年了哦')
    elif a<18:
        print('未成年啊')
    else:
        print('你已经是老司机了')
#判断列表是否为空：
foods=[]
if foods:
    print('列表为空')
else:
    foods.append('rice')
print(foods)   
goods=[]
if len(goods)==0:
   temp=['book','bread','clothe','pens']
   for g in temp:
       if g=='book':
           print(g+'has exists')
       else:
           goods.append(g)    
print(goods)
print('============')
students=['zzl','xiaoA','long','lisi','2b','zzl','2b']
#去重
new_students=[]
for s in students:
    if s not in new_students:
        new_students.append(s)
print(new_students)
print('=============')
#列表集合的连接
languages=['Chinese','English','Janpanese','French']
conacts=''
for l in languages:
    conacts=conacts+l+','
print('=============')
print(conacts.rstrip(','))