#导入postman解析类
from postman_resolve import PostmanResolver

#创建postman解析类对象
p=PostmanResolver(r'.\study_09\postman_collection.json')
#读取postman解析文件
content= p.read_from_file()
#输出解析结果
print(content)
print('==================')
#解析结果写入指定文件
p.write_to_file(content,r'postman.json')
