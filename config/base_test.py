import pytest
from config.data import Data
from playwright.sync_api import Page
from pages.login_page import LoginPage

class BaseTest:

    page: Page
    data: Data
    login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, page):

        request.cls.page = page
        request.cls.data = Data()
        request.cls.login_page = LoginPage(page)