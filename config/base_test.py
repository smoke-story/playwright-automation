from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.account_info_page import AccountInfoPage
from pages.register_page import RegisterPage
from .data import Data
import pytest


class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    account_info_page: AccountInfoPage
    register_page: RegisterPage


    @pytest.fixture(autouse=True)
    def setup(self, request, page: Page):
        request.cls.page = page
        request.cls.data = Data()
        request.cls.login_page = LoginPage(page)
        request.cls.dashboard_page = DashboardPage(page)
        request.cls.account_info_page = AccountInfoPage(page)
        request.cls.register_page = RegisterPage(page)


class LoginUser:

    @pytest.fixture(autouse=True)
    def login_user(self, page: Page):
        page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        expect(page, "Title is not equal").to_have_title("Account Login")
        page.locator("form input#input-email").fill(Data.LOGIN)
        page.locator("form input#input-password").fill(Data.PASSWORD)
        page.locator("form input[value='Login']").click()
