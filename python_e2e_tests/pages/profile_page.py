import os

from python_e2e_tests.pages.header import Header


class ProfilePage(Header):
    path  = '/profile'
    profile_page_url = os.getenv("BASE_URL") + path
    category_input = "//input[@name='category']"
    create_category_button = "//button[text()='Create']"
    not_empty_category_list = "//ul[@class='categories__list']/li"
    cant_add_new_category_alert = "//div[@class='Toastify']/div/div/div[@role='alert']"
    # TO DO
    # описать остальной профиль

    def open_welcome_page(self):
        self.goto_url(f'{self.profile_page_url}')
        return self

    def create_category(self, category_name: str):
        self.fill(self.category_input, category_name)
        self.click(self.create_category_button)
        return self

    def is_category_in_category_list(self, category_name: str):
        self.page.wait_for_selector(self.not_empty_category_list)
        categories = self.page.locator(self.not_empty_category_list).all_text_contents()
        return category_name in categories

