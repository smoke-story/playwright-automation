from playwright.sync_api import  Page, expect
from config.data import Data

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_page_link = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
        self.title_text = "Account Login"
        self.register_block = page.locator("//div//h2[text()='New Customer']")
        self.login_form = page.locator("//div//h2[text()='Returning Customer']")
        self.side_bar = page.locator("aside#column-right")
        self.email_field = page.locator("form input#input-email")
        self.password_field = page.locator("form input#input-password")
        self.login_button = page.locator("form input[value='Login']")
        self.my_account_link = page.locator(
            "//aside[@id='column-right']//a[contains(text(), 'My Account')]"
        )

    def open(self) -> None:
        self.page.goto(self.login_page_link)

    def log_in_user(self) -> None:
        self.email_field.fill(Data.LOGIN)
        self.password_field.fill(Data.PASSWORD)
        self.login_button.click()

    def should_be_my_account_link(self) -> None:
        expect(self.my_account_link).to_be_visible()

    def should_be_register_block(self) -> None:
        expect(self.register_block).to_be_visible()

    def should_be_login_form(self) -> None:
        expect(self.login_form).to_be_visible()

    def should_be_right_sidebar(self) -> None:
        expect(self.side_bar).to_be_visible()




