
from Page.BasePage import Action


class Start(Action):

        self.start_loc = ('id', 'com.xueqiu.android:id/tv_agree')

    def start_success(self):
        '''判断启动成功'''
        #start_success = self.driver.find_elements_by_id('com.xueqiu.android:id/tab_icon')
        start_success = self.find_element(self.start_loc).text
        print(start_success)
        return start_success

    def click_start(self):
        '''点击同意按钮'''
        self.click_button(self.start_loc)




