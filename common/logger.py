# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 18:46
# @Author : YangWeiMin

import os
import logging
import time

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')

if not os.path.exists(log_path):os.mkdir(log_path)

class Log(object):
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger() #实例化一个logger对象
        self.logger.setLevel(logging.DEBUG) #设置日志级别
        # 日志的输出格式
        self.formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

    def console(self,level,message):
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8') #将记录器产生的日志记录发送至指定磁盘
        fh.setLevel(logging.DEBUG)  #设置日志级别，只有日志级别大于等于才会输出
        fh.setFormatter(self.formatter) #设置日志输出格式
        self.logger.addHandler(fh)   #为实例logger增加一个处理器

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        # 避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()


    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

    def critical(self,message):
        self.console('critical', message)

