
import unittest
from Page.ClickStockPage import ClickStock
import time
from common.logger import Log

class CaseClickStock(ClickStock,unittest.TestCase):

    log = Log()

    def test_clickstock_success(self):
        '''个股页点击'''
        try:
            for i in range(10):
                print("第%d次" % i)
                self.exc_button()
                time.sleep(5)
                self.log.info('运行成功')
        except Exception as e:
            self.getScreenShot()
            #self.log.error(e)
            self.log.critical(e)#判断如果返回的是找不到元素不send信息





if __name__ == '__main__':
    unittest.main()