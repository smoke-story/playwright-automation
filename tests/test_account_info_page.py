from config.base_test import BaseTest, LoginUser
import allure


@allure.feature("Account information page functionality")
class TestAccountInfoPage(BaseTest, LoginUser):

    @allure.title("user should see form account info")
    def test_user_should_see_form_account_info(self) -> None:
        self.account_info_page.open()
        self.account_info_page.should_be_account_info_title()
        self.account_info_page.should_be_form_account_info()

    @allure.title("user can change account info")
    def test_user_can_change_account_info(self) -> None:
        self.account_info_page.open()
        self.account_info_page.should_be_account_info_title()
        self.account_info_page.change_account_info()
        self.dashboard_page.click_to_edit_account_icon()
        self.account_info_page.should_be_correct_info_after_change()
