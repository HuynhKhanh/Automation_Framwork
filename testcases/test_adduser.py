import allure
import pytest
from pages.add_memmber_page import AddMember


@pytest.mark.usefixtures("setup")
class TestAddUser:
    def test_add_valid_user(self):
        add_member = AddMember(self.driver)
        with allure.step("Input information of user "):
            add_member.input_member('Khanh', 'Huynh 1', 'Dev', 'Contour', '0974536267', 'http://abc.com',
                                    'khanhh.941@gmail.com')
        with allure.step("Check on the box to confirm"):
            add_member.accept_term()
        with allure.step("Click on button Submit"):
            add_member.submit_member()
        with allure.step("Display message success"):
            add_member.verify_message_after_add_member()
