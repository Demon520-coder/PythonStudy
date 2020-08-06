#字典学习,python中的字典和js中的对象差不多，对象的访问通过键来访问
dic={'name':'zzl','age':35,'address':'陕西省西安市未央区'}
print(dic) 
print(dic['name'])
dic['name']='zzl_001' #修改字典某一项的值
print(dic)
del dic['name']
print(dic)
#字典遍历：同k,v的形式遍历
for key,value in dic.items():
    print(key+':'+str(value))
print('==========')
#获得字典的所有键dic.keys()
keys=dic.keys()
for k in keys:
    print(k)
#获得字典的所有值：dic.values()
vals=dic.values()
print(vals)    
if 'name' not in dic.keys():
    dic['name']='zzl_dic'
print(dic)
if 'name' in dic.keys():
   print('name has exists')
favorite_lan={
    'john':'c#',
    'phil':'python',
    'jen':'go'
}
for n in favorite_lan.keys():
    print('"key"="'+favorite_lan[n]+'"\n')

print('thank you very '+
     'much'+
     '! my dear friend')
print('==============================')
#字典集合
dicts=[{'name':'001','gender':'man','score':'101'},
       {'name':'002','gender':'man','score':'102'},
       {'name':'003','gender':'man','score':'103'},
       {'name':'004','gender':'man','score':'104'},
       {'name':'005','gender':'man','score':'105'}
    ]   
for d in dicts:
    temp=list(d.keys())
    for x in d.keys():
        print('"key"="'+x+'"')
        print('"value=""'+d[x]+'"')
        if x==temp[-1]:
            print('-------------->')
dic_keys=d.keys()
print((list(dic_keys))[-1])
print('============================')
pepole={
    'name':'zzl',
    'favorite':['programmer','play games','sleep']
}
for p in pepole.keys():
    if p=='favorite':
        for f in pepole[p]:
            print(f.title())
