from typing import TYPE_CHECKING, Optional
from playwright.sync_api import Page


class BaseLogic:

    path = ''
    def __init__(self, page: 'Page'):
        self.page = page

    def click(self, locator: str) -> None:
        """Нажать на элемент страницы."""
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str) -> None:
        """Ввести данные в Input на странице."""
        self.page.locator(locator).fill(value)

    def goto_url(self, path: Optional[str] = None) -> None:
        """Ввести данные в Input на странице."""
        self.page.goto(path or self.path)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).evaluate("element => element.textContent")
