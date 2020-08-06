#导入模块
#导入多级模块
import helper.message_helper as output_helper
#import make_print
#导入模块，并且给模块起别名
import make_print as mp
#导入模块中的方法
from caculate import make_full_name as mk
#导入模块中的多个方法，并分别给方法起别名
from caculate import make_sum as ms, make_divide as md
#python方法中的任意数量实参，类似于C#中的params参数
def make_pizze(size,*others):
    print('pizze size='+str(size)+'\n')
    for o in others:
        print(o)
make_pizze(30,'orange','salt','bread')        
make_pizze(40)
make_pizze(50,3,'banana')
#ptyon中还可以添加任意数量关键字实参，任意数量关键字实参最终会转化为字典
def get_info(nation,**person):
    print('nation is'+nation+'\n')
    for k,v in person.items():
        print(k+'='+v)
get_info('china')
print('-------------')
get_info('china',name='zzl',age='35',address='陕西省汉中市',profession='computer')
#调用模块中的方法
result= mp.start_print(['zzl','001'],[])
print(result)
print('--------->')
print(mk('Jhon','tom'))
print('----------->')
#:任意数量关键之实参，其实体现在形参上是一个字典集合
user_info=mp.build_profile('zzl','001',height=138,weight=38,profession='programmer')
print(user_info)
print('---------->')
car=mp.make_car('china','byd',color='red',seats=4,length=3)
print(car)
print('-------------->')
cars=mp.make_cars_v2(5,'china','byd',color='orange',price=15,seats=4)
print(cars)
print('-------------->')

print(mp.is_empty(''))
print(mp.is_empty(' '))
print(mp.is_empty('zzl'))
print(len(' '))
temp=' '.split(' ')
print(temp)

temp=mp.make_list_for_count(5,'zzl','001','003')
print(temp)
print('-------->')
print(mp.make_list_for_count(-3,'zzl','003'))
print('------->')
print(mp.make_list_for_count_v2('001','002'))
print('------->')
arr=['004',45,'001',{'name':'zzl','age':45},['4000','3333']]
#切片复制
arr_copy=arr[:]
print('arr_copy')
print(arr_copy)
#列表解析复制
arr_copy_for=[x for x in arr]
print('arr_copy_for')
print(arr_copy_for)
print('------------>')
arr_numbers=[]
for x in range(0,20):
    arr_numbers.append(x)
print(arr_numbers)    

print('-----多级模块中方法-------')
output_helper.show_message('zzl','china','shanxi','hanzhong')
