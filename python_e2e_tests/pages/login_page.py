import os

from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.main_page import MainPage


class LoginPage(BaseLogic):

    path = '/login'
    login_page_url = os.getenv("AUTH_URL") + path
    username_input = "//input[@name='username']"
    password_input = "//input[@name='password']"
    signup_button = "//a[@href='/register']"
    signin_button = "//button[@type='submit']"
    signin_text = "//p[@class='form__paragraph'and text()='Please sign in']"

    def open_login_page(self):
        self.goto_url(f'{self.login_page_url}')
        return self

    def click_signup_button(self):
        self.click(self.signup_button)
        return self

    def enter_username(self, username):
        self.fill(self.username_input, username)
        return self

    def enter_password(self, password):
        self.fill(self.password_input, password)
        return self

    def click_signin_button(self):
        self.click(self.signin_button)
        return self

    def click_signup_button(self):
        self.click(self.signup_button)
        return self

    def login(self, username, password):
        self.enter_username(username).enter_password(password).click_signin_button()
        return MainPage(self.page)


