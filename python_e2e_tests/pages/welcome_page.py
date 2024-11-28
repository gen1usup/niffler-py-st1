
from playwright.sync_api import Page
from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.login_page import LoginPage
from python_e2e_tests.pages.register_page import RegisterPage


class WelcomePage(BaseLogic):
    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths['WelcomePage'])

    locators = {
        'welcome_text': "//h1[@class='main__header']",
        'login_button': "//a[@href='/redirect']",
        'register_button': "//a[text()='Register']"
    }


    def open_welcome_page(self):
        self.goto_url(f'{self.full_url}')
        return self

    def click_login(self):
        self.click(self.locators['login_button'])
        return LoginPage(self.app, self.page)

    def click_register(self):
        self.click(self.locators['register_button'])
        return RegisterPage(self.app, self.page)

    def get_welcome_text(self):
        return self.get_text(self.locators['welcome_text'])



