from time import sleep
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from configfiles.data_config import *


class AddMember(BaseDriver):
    # Locator
    add_member_tab = (By.LINK_TEXT, 'Add Member')
    first_name = (By.ID, 'first_name')
    last_name = (By.ID, 'last_name')
    position = (By.ID, 'title')
    company = (By.ID, 'company')
    phone = (By.ID, 'phone')
    website = (By.ID, 'website')
    email = (By.ID, 'email')
    checkbox = (By.ID, 'remember')
    btn_Submit = (By.XPATH, "//button[@type='submit']")
    toast_message_success = (By.ID, "toast-success")

    def __init__(self, driver):
        self.driver = driver

    def input_member(self, first_name, last_name, position, company, phone_number, website,  email):
        # Click on add member tab
        self.click(self.add_member_tab)

        # Input the first_name
        self.set_value(self.first_name, first_name)

        # Input the last_name
        self.set_value(self.last_name, last_name)

        # Input the title
        self.set_value(self.position, position)

        # Input the company
        self.set_value(self.company, company)

        # Input the phone number
        self.set_value(self.phone, phone_number)

        # Input the phone website
        self.set_value(self.website, website)

        # Input the email
        self.set_value(self.email, email)

    def accept_term(self):
        self.tick_on_checkbox(self.checkbox)

    def submit_member(self):
        self.click(self.btn_Submit)
        sleep(TIME_SLEEP)

    def verify_message_after_add_member(self):
        toast = self.driver.find_element(By.ID, "toast-success")
        actual_message = toast.text
        expected_message_submit_success = "Member has been added"
        print("Title of the toast message is", toast.text)
        if expected_message_submit_success.find(actual_message) != -1:
            print("Add member successfully")
        else:
            print("Fail to add member")


