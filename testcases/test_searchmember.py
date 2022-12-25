import allure
import pytest
from pages.search_member_page import SearchMember
import unittest


@pytest.mark.usefixtures("setup")
class TestSearchMember(unittest.TestCase):
    def test_search_member_with_valid_id(self):
        expected_id = 13
        search_member = SearchMember(self.driver)
        with allure.step("Navigate to search member tab "):
            search_member.navigate_to_search_member_tab()
        with allure.step("Search the member with ID "):
            search_member.search_with_condition(expected_id)
        with allure.step("Verify the value id after search member with id "):
            actual_id = search_member.get_row_column_info()
            message = "The ID is correct"
            self.assertEqual(expected_id, int(actual_id), message)




