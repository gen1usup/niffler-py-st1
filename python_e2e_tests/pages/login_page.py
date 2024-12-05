import os
from typing import Optional, Union

from playwright.sync_api import Page

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic


class LoginPage(BaseLogic):
    # Вынесение локаторов в отдельные переменные класса
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    SIGNUP_BUTTON = "//a[@href='/register']"
    SIGNIN_BUTTON = "//button[@type='submit']"
    SIGNIN_TEXT = "//p[@class='form__paragraph' and text()='Please sign in']"
    ERROR_MESSAGE = "//div[@class='error-message']"  # Локатор для сообщения об ошибке


    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.auth_url, self.app.paths.login_page)

    def open_login_page(self) -> 'LoginPage':
        """Открыть страницу входа."""
        self.goto_url(self.full_url)
        return self

    def click_signup_button(self) -> Union['RegisterPage', 'LoginPage']:
        """Нажать на кнопку регистрации."""
        from python_e2e_tests.pages.register_page import RegisterPage
        self.click(self.SIGNUP_BUTTON)
        result = self.verify_navigation_by_url(
            self.app.paths.register_page,
            self.app.auth_url,
            RegisterPage
        )
        return result
        # Если требуется обработка ошибок, можно раскомментировать и использовать следующий код:
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
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> 'LoginPage':
        """Ввести пароль."""
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_signin_button(self) -> 'LoginPage':
        """Нажать на кнопку входа."""
        self.click(self.SIGNIN_BUTTON)
        return self

    def verify_signin_text(self) -> bool:
        """Проверить наличие текста 'Please sign in'."""
        self.wait_for_visible(self.SIGNIN_TEXT)
        text = self.get_text(self.SIGNIN_TEXT)
        return "Please sign in" in text

    def get_error_message(self) -> Optional[str]:
        """Получить текст сообщения об ошибке, если оно отображается."""
        if self.page.locator(self.ERROR_MESSAGE).is_visible():
            return self.get_text(self.ERROR_MESSAGE)
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

        result = self.verify_navigation_by_url(
            self.app.paths.main_page,
            self.app.base_url,
            MainPage,
            waittime=1
        )
        return result
        # Если требуется обработка ошибок, можно раскомментировать и использовать следующий код:
        # if isinstance(result, MainPage):
        #     return result
        # else:
        #     error = self.get_error_message()
        #     if error:
        #         return self
        #     return self  # По умолчанию возвращаем LoginPage
