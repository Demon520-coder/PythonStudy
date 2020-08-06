#导入有序字典
from collections import OrderedDict
numbers={'001':'1','002':'2','003':'3'}
for k,v in numbers.items():
    print(k+'='+v)
numbers2={}
numbers['01']='1'
numbers['02']='2'
numbers['03']='3'
for x,y in numbers2.items():
    print(x+'='+y)    