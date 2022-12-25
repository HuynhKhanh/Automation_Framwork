import time

from selenium.common import NoSuchElementException

from base.wait import *


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def set_value(self, locator, value):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.click()

    def tick_on_checkbox(self, locator):
        for i in range(10):
            try:
                WaitForElement.wait(self.driver, locator)
                element = self.driver.find_element(*locator)
                element.click()
                break
            except NoSuchElementException as e:
                print('Retry in 1 second')
                time.sleep(1)
        else:
            raise e

    def get_value(self, locator):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        return element.get_attribute()

    def clear_element_content(self, locator):
        el = self.driver.find_element(*locator)
        el.clear()

    def find_element(self, locator):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        return element
