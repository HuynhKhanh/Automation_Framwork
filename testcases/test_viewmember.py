import allure
import pytest
from pages.search_member_page import SearchMember
from pages.view_member_page import ViewMember
import unittest


@pytest.mark.usefixtures("setup")
class TestViewMember(unittest.TestCase):
    def test_view_detail_member_with_existed_id(self):
        search_member_id = 13
        expected_email = "khanhh.941@gmail.com"
        message = "Email of member is correctly"
        search_member = SearchMember(self.driver)
        view_member = ViewMember(self.driver)
        with allure.step("Navigate to View Member "):
            view_member.navigate_to_view_member()
        with allure.step("Search the member with ID "):
            search_member.search_with_condition(search_member_id)
        with allure.step("Verify the value id after search member with id "):
            actual_email = view_member.verify_field_after_search()
            self.assertEqual(expected_email, actual_email, message)
