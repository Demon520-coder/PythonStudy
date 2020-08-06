#输入
print('python input')
message=input('input\n')
print(message)
print('==============')
unconfirm_users=[]
# flag=True
while True:
    user=input('enter your name,please\n')
    if user not in unconfirm_users:
        unconfirm_users.append(user)
    else:
        print('name has been existed')
    if len(unconfirm_users)==3:
        break
print(unconfirm_users)
print('================')
confirm_users=['bob','tom','alice','lucy']
while confirm_users:
   print(confirm_users.pop())
print('================')
array=[1,2,3,4,5,6]
number=0
while array:
    if number<len(array):
        print(array[number])
        number+=1
    else:
        break
#删除包含指定值的所有列表元素：
elments=['html','ul','head','div','p','img','a','li','i','html','head','div']
e='div'
i=0
while e in elments: 
   if i>=1:
       elments.remove(e)
   i+=1

print(elments)
print('=============')
#定义三明治列表集合
sandwitch_orders=['organge','banana','apple','greetea']
finished_orders=[]
#使用两种方法遍历列表集合：
print('=======第一种：for循环========')
for s in sandwitch_orders:
    finished_orders.append(s)
    print(s+'制作完毕')
print('=======第二种：while循环======')    
idx=len(sandwitch_orders)
while idx>=0:
    idx-=1
    print(sandwitch_orders[idx])
   
print('---------->')
while sandwitch_orders:
    sandwitch=sandwitch_orders.pop()
    finished_orders.append(sandwitch)
    print(sandwitch+'制作完毕')
print('==========梦想调查=========')
dic={}
name=input('what is your name?')
dic['name']=name
age=input('How old are you?')
dic['age']=age  
address=input('Where are you from?')
dic['address']=address
gender=input('Are you a man or woman?')
dic['gender']=gender
print(dic) 