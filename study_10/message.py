#python类的创建和使用
import Pepole as p
import Car as c
import User as u
p1=p.Pepole('zzl',28,'China')
#python链式编程:返回self即可
print(p1.change_name('zzl_001').change_nation('England').append_age(4).append_age(-9).get_personal_info())
print('========继承===========')
ec=c.ElectricCar('i5','bmw',2007,1000000)
ec.description()
ec.set_year(2020).increase_distance(30)
ec.description()
ec.increase_oil(0)
ec.battery.charge(50)
ec.display()
ec.battery.charge(200)
ec.battery.get_range()
print('========================')
test_user=u.AdminUser('zzl','123456')
u_name=input('请输入用户名:\n')
u_pwd=input('请输入密码:\n')
login_result= test_user.login(u_name,u_pwd)
if login_result==None:
    print('登录失败')
else:
    print('登录成功')
print('===========')
print('拥有的权限有：')
for v in test_user.privileges:
    print(v)    
test_user.add_privilege('read')
test_user.add_privilege('read')
print('===============')
test_user.remove_privilege('x')
print('===============')
test_user.remove_privilege('read')   