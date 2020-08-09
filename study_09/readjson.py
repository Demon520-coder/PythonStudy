#导入json包
import json
import os
print("请将文件拷贝到当前python程序所在文件夹下，并以collection结尾,扩展名为.json")
print("======开始读取======")
current_files=os.listdir()
json_read_file={'file':r'Study_09\postman_collection.json'}

# for f in current_files:
#     if f.endswith('collection.json'):
#       json_read_file['file']=f
#       break

if json_read_file['file']:
    file_name=json_read_file['file']
    try:
        with open(file_name,'r',encoding='utf-8') as json_file:
            contents=json_file.read()
    except FileNotFoundError:
        print('sorry,the file '+file_name+'not exist')    

    data= json.loads(contents)
    #解析数据
    if 'item' in data.keys():
        data_items=data['item']
        data_arr=[]
        for v in data_items:                  
            for x in v: 
                temp=v['request']                      
                obj={'name':v['name']}
                obj['header']=temp['header']
                obj['payload']=(temp['body']['raw']).strip()
                obj['url']=(temp['url']['raw']).strip()
                data_arr.append(obj)
                                                
        #写入数据
        with open('postman.json','w',encoding='utf-8') as json_file_write:
            json.dump(data_arr,json_file_write,ensure_ascii=False,indent=4)

    print("======写入完毕======")
    print('文件已经成功写入到路径:'+os.path.abspath(os.curdir)+'\\postman.json')
    q=input('退出.....Y/N\n')
    if q.lower()=='y':
        print('退出成功')
else:
    print('未发现postmane collection文件')
    input('')   


