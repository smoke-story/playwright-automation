from config.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_guest_should_see_register_block(self):
        self.login_page.open()
        self.login_page.should_be_register_block()

    def test_guest_should_see_login_form(self):
        self.login_page.open()
        self.login_page.should_be_login_form()

    def test_guest_should_see_right_sidebar(self):
        self.login_page.open()
        self.login_page.should_be_right_sidebar()

    def test_guest_can_sign_in_account(self):
        self.login_page.open()
        self.login_page.log_in_user()
        self.login_page.should_be_my_account_link()

