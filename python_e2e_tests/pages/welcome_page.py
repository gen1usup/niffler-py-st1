from playwright.sync_api import Page, Locator
from typing import Optional

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.login_page import LoginPage
from python_e2e_tests.pages.register_page import RegisterPage


class WelcomePage(BaseLogic):
    # Вынесение локаторов в отдельные переменные класса
    WELCOME_TEXT = "//h1[@class='main__header']"
    LOGIN_BUTTON = "//a[@href='/redirect']"
    REGISTER_BUTTON = "//a[text()='Register']"

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths.welcome_page)

    def open_welcome_page(self) -> 'WelcomePage':
        """Открыть страницу приветствия."""
        self.goto_url(self.full_url)
        return self

    def click_login(self) -> LoginPage:
        """Нажать на кнопку входа и перейти на страницу входа."""
        self.click(self.LOGIN_BUTTON)
        return LoginPage(self.app, self.page)

    def click_register(self) -> RegisterPage:
        """Нажать на кнопку регистрации и перейти на страницу регистрации."""
        self.click(self.REGISTER_BUTTON)
        return RegisterPage(self.app, self.page)

    def get_welcome_text(self) -> str:
        """Получить текст приветствия."""
        return self.get_text(self.WELCOME_TEXT)
