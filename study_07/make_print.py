#打印方法
def start_print(print_doc,print_stored):
    while print_doc:
        current=print_doc.pop()
        print_stored.append(current)
    return print_stored


def build_profile(first,last,**user_info):
    '''构建用户的个人信息'''
    profile={}
    profile['first']=first
    profile['last']=last
    for k,v in user_info.items():
        profile[k]=v
    return profile


def make_car(nation,brand,**car_info):
    '''构建汽车信息'''
    car={'nation':nation,'brand':brand.title()}
    for v,k in car_info.items():      
            car[v]=k
    return car


def make_cars(count,nation,brand,**car_info):
    '''构建多辆相同款式的汽车'''
    cars=[]
    while count>0:
        car=make_car(nation,brand,car_info=car_info)
        cars.append(car)
        count-=1
    return cars


def make_cars_v2(count,nation,brand,**car_info):
    cars=[]
    for x in range(0,count):
        cars.append(make_car(nation,brand,car_info=car_info))
    return cars


def is_empty(name):
    '''判断字符串是否为空'''
    if name:
        return False
    elif len(name)==0:
        return True
    else:
        return False    

def do_for(count,message):
    for v in range(0,count):
        print('第'+str(v)+'次输出： '+message)

def make_list_for_count(count,*elements):
    '''根据指定的元素，创建指定元素的集合'''
    if count<=0:
        return []
    temp_list=[]
    if count>len(elements):
        count=len(elements)
    for v in range(0,count):
        temp_list.append(elements[v])
    return temp_list

def make_list_for_count_v2(*elements):
    '''根据列表解析创建列表集合'''
    return [v for v in elements]    