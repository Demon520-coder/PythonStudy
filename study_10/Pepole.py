class Pepole():
    def __init__(self,name,age,nation):
        self.name=name
        self.age=age
        self.nation=nation
        self.lanuage='Chinese'
      
    def append_age(self,step):
        if step>0:
            self.age+=step
        else:
            print('输入有误')    
        return self    


    def change_name(self,name):
        '''更改姓名'''
        if name:
            self.name=name
        return self    

    def change_nation(self,nation):
        '''更该国籍'''
        if nation:
            self.nation=nation
        return self    

    def show_info(self):
        '''显示个人信息'''
        print(self.get_personal_info())

    def get_personal_info(self):
        return self.name+'_'+self.nation+'_'+str(self.age)+'_'+self.lanuage

    def write_to_file(self):
        with open('person.txt','w',encoding='utf-8') as write_object:        
            write_object.writelines(self.get_personal_info())