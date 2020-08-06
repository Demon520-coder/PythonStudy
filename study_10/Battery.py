class Battery():
    def __init__(self,brand,size=0):
        self.brand=brand
        self.size=size

    def charge(self,percent):
        if percent>0:
            self.size+=percent

    def display_size(self):
        print('There has '+str(self.size)+'V for using')            


    def get_range(self):
        if self.size==100:
            range=70
        elif self.size==85:
            range=50
        else:
            range=10

        message='This car can go through about '+str(range)+' mails'
        print(message)
