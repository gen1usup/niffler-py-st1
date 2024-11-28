from playwright.sync_api import Page
from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
from python_e2e_tests.pages.header import Header
from python_e2e_tests.pages.login_page import LoginPage



class MainPage(BaseLogic):
    locators = {
        'history_of_spendings_text': '//h2[text()="History of spendings"]'
    }

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths['MainPage'])
        self.header = Header(page, self.app.base_url,
                             self.app.paths['MainPage'], self.app)