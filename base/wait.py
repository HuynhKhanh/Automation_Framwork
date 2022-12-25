from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class WaitForElement:
    @staticmethod
    def wait(driver, locator, time_out=10):
        try:
            WebDriverWait(driver, time_out).until(
                lambda driver: driver.find_element(*locator))
        except TimeoutException:
            print('Not able to find ID:' + locator)

    def wait_for_presence_of_all_element(self, locator_type, locator):
        list_of_elements = self.until(EC.presence_of_all_elements_located(locator_type, locator))
        print(len(list_of_elements))
        return list_of_elements
