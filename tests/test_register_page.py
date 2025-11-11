from config.base_test import BaseTest
import pytest
import allure


@allure.feature("Registering new user account")
class TestRegisteringNewUserAccount(BaseTest):

    @allure.title("guest can see register form")
    def test_guest_can_see_register_form(self) -> None:
        self.register_page.open()
        self.register_page.should_be_register_page_title()
        self.register_page.should_be_register_form()

    @allure.title("guest can create new user account")
    @pytest.mark.flaky(reruns=3)
    def test_guest_can_create_new_user_account(self) -> None:
        self.register_page.open()
        self.register_page.should_be_register_page_title()
        self.register_page.registering_new_user()
        self.register_page.should_be_success_page_after_register()
        self.register_page.should_be_success_register_message()
        self.register_page.click_continue_button_after_success_register_message()
        self.dashboard_page.should_be_dashboard_title()
