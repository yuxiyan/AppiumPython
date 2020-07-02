from Page.BasePage import Action
import yaml,os
from common.read_caps import get_yml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)


class DeleteGroup(Action):


    loc=get_yml(PATH("locate/DeleteGroup.yml"))


    def exc_button(self):
        '''执行点击动作'''
        self.click_button(self.loc['click_hangqing_loc'])
        self.click_button(self.loc['click_editgroup_loc'])
        self.click_button(self.loc['click_managegroup_loc'])
        self.click_button(self.loc['click_group_loc'])
        self.click_button(self.loc['click_confirm_loc'])
        self.click_button(self.loc['click_finish_loc'])

    def deletegroup_success(self):
        '''判断是否删除成功'''
        exc_success = self.find_element(self.loc['deletegroup_success_loc'])
        print(exc_success)

        return exc_success

