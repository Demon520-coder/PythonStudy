import Dog as D
import Student as Stu
import Restaurant as Res
my_dog=D.Dog("二哈",5)
my_dog.sit()
my_dog.show()
my_dog.roll_over()

count=[x for x in range(0,5)]
dogs=[]
for v in count:
    dogs.append(D.Dog("name_"+str(v),v))

a=0
for d in dogs:
    print(d.name)
    a+=d.age
print(a)
print("===============")
s=Stu.Student("zzl",'男',35)
s.print_stu_info()
s.study('Chinese','English','French')
print("===========")
s.study()
print("==============")
r=Res.Restaurant("福味居","粤菜")
r.open_restaurant()
r.describe_restaurant()
r.close_restaurant()






