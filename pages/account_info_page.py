from playwright.sync_api import Page, expect
from faker import Faker
import allure


class AccountInfoPage:

    def __init__(self, page: Page)  -> None:
        self.page = page
        self.fake = Faker()
        self.form_account_info = self.page.locator("div#content")
        self.first_name_field = self.page.locator("#input-firstname")
        self.last_name_field = self.page.locator("#input-lastname")
        self.email_field = self.page.locator("#input-email")
        self.phone_number_field = self.page.locator("#input-telephone")
        self.button_submit = self.page.locator("input[type = 'submit']")
        self.old_first_name = None
        self.current_first_name = None


    @allure.step("open account info page")
    def open(self)  -> None:
        self.page.goto(
            "https://ecommerce-playground.lambdatest.io/index.php?route=account/edit")

    @allure.step("should be account info page title")
    def should_be_account_info_title(self) -> None:
        expect(self.page, f"Title is not correct: \
            {self.page.title()}").to_have_title("My Account Information")

    @allure.step("should be form account info")
    def should_be_form_account_info(self) -> None:
        expect(self.form_account_info,
            "Something wrong with 'Account information form'").to_be_visible()

    @allure.step("change account info")
    def change_account_info(self) -> None:
        self.old_first_name = self.page.get_attribute("#input-firstname", "value")
        self.first_name_field.fill(self.fake.first_name())
        self.last_name_field.fill(self.fake.last_name())
        self.phone_number_field.fill(self.fake.phone_number())
        self.button_submit.click()

    @allure.step("should be correct info after change")
    def should_be_correct_info_after_change(self) -> None:
        self.current_first_name = self.page.get_attribute("#input-firstname", "value")
        print("\nold: ", self.old_first_name, "\ncurrent: ", self.current_first_name)
        assert self.old_first_name != self.current_first_name, \
            f"'Current first name':{self.current_first_name} is not correct"
