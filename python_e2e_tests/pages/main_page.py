import os

from python_e2e_tests.pages.header import Header


class MainPage(Header):
    path = '/main'
    main_page_url = os.getenv("BASE_URL") + path
    history_of_spendings_text = "//h2[text()='History of spendings']"

    def open_main_page(self):
        self.goto_url(f'{self.main_page_url}')


