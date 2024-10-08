import os

from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.login_page import LoginPage


class RegisterPage(BaseLogic):
    path = '/register'
    main_page_url = os.getenv("AUTH_URL") + path
    username_input = "//input[@id='username']"
    password_input = "//input[@id='password']"
    password_confirmation_input = "//input[@id='passwordSubmit']"
    signup_button = "//button[@type='submit']"
    signin_button = "//a[text()='Sign in!']"
    signup_text = "//p[@class='form__paragraph' and text()='Registration form']"
    success_registration_text = "//p[@class='form__paragraph' and contains(text(),'Congratulations')]"
    success_registration_button = "//p[@class='form__paragraph'][2]"

    def open_register_page(self):
        self.goto_url(self.main_page_url)
        return self

    def click_signin_button(self):
        self.click(self.signin_button)
        return LoginPage(self.page)

    def register(self, username, password, password_confirmation):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.fill(self.password_confirmation_input, password_confirmation)
        self.click(self.signup_button)
