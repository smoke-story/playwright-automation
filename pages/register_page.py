from playwright.sync_api import Page, expect
from faker import Faker
import allure


class RegisterPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.fake = Faker()
        self.link_register_account = ("https://ecommerce-playground.lambdatest.io"
            "/index.php?route=account/register")
        self.first_name_field = self.page.locator("#input-firstname")
        self.last_name_field = self.page.locator("#input-lastname")
        self.email_field = self.page.locator("#input-email")
        self.phone_number_field = self.page.locator("#input-telephone")
        self.password_1_field = self.page.locator("#input-password")
        self.password_2_field = self.page.locator("#input-confirm")
        self.radiobutton_no_subscribe = self.page.locator("#input-newsletter-no")
        self.checkbox_agreement = self.page.locator("#input-agree ~ label")
        self.button_continue_register = self.page.locator("input[value='Continue']")
        self.success_register_message = self.page.locator(
            "div#content h1")
        self.button_success_page_continue = self.page.locator(
            "//div/a[contains(text(), 'Continue')]")
        self.form_register_account = self.page.locator(
            "//h1[contains(text(), 'Register Account')]/following-sibling::form")


    @allure.step("open register page")
    def open(self) -> None:
        self.page.goto(self.link_register_account)

    @allure.step("should be register page title")
    def should_be_register_page_title(self) -> None:
        expect(self.page, f"'Register page' title is not correct: \
            {self.page.title()}").to_have_title("Register Account")

    @allure.step("should be register form")
    def should_be_register_form(self) -> None:
        expect(self.form_register_account,
            "'Register form' is not present").to_be_visible()

    @allure.step("should be success page after register")
    def should_be_success_page_after_register(self) -> None:
        expect(self.page, f"'Success register page' title is not correct: \
            {self.page.title()}").to_have_title("Your Account Has Been Created!")

    @allure.step("should be success register message")
    def should_be_success_register_message(self) -> None:
        expect(self.success_register_message,
            "'Success register message' is not correct"
                ).to_have_text("Your Account Has Been Created!")

    @allure.step("registering new user")
    def registering_new_user(self) -> None:
        random_password = self.fake.password()
        self.first_name_field.fill(self.fake.first_name_male())
        self.last_name_field.fill(self.fake.last_name_male())
        self.email_field.fill(self.fake.email())
        self.phone_number_field.fill(self.fake.phone_number())
        self.password_1_field.fill(random_password)
        self.password_2_field.fill(random_password)
        self.radiobutton_no_subscribe.check()
        self.checkbox_agreement.click()
        self.button_continue_register.click()

    @allure.step("click continue button after success register message")
    def click_continue_button_after_success_register_message(self) -> None:
        self.button_success_page_continue.click()
