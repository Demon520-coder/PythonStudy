class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        self.name=restaurant_name
        self.type=restaurant_type

    def open_restaurant(self):
        print("餐厅正在营业")

    def describe_restaurant(self):
        print("餐厅的名字叫"+self.name+",是一个"+self.type+"餐厅")

    def close_restaurant(self):
        print("餐厅打烊了")