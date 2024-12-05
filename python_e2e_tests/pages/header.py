from playwright.sync_api import Page
from python_e2e_tests.pages.base_logic import BaseLogic
from typing import TypeVar

T = TypeVar('T')

class Header(BaseLogic):

    main_button = "//li[@data-tooltip-id='main']"
    friends_button = "//li[@data-tooltip-id='friends']"
    all_people_button = "//li[@data-tooltip-id='people']"
    profile_button = "//li[@data-tooltip-id='profile']"
    logout_button = "//button[@type='button' and @class='button-icon button-icon_type_logout']"

    def __init__(self, page: Page, url: str, path: str, app):
        self.app = app
        super().__init__(page, url, path)

    def click_logout(self) -> 'WelcomePage':
        """Выйти из профиля и вернуть страницу логина."""
        from python_e2e_tests.pages.welcome_page import WelcomePage
        self.click(self.logout_button)
        return WelcomePage(self.app, self.page)

    def go_main(self):
        """Перейти на главную страницу."""
        self.click(self.main_button)

    def go_friends(self):
        """Перейти на страницу друзей."""
        self.click(self.friends_button)

    def go_all_people(self):
        """Перейти на страницу всех пользователей."""
        self.click(self.all_people_button)

    def go_profile(self) -> 'ProfilePage':
        from python_e2e_tests.pages.profile_page import ProfilePage
        """Перейти на страницу профиля."""
        self.click(self.profile_button)
        return ProfilePage(self.app, self.page)
