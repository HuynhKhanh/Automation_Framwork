from time import sleep
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from configfiles.data_config import *


class SearchMember(BaseDriver):
    # Locator
    search_member_tab = (By.LINK_TEXT, 'Search Member')
    search_tbx = (By.ID, 'default-search')
    search_btn = (By.XPATH, "//button[@type='submit']")

    before_XPath = "//*[@class = 'w-full text-sm text-left text-gray-500 dark:text-gray-400']/tbody/tr["
    after_td_XPath_1 = "]/td[1]"
    after_td_XPath_2 = "]/td[2]"
    after_td_XPath_3 = "]/td[3]"
    after_td_XPath_4 = "]/td[4]"
    after_td_XPath_5 = "]/td[5]"

    before_XPath_1 = "//*[@class = 'w-full text-sm text-left text-gray-500 dark:text-gray-400']/tbody/tr[1]/th["
    after_XPath = "]"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_search_member_tab(self):
        # Click on add search tab
        self.click(self.search_member_tab)
        sleep(TIME_SLEEP)

    def search_with_condition(self, value):
        # Clear the existed value
        self.clear_element_content(self.search_tbx)

        # Input the value
        self.set_value(self.search_tbx, value)

        # Click the button Search
        self.click(self.search_btn)
        sleep(TIME_SLEEP)

    def get_row_column_info(self):
        print("Test data")
        row = len(self.driver.find_elements(By.XPATH, "//*[@class = 'w-full text-sm text-left text-gray-500 "
                                                      "dark:text-gray-400']/tbody/tr"))
        column = len(self.driver.find_elements(By.XPATH, "//*[@class = 'w-full text-sm text-left text-gray-500 "
                                                         "dark:text-gray-400']/tbody/tr[1]/td"))
        for t_row in range(1, (row + 1)):
            final_xpath = self.before_XPath + str(t_row) + self.after_td_XPath_1
            cell_text = self.driver.find_element(By.XPATH, final_xpath).text
            return cell_text

    def get_column_header_info(self):
        num_row = len(self.driver.find_elements(By.XPATH, "//*[@class = 'w-full text-sm text-left text-gray-500 "
                                                          "dark:text-gray-400']/tbody/tr"))
        print("row is", num_row)
        num_columns = len(self.driver.find_elements(By.XPATH, "//*[@class = 'w-full text-sm text-left text-gray-500 "
                                                              "dark:text-gray-400']/tbody/tr[1]/td"))
        print("number_of_column_is", num_columns)

        print("Data present in Col - 1 i.e. ID")
        for t_col in range(1, (num_columns + 1)):
            final_xpath_1 = self.before_XPath_1 + str(t_col) + self.after_XPath
            print(final_xpath_1)
            cell_text = self.driver.find_elements(By.XPATH, final_xpath_1)
            print(cell_text)
