
import unittest
from Page.DeleteGroupPage import DeleteGroup
import time
from common.logger import Log

class CaseDeleteGroup(DeleteGroup,unittest.TestCase):

    log = Log()

    def test_deletegroup_success(self):
        '''删除分组'''
        try:
            self.exc_button()
            time.sleep(5)
            self.assertEqual(self.deletegroup_success(),None)
            self.log.info('删除成功')
        except Exception as e:
            self.getScreenShot()
            self.log.error(e)


if __name__ == '__main__':
    unittest.main()