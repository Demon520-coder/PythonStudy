import random

class Die():
    def __init__(self,sides=6):
        """初始化骰子"""
        '''骰子的面数'''
        self.sides=sides

    def roll_die(self):
        '''掷骰子'''
        return random.randint(1,6)

input_str=input('开始掷骰子?(Y/N)\n')
if input_str.lower()=='y':
    d=Die()
    while True:
        n=d.roll_die()
        if n<=3:
            print('你掷出了'+str(n)+'!继续加油哦')
        else:
            print('厉害！掷出了'+str(n)+'!')    
        s=input('再掷一次(Y/N)\n')
        if s.lower()=='n':
            break

    