import os
import time
from typing import Optional, Type, TypeVar, Union
from urllib.parse import urljoin

from asgiref.timeout import timeout
from playwright.sync_api import Page

from python_e2e_tests.helper.application import App

T = TypeVar('T')

class BaseLogic:
    def __init__(self, page: Page, url: str, path: str):
        self.page = page
        self.full_url = self.build_full_url(url, path)

    @staticmethod
    def build_full_url(url: Optional[str], path: str) -> str:
        return urljoin(url, path)

    def click(self, locator: str) -> None:
        """Нажать на элемент страницы."""
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str) -> None:
        """Ввести данные в Input на странице."""
        self.page.locator(locator).fill(value)

    def goto_url(self, path: Optional[str] = None) -> None:
        """Перейти на указанный URL."""
        self.page.goto(path)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).evaluate("element => element.textContent")

    def wait_for_visible(self, locator: str, timeout: int = 5000) -> None:
        """Ожидать видимости элемента."""
        self.page.wait_for_selector(locator, timeout=timeout)

    def is_visible(self, locator: str) -> bool:
        """Проверить видимость элемента на странице."""
        self.page.wait_for_selector(locator)
        return self.page.locator(locator).is_visible()

    def verify_navigation_by_url(self, expected_path: str, url: str, page_class: Type[T], waittime = 0) -> Union[T, 'BaseLogic']:
        """
        Проверяет, что текущий URL соответствует ожидаемому, и возвращает экземпляр соответствующей страницы.

        :param waittime:
        :param url:
        :param expected_path: Ожидаемый путь после перехода.
        :param page_class: Класс страницы, которую следует вернуть при успешной проверке.
        :return: Экземпляр page_class при успешной проверке, иначе экземпляр текущей страницы.
        """
        expected_url = self.build_full_url(url, expected_path)
        time.sleep(waittime)
        self.page.reload()
        current_url = self.page.url

        if current_url == expected_url:
            return page_class(self.app, self.page)
        else:
            # Можно добавить дополнительную логику, например, логирование или повторную попытку
            return self