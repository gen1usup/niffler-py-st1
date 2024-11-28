import os
from typing import Optional, Union

from playwright.sync_api import Page

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
# from python_e2e_tests.pages.main_page import MainPage
# Удалите глобальный импорт RegisterPage
# from python_e2e_tests.pages.register_page import RegisterPage


class LoginPage(BaseLogic):
    locators = {
        "username_input": "//input[@name='username']",
        "password_input": "//input[@name='password']",
        "signup_button": "//a[@href='/register']",
        "signin_button": "//button[@type='submit']",
        "signin_text": "//p[@class='form__paragraph' and text()='Please sign in']",
        "error_message": "//div[@class='error-message']"  # Локатор для сообщения об ошибке
    }

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.auth_url, self.app.paths["LoginPage"])

    def open_login_page(self) -> 'LoginPage':
        """Открыть страницу входа."""
        self.goto_url(self.full_url)
        return self

    def click_signup_button(self) -> Union['RegisterPage', 'LoginPage']:
        """Нажать на кнопку регистрации."""

        from python_e2e_tests.pages.register_page import RegisterPage
        self.click(self.locators["signup_button"])
        result = self.verify_navigation_by_url(self.app.paths["RegisterPage"], self.app.auth_url, RegisterPage)
        return result
        # if isinstance(result, RegisterPage):
        #     return result
        # else:
        #     # Проверка на наличие сообщения об ошибке
        #     error = self.get_error_message()
        #     if error:
        #         return self  # Возвращаем текущую страницу LoginPage для дальнейшей проверки
        #
        #     # Дополнительная проверка может быть добавлена здесь
        #     return self  # По умолчанию возвращаем LoginPage

    def enter_username(self, username: str) -> 'LoginPage':
        """Ввести имя пользователя."""
        self.fill(self.locators["username_input"], username)
        return self

    def enter_password(self, password: str) -> 'LoginPage':
        """Ввести пароль."""
        self.fill(self.locators["password_input"], password)
        return self

    def click_signin_button(self) -> 'LoginPage':
        """Нажать на кнопку входа."""
        self.click(self.locators["signin_button"])
        return self

    def verify_signin_text(self) -> bool:
        """Проверить наличие текста 'Please sign in'."""
        self.wait_for_visible(self.locators["signin_text"])
        text = self.get_text(self.locators["signin_text"])
        return "Please sign in" in text

    def get_error_message(self) -> Optional[str]:
        """Получить текст сообщения об ошибке, если оно отображается."""
        if self.page.locator(self.locators["error_message"]).is_visible():
            return self.get_text(self.locators["error_message"])
        return None

    def login(self, username: str, password: str) -> Union['MainPage', 'LoginPage']:
        """
        Выполнить процесс входа в систему.

        :param username: Имя пользователя
        :param password: Пароль
        :return: Экземпляр MainPage при успешном входе, иначе экземпляр LoginPage
        """

        from python_e2e_tests.pages.main_page import MainPage
        self.open_login_page()
        self.enter_username(username).enter_password(password).click_signin_button()

        result = self.verify_navigation_by_url(self.app.paths['MainPage'], self.app.base_url, MainPage, waittime = 1)
        return result
        # if isinstance(result, MainPage):
        #     return result
        # else:
        #     error = self.get_error_message()
        #     if error:
        #         return self
        #     return self  # По умолчанию возвращаем LoginPage

