from playwright.sync_api import Page
from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.header import Header
from python_e2e_tests.pages.login_page import LoginPage


class MainPage(BaseLogic):
    # Вынесение локаторов в отдельные переменные класса
    HISTORY_OF_SPENDINGS_TEXT = '//h2[text()="History of spendings"]'

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths.main_page)
        self.header = Header(page, self.app.base_url,
                             self.app.paths.main_page, self.app)