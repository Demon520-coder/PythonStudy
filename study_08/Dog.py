#创建类：
#注意点：1.约定类的首字母大写;2.类的构造函数为:__init__;3.类中的每一个方法都必须传递self形参，因为python在创建实例时会自动传递self;
#3.python类没有构造函数重载;

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
  
    def sit(self):
        print("This dog has beeb sit")

    def show(self):
        msg="Dog's name is "+self.name+"\n"
        msg+="Dog's age is "+str(self.age)+"years"
        print(msg)
    
    def roll_over(self):
        print("Look!This dog can roll over!!!")