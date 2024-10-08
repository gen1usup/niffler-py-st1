import dotenv

from python_e2e_tests.pages.main_page import MainPage
from python_e2e_tests.pages.login_page import LoginPage
from python_e2e_tests.pages.profile_page import ProfilePage
from python_e2e_tests.pages.register_page import RegisterPage
from python_e2e_tests.pages.welcome_page import WelcomePage

dotenv.load_dotenv()

class App:
    def __init__(self, page):
        self.login_page = LoginPage(page)
        self.register_page = RegisterPage(page)
        self.profile_page = ProfilePage(page)
        self.welcome_page = WelcomePage(page)
        self.home_page = MainPage(page)