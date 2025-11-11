from config.base_test import BaseTest
import allure


@allure.feature("Login page functionality")
class TestLoginPage(BaseTest):

    @allure.title("guest should see register block")
    def test_guest_should_see_register_block(self) -> None:
        self.login_page.open()
        self.login_page.should_be_register_block()

    @allure.title("guest should see login form")
    def test_guest_should_see_login_form(self) -> None:
        self.login_page.open()
        self.login_page.should_be_login_form()

    @allure.title("guest should see right sidebar")
    def test_guest_should_see_right_sidebar(self) -> None:
        self.login_page.open()
        self.login_page.should_be_right_sidebar()

    @allure.title("guest can sign in account")
    def test_guest_can_sign_in_account(self) -> None:
        self.login_page.open()
        self.login_page.log_in_user()
        self.login_page.should_be_my_account_link()

