from playwright.sync_api import Page, expect
from config.data import Data
import allure


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_page_link = "https://ecommerce-playground.lambdatest.io" \
            "/index.php?route=account/login"
        self.register_block = page.locator("//div//h2[text()='New Customer']")
        self.login_form = page.locator("//div//h2[text()='Returning Customer']")
        self.side_bar = page.locator("aside#column-right")
        self.email_field = page.locator("form input#input-email")
        self.password_field = page.locator("form input#input-password")
        self.login_button = page.locator("form input[value='Login']")
        self.my_account_link = page.locator(
            "//aside[@id='column-right']//a[contains(text(), 'My Account')]")
        
    
    @allure.step("open login page")
    def open(self) -> None:
        self.page.goto(self.login_page_link)
    
    @allure.step("log in user")
    def log_in_user(self) -> None:
        self.email_field.fill(Data.LOGIN)
        self.password_field.fill(Data.PASSWORD)
        self.login_button.click()
    
    @allure.step("should be login page title")
    def should_be_login_page_title(self)  -> None:
        expect(self.page, f"Title is not correct: \
            {self.page.title()}").to_have_title("Account Login")
    
    @allure.step("should be my account link")
    def should_be_my_account_link(self) -> None:
        expect(self.my_account_link,
            "'My account link' is not present").to_be_visible()
    
    @allure.step("should be register block")
    def should_be_register_block(self) -> None:
        expect(self.register_block,
            "'Register block' is not present").to_be_visible()
    
    @allure.step("should be login form")
    def should_be_login_form(self) -> None:
        expect(self.login_form,
            "'Login form' is not present").to_be_visible()
    
    @allure.step("should be right sidebar")
    def should_be_right_sidebar(self) -> None:
        expect(self.side_bar,
            "'Right sidebar' is not present").to_be_visible()
