import os

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
# from python_e2e_tests.pages.header import Header
from playwright.sync_api import Page

from python_e2e_tests.pages.header import Header


class ProfilePage(BaseLogic):

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths['ProfilePage'])
        self.header = Header(page, self.app.base_url,
                             self.app.paths['ProfilePage'], self.app)

    locators = {
        "category_input": "//input[@name='category']",
        "create_category_button": "//button[text()='Create']",
        "not_empty_category_list": "//ul[@class='categories__list']/li",
        "cant_add_new_category_alert": "//div[@class='Toastify']/div/div/div[@role='alert']"
    }

    def create_category(self, category_name: str):
        """Создать новую категорию."""
        self.fill(self.locators["category_input"], category_name)
        self.click(self.locators["create_category_button"])
        return self

    def is_category_in_category_list(self, category_name: str) -> bool:
        """Проверить, есть ли категория в списке."""
        self.wait_for_visible(self.locators["not_empty_category_list"])
        categories = self.page.locator(self.locators["not_empty_category_list"]).all_text_contents()
        return category_name in categories

