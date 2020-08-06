class Student():
    def __init__(self,name,gender,age):
        '''初始化一个学生对象'''
        self.name=name
        self.gender=gender
        self.age=age

    def print_stu_info(self):
        '''输出学生的信息'''
        print(self.name+"|"+self.gender+"|"+str(self.age))    

    def study(self,*subjects):
        '''学生学习的科目'''
        #判断集合或字符串是否为空       
        if subjects:
            print("学生"+self.name+"学习的科目有:")
            for s in subjects:
                print(s)
        else:
            print("学生"+self.name+"没有学习的课程")
        
          
