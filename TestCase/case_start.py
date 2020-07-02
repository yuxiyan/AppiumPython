# -*- coding:utf-8 -*-
# @Time   : 2018-11-05 19:48
# @Author : YangWeiMin

import unittest
from Page.StartPage import Start

import time
from common.logger import Log

class CaseLogin(Start,unittest.TestCase):

    log = Log()

    def test_start_success(self):
        '''启动'''
        try:
            #self.assertEqual(self.start_success(),'同意')
            #self.log.info('启动成功')
            #time.sleep(2)
            A=self.click_start()
            print(A)
            self.log.info('进入首页')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)

