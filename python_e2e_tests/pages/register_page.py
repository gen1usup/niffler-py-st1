from playwright.sync_api import Page

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic


class RegisterPage(BaseLogic):
    locators = {
        'username_input': "//input[@id='username']",
        'password_input':"//input[@id='password']",
        "password_confirmation_input": "//input[@id='passwordSubmit']",
        "signup_button": "//button[@type='submit']",
        "signin_button": "//a[text()='Sign in!']",
        "signup_text": "//p[@class='form__paragraph' and text()='Registration form']",
        "success_registration_text": "//p[@class='form__paragraph' and contains(text(),'Congratulations')]",
        "success_registration_button": "//p[@class='form__paragraph'][2]"
    }


    def __init__(self, app: 'App', page: Page):
        self.app = app
        super().__init__(page, self.app.auth_url, self.app.paths['RegisterPage'])


    def open_register_page(self):
        self.page.goto(self.full_url)


    def click_signin_button(self) -> 'LoginPage':
        from python_e2e_tests.pages.login_page import LoginPage
        self.click(self.locators['signin_button'])
        return LoginPage(self.app, self.page)

    def register(self, username, password, password_confirmation):
        self.fill(self.locators['username_input'], username)
        self.fill(self.locators['password_input'], password)
        self.fill(self.locators['password_confirmation_input'], password_confirmation)
        self.click(self.locators['signup_button'])
