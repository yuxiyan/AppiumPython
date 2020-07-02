# -*- coding:utf-8 -*-

import yaml
import os

# 获取当前文件的上一层路径


cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
caps_path = os.path.join(os.path.join(cur_path,'config'),'yuxiyan_yml.yml')
print(cur_path)

def read_caps():
    with open(caps_path,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data



def get_yml(f):
    with open(f,'r',encoding="utf-8") as f:
        data =yaml.load(f,Loader=yaml.FullLoader)
        return data

