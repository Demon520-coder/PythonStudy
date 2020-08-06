class User():
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.pwd=pwd

    def login(self,name,pwd):
        if name.lower()==(self.user_name.lower()) and pwd.lower()==(self.pwd.lower()):
            return self
        else:
            return None



class AdminUser(User):
    def __init__(self,user_name,pwd):
        super().__init__(user_name,pwd)
        self.privileges=['get','post','add','delete']

    def add_privilege(self,p):
        if p not in self.privileges:
            self.privileges.append(p)
            print('新增权限成功')
            print(self.privileges)
        else:
            print('权限'+p+'已经存在')    

    def remove_privilege(self,p):
        if p in self.privileges:
            self.privileges.remove(p)
            print('移除成功')
            print(self.privileges)
        else:
            print('未找到权限'+p)    
                
                
