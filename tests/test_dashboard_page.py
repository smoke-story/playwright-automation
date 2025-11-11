from config.base_test import BaseTest, LoginUser
import allure


@allure.feature("User can see the presence of elements for interaction")
class TestDashboardPage(BaseTest, LoginUser):

    @allure.title("user can see my account block")
    def test_user_can_see_my_account_block(self) -> None:
        self.dashboard_page.should_be_dashboard_title()
        self.dashboard_page.should_be_my_account_block()

    @allure.title("user can see my orders block")
    def test_user_can_see_my_orders_block(self) -> None:
        self.dashboard_page.should_be_dashboard_title()
        self.dashboard_page.should_be_my_orders_block()

    @allure.title("user can see my affiliate account block")
    def test_user_can_see_my_affiliate_account_block(self) -> None:
        self.dashboard_page.should_be_dashboard_title()
        self.dashboard_page.should_be_my_affiliate_account_block()
    
    @allure.title("user can see success message after change account info")
    def test_user_can_see_success_message_after_change_account_info(self) -> None:
        self.dashboard_page.should_be_dashboard_title()
        self.dashboard_page.click_to_edit_account_icon()
        self.account_info_page.change_account_info()
        self.dashboard_page.should_be_success_message()
