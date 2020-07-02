

from Page.BasePage import Action
import yaml,os
from common.read_caps import get_yml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)


class ClickStock(Action):


    loc=get_yml(PATH("locate/ClickStockPage.yml"))
    print(loc)

    def exc_button(self):
        '''执行点击动作'''
        self.click_button(self.loc['click_hangqing_loc'])
        self.click_button(self.loc['click_stock_loc'])
        self.click_button(self.loc['click_stockminute_loc'])
        self.click_button(self.loc['click_stockfivedays_loc'])
        self.click_button(self.loc['click_stockday_loc'])
        self.click_button(self.loc['click_stockweek_loc'])
        self.click_button(self.loc['click_stockmonth_loc'])
        self.click_button(self.loc['click_stockseason_loc'])
        self.click_button(self.loc['click_stockyear_loc'])
        self.click_button(self.loc['click_discussion_loc'])
        self.click_button(self.loc['click_newpost_loc'])
        self.click_button(self.loc['click_recommand_loc'])
        self.click_button(self.loc['click_title_loc'])
        self.click_button(self.loc['click_switch_loc'])
        self.click_button(self.loc['click_back_loc'])







































