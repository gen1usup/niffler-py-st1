from faker import  Faker
import pytest

from python_e2e_tests.helper.http_client import HttpClient
from python_e2e_tests.pages.profile_page import ProfilePage
from python_e2e_tests.pages.register_page import RegisterPage
from python_e2e_tests.pages.welcome_page import WelcomePage
from python_e2e_tests.pages.main_page import MainPage
from python_e2e_tests.pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(scope='function')
def welcome_page(page, app):
    welcome_page = WelcomePage(app, page).open_welcome_page()
    return welcome_page

@pytest.fixture(scope='function')
def register_page(welcome_page):
    register_page: RegisterPage= welcome_page.click_register()
    return register_page

@pytest.fixture(scope='function')
def login_page(welcome_page):
    login_page = welcome_page.click_login()
    return login_page

@pytest.fixture(scope='function')
def main_page(login_page, test_user):
    login, password = test_user
    main_page: MainPage = login_page.login(login, password)
    return main_page

@pytest.fixture(scope='function')
def profile_page(main_page):
    profile_page: ProfilePage = main_page.header.go_profile()
    return profile_page

@pytest.fixture(scope='session')
def test_user(niffler_auth_db, app):
    login = fake.user_name()
    password = fake.password()
    http_client = HttpClient(app)
    http_client.register(login, password, password)
    yield login, password
    niffler_auth_db.delete_user_data_by_username(login)

@pytest.fixture(scope='function')
def user_credentials(niffler_auth_db):
    username = fake.user_name()
    password = fake.password()
    yield username, password
    niffler_auth_db.delete_user_data_by_username(username)

@pytest.fixture(scope='function')
def test_category(niffler_spend_db):
    category_name = fake.word()
    yield category_name
    niffler_spend_db.delete_category_by_category_name(category_name)



def test_welcome_page(welcome_page):
    assert welcome_page.is_visible(welcome_page.WELCOME_TEXT)

def test_welcome_page_login_button(welcome_page):
    login_page: LoginPage = welcome_page.click_login()
    assert login_page.is_visible(login_page.SIGNIN_TEXT)

def test_welcome_page_register_button(welcome_page):
    register_page: RegisterPage= welcome_page.click_register()
    assert register_page.is_visible(register_page.SIGNUP_TEXT)

def test_registration(welcome_page, user_credentials, niffler_auth_db):
    login, password = user_credentials
    register_page: RegisterPage = welcome_page.click_register()
    register_page.register(login, password, password)
    assert register_page.is_visible(RegisterPage.SUCCESS_REGISTRATION_TEXT)
    assert niffler_auth_db.get_user_by_username(login)

def test_login(login_page, test_user):
    login, password = test_user
    main_page: MainPage = login_page.login(login, password)
    assert main_page.is_visible(main_page.HISTORY_OF_SPENDINGS_TEXT)

def test_redirect_to_login_from_register_page(register_page):
    login_page: LoginPage = register_page.click_signin_button()
    assert login_page.is_visible(login_page.SIGNIN_TEXT)

def test_redirect_to_register_from_login_page(login_page):
    register_page: RegisterPage = login_page.click_signup_button()
    assert register_page.is_visible(register_page.SIGNUP_TEXT)


def test_logout(main_page):
    welcome_page: WelcomePage = main_page.header.click_logout()
    assert welcome_page.is_visible(welcome_page.WELCOME_TEXT)

def test_success_add_new_category(profile_page, test_category):
    profile_page.create_category(test_category)
    assert profile_page.is_category_in_category_list(test_category)

def test_fail_add_new_category(profile_page):
    profile_page.create_category(' ')
    assert profile_page.is_visible(profile_page.CANT_ADD_NEW_CATEGORY_ALERT)




