import os
from typing import Optional

from python_e2e_tests.helper.application import App
from python_e2e_tests.pages.base_logic import BaseLogic
from playwright.sync_api import Page

from python_e2e_tests.pages.header import Header


class ProfilePage(BaseLogic):
    # Вынесение локаторов в отдельные переменные класса
    CATEGORY_INPUT = "//input[@name='category']"
    CREATE_CATEGORY_BUTTON = "//button[text()='Create']"
    NOT_EMPTY_CATEGORY_LIST = "//ul[@class='categories__list']/li"
    CANT_ADD_NEW_CATEGORY_ALERT = "//div[@class='Toastify']/div/div/div[@role='alert']"

    def __init__(self, app: App, page: Page):
        self.app = app
        super().__init__(page, self.app.base_url, self.app.paths.profile_page)
        self.header = Header(page, self.app.base_url,
                             self.app.paths.profile_page, self.app)

    def create_category(self, category_name: str) -> 'ProfilePage':
        """Создать новую категорию."""
        self.fill(self.CATEGORY_INPUT, category_name)
        self.click(self.CREATE_CATEGORY_BUTTON)
        return self

    def is_category_in_category_list(self, category_name: str) -> bool:
        """Проверить, есть ли категория в списке."""
        self.wait_for_visible(self.NOT_EMPTY_CATEGORY_LIST)
        categories = self.page.locator(self.NOT_EMPTY_CATEGORY_LIST).all_text_contents()
        return category_name in categories

    def get_cant_add_new_category_alert(self) -> Optional[str]:
        """Получить текст предупреждения о невозможности добавления новой категории."""
        if self.page.locator(self.CANT_ADD_NEW_CATEGORY_ALERT).is_visible():
            return self.get_text(self.CANT_ADD_NEW_CATEGORY_ALERT)
        return None
