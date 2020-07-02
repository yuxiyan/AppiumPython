

from Page.BasePage import Action
import yaml,os
from common.read_caps import get_yml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)


class CreateGroup(Action):


    loc=get_yml(PATH("locate/CreatGroup.yml"))
    """
    click_hangqing_loc=("xpath","//android.widget.TextView[@text='行情']")
    click_editgroup_loc=("id","com.xueqiu.android:id/edit_group")
    click_managegroup_loc=("id","com.xueqiu.android:id/title2")
    click_creatgroup_loc=("id","com.xueqiu.android:id/add_item")
    click_input_loc = ("id", "com.xueqiu.android:id/dialog_input_text")
    click_confirm_loc = ("id", "com.xueqiu.android:id/bt_right")
    #creatgroup_success_loc = ("xpath", "//android.widget.EditText[@text='900']")
    click_finish_loc=("id","com.xueqiu.android:id/action_close")
    creatgroup_success_loc=("xpath", "//android.widget.TextView[@text='900']")
    """

    def exc_button(self):
        '''执行点击动作'''
        self.click_button(self.loc['click_hangqing_loc'])
        self.click_button(self.loc['click_editgroup_loc'])
        self.click_button(self.loc['click_managegroup_loc'])
        self.click_button(self.loc['click_creatgroup_loc'])
        self.send_keys(self.loc['click_input_loc'],self.loc['click_input_loc'][2])
        self.click_button(self.loc['click_confirm_loc'])
        self.click_button(self.loc['click_finish_loc'])

    def creategroup_success(self):
        '''判断是否创建成功'''
        exc_success = self.find_element(self.loc['creategroup_success_loc']).text
        print(exc_success)
        return exc_success












