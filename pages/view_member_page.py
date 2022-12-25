from time import sleep
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from configfiles.data_config import *


class ViewMember(BaseDriver):
    # Locator
    view_member_tab = (By.LINK_TEXT, 'View Member')
    email = (By.ID, 'email')

    def navigate_to_view_member(self):
        # Click on add search tab
        self.click(self.view_member_tab)
        sleep(TIME_SLEEP)

    def verify_field_after_search(self):
        # field_locator = self.driver.find_element(By.ID, 'email')
        actual_field_value = self.find_element(self.email).text
        return actual_field_value
