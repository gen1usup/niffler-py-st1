from playwright.sync_api import Page
from typing import Optional

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic


class RegisterPage(BaseLogic):
    # Вынесение локаторов в отдельные переменные класса
    USERNAME_INPUT = "//input[@id='username']"
    PASSWORD_INPUT = "//input[@id='password']"
    PASSWORD_CONFIRMATION_INPUT = "//input[@id='passwordSubmit']"
    SIGNUP_BUTTON = "//button[@type='submit']"
    SIGNIN_BUTTON = "//a[text()='Sign in!']"
    SIGNUP_TEXT = "//p[@class='form__paragraph' and text()='Registration form']"
    SUCCESS_REGISTRATION_TEXT = "//p[@class='form__paragraph' and contains(text(),'Congratulations')]"
    SUCCESS_REGISTRATION_BUTTON = "//p[@class='form__paragraph'][2]"

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.auth_url, self.app.paths.register_page)

    def open_register_page(self) -> 'RegisterPage':
        """Открыть страницу регистрации."""
        self.goto_url(self.full_url)
        return self

    def click_signin_button(self) -> 'LoginPage':
        """Нажать на кнопку 'Sign in!' и перейти на страницу входа."""
        from python_e2e_tests.pages.login_page import LoginPage
        self.click(self.SIGNIN_BUTTON)
        return LoginPage(self.app, self.page)

    def register(self, username: str, password: str, password_confirmation: str) -> 'RegisterPage':
        """
        Зарегистрировать нового пользователя.

        :param username: Имя пользователя
        :param password: Пароль
        :param password_confirmation: Подтверждение пароля
        :return: Экземпляр RegisterPage для дальнейших действий или проверок
        """
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.fill(self.PASSWORD_CONFIRMATION_INPUT, password_confirmation)
        self.click(self.SIGNUP_BUTTON)
        return self

    def verify_signup_text(self) -> bool:
        """
        Проверить наличие текста 'Registration form' на странице.

        :return: True, если текст присутствует, иначе False
        """
        self.wait_for_visible(self.SIGNUP_TEXT)
        text = self.get_text(self.SIGNUP_TEXT)
        return "Registration form" in text

    def is_successfully_registered(self) -> bool:
        """
        Проверить, успешно ли прошла регистрация.

        :return: True, если регистрация успешна, иначе False
        """
        self.wait_for_visible(self.SUCCESS_REGISTRATION_TEXT)
        text = self.get_text(self.SUCCESS_REGISTRATION_TEXT)
        return "Congratulations" in text

    def click_success_registration_button(self) -> 'MainPage':
        """
        Нажать на кнопку после успешной регистрации, чтобы перейти на главную страницу.

        :return: Экземпляр MainPage
        """
        from python_e2e_tests.pages.main_page import MainPage
        self.click(self.SUCCESS_REGISTRATION_BUTTON)
        return MainPage(self.app, self.page)

    def get_success_registration_text(self) -> Optional[str]:
        """
        Получить текст сообщения об успешной регистрации, если оно отображается.

        :return: Текст сообщения или None
        """
        if self.page.locator(self.SUCCESS_REGISTRATION_TEXT).is_visible():
            return self.get_text(self.SUCCESS_REGISTRATION_TEXT)
        return None
