from playwright.sync_api import Page, expect
import allure


class DashboardPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = self.page.title()
        self.message_success = self.page.locator("div.alert-success")
        self.my_account_block = self.page.locator(
            "//h2[contains(text(), 'My Account')]/parent::div")
        self.my_orders_block = self.page.locator(
            "//h2[contains(text(), 'My Orders')]/parent::div")
        self.my_affiliate_account_block = self.page.locator(
            "//h2[contains(text(), 'My Affiliate Account')]/parent::div")
        self.edit_account_link = self.page.locator(
            "//h2[contains(text(), 'My Account')]/parent::div \
            //a[contains(text(), 'Edit your account')]")
    
    
    @allure.step("should be dashboard title")
    def should_be_dashboard_title(self) -> None:
        expect(self.page, f"Title is not correct: \
            {self.page.title()}").to_have_title("My Account")
    
    @allure.step("should be my account block")
    def should_be_my_account_block(self) -> None:
        expect(self.my_account_block,
            "Something wrong with 'My account' block").to_be_visible()

    @allure.step("should be my orders block")
    def should_be_my_orders_block(self) -> None:
        expect(self.my_orders_block,
            "Something wrong with 'My orders' block").to_be_visible()

    @allure.step("should be my affiliate account block")
    def should_be_my_affiliate_account_block(self) -> None:
        expect(self.my_affiliate_account_block,
            "Something wrong with 'My affiliate account' block").to_be_visible()
        
    @allure.step("click to edit account icon")
    def click_to_edit_account_icon(self) -> None:
        self.edit_account_link.click()
    
    @allure.step("should be success message")
    def should_be_success_message(self) -> None:
        expect(self.message_success, f"Sucsess message is not correct: \
            {self.message_success}").to_be_visible()
        
