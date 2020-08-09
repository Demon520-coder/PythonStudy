import json
'''文件读写帮助类'''
class FileHelper():
    def __init__(self,path):
        if path:
            self.path=path
        else:          
            print('路径无效')

    
    def write(self,content,mode):
        '''写入文件'''
        with open(self.path,mode,encoding='utf-8') as write_file:
            write_file.writelines(content)

    def write_append(self,content):
        self.write(content,'a')

    def read(self):
        with open(self.path,'r',encoding='utf-8') as read_file:
            content=read_file.read()
        return content

    def read_lines(self):
         with open(self.path) as read_files:
             lines=read_files.readlines()
         return lines           
    
    def remove_content(self):
        self.write('','w')

    def write_to_json(self,content={},ensure=False):
        with open(self.path,'w',encoding='utf-8') as json_writter:
            json.dump(content,json_writter,ensure_ascii=ensure)

    def json_to_object(self):
        content=self.read()
        obj= json.loads(content,encoding='utf-8')
        return obj
