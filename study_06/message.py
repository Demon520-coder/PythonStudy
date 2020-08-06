#python 函数学习：
def out_put(message):
    """定义了一个函数"""
    print(message)
out_put('This is my first method')

def add(a,b):
    '''ddd'''
    print(str(a+b))
add(3,4)
#关键字实参传递
def show_message(person):
    print(person)
show_message(person=['zzl','001'])
#函数参数指定默认值：
def show_dic(dic={'name':'zzl'}):
    '''传递字典参数'''
    print(dic)
show_dic()
def make_shirt(size,name='I love python'):
    '''size:尺寸大小，name：T恤名称'''
    print('This shirt calls '+name+', size '+str(size))
make_shirt(50,'海南直接')
make_shirt(size=45)
#带有返回值的函数：
def get_full_name(first_name,last_name):
    '''返回完整名称'''
    full_name=first_name+' '+last_name
    return full_name
name=get_full_name('John','Hua')
print(name)
print('----------->')
def get_max_from_list(arr):
    if len(arr)==0:
        return 0
    return max(arr)
print(get_max_from_list([1,2,3]))