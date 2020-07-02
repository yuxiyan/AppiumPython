
import unittest
from Page.CreateGroupPage import CreateGroup
import time
from common.logger import Log

class CaseCreateGroup(CreateGroup,unittest.TestCase):

    log = Log()

    def test_creategroup_success(self):
        '''创建分组'''
        try:
            self.exc_button()
            time.sleep(5)
            self.assertEqual(self.creategroup_success(),'900')
            self.log.info('创建成功')
        except Exception as e:
            self.getScreenShot()
            #self.log.error(e)
            self.log.critical(e)


if __name__ == '__main__':
    unittest.main()