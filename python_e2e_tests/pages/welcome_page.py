import os

from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.login_page import LoginPage
from python_e2e_tests.pages.register_page import RegisterPage


class WelcomePage(BaseLogic):
    path = '/'
    welcome_page_url = os.getenv("BASE_URL") + path
    welcome_text = "//h1[@class='main__header']"
    login_button = "//a[@href='/redirect']"
    register_button = "//a[@href='http://auth.niffler.dc:9000/register']"

    def open_welcome_page(self):
        self.goto_url(f'{self.welcome_page_url}')
        return self

    def click_login(self):
        self.click(self.login_button)
        return LoginPage(self.page)

    def click_register(self):
        self.click(self.register_button)
        return RegisterPage(self.page)

    def get_welcome_text(self):
        return self.get_text(self.welcome_text)



