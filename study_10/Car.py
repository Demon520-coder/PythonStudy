#python中的继承关系：
#1.父类和子类必须要在同一个python文件中，并且父类在最前面
#2.子类继承父类的时候，通过子类后的小括号传递父类的名称，即表示继承
#3.子类重写父类的方法:在子类中定义一个和父类完全一样的方法，则子类的方法将会覆盖父类的方法
import Battery
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.color='red'
        self.distance=0
        self.oil=0
        
    def description_self(self):
        """描述汽车的信息"""
        print(self.make+' '+self.model+' '+str(self.year))

    def set_year(self,year):
        if year>=0 and year>self.year:
            self.year=year
        else:
            print('设置有误')
        return self

    def increase_distance(self,distance):
        if distance>0 and distance>=self.distance:
            self.distance=distance
        else:
            print('里程设置有误')
        return self

    def increase_oil(self,oil):
        if oil>=self.oil:
            self.oil+=oil
        return self    


#继承
class ElectricCar(Car):
    def __init__(self,make,model,year,price):
        super().__init__(make,model,year)
        self.battery=0
        self.price=price
        self.battery=Battery.Battery('海尔')

    def description(self):
        super().description_self()    
        print(' '+'电量='+str(self.battery)+' 价格='+str(self.price))
        
    def increase_oil(self,oil):
        print('sorry,there is no oil for ElectricCar')
        
    def display(self):
        self.battery.display_size()        


