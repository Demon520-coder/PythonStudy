from file_helper import FileHelper
#创建程序存储用户输入的个人信息
u_name=input('input your name\n')
u_gender=input('input your gender\n')
u_age=input('input your age\n')
f_h=FileHelper(r'study_11\user_info.txt')
f_h.write_append(u_name+'\n')
f_h.write_append(u_gender+'\n')
f_h.write_append(u_age+'\n')
print('==========读取个人信息=========')
content= f_h.read()
print(content)
print('==========序列化存储=========')
f_h.remove_content()
user={'name':u_name,'gender':u_gender,'age':u_age}
f_h.write_to_json(user)
obj= f_h.json_to_object()
print(obj['name']+'_'+obj['gender']+'_'+obj['age'])