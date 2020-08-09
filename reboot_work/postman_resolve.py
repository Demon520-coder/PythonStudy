import json
import os


#postman文件解析类
class PostmanResolver():
    def __init__(self,path):
        if path:
            self.path=path
        else:
            raise ValueError('解析路径不能为空')    
          
    def read_from_file(self):
       '''读取文件内容'''
       try:
            with open(self.path,'r',encoding='utf-8') as read_file_object:
                content=read_file_object.read()
            data_obj=json.loads(content)
            data_result=[]
            if 'item' in data_obj.keys():
                data_items=data_obj['item']               
                for v in data_items:                 
                    data_req=v['request']
                    data_temp={'name':v['name']}
                    for n in v:
                        if n!='request':
                           continue
                        else:
                            data_temp['header']=data_req['header']
                            data_temp['payload']=data_req['body']['raw'].strip()
                            data_temp['url']=data_req['url']['raw'].strip()
                            data_result.append(data_temp)
            return data_result
       except FileNotFoundError:
            return []
              
    
    def  write_to_file(self,content,write_path):            
        '''把读取的内容写入指定文件''' 
        if content:
            with open(write_path,'w',encoding='utf-8') as write_file_object:
                 json.dump(content,write_file_object,ensure_ascii=False)
            print('写入成功，文件路径:'+os.path.abspath(write_path))
        else:
            print('没有写入任何内容')     
                   
