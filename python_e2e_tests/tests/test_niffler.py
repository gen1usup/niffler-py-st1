
from faker import  Faker
from bs4 import BeautifulSoup
import pytest
import requests
from fastapi_pagination import response

from python_e2e_tests.helper.http_client import HttpClient
from python_e2e_tests.models.user_auth import UserAuth
from python_e2e_tests.models.user_auth import Authority
from python_e2e_tests.pages.profile_page import ProfilePage
from python_e2e_tests.pages.register_page import RegisterPage
from python_e2e_tests.pages.welcome_page import WelcomePage
from python_e2e_tests.pages.main_page import MainPage
from python_e2e_tests.pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(scope='function')
def welcome_page(page, app):
    page.goto(app.base_url)
    welcome_page = WelcomePage(app, page)
    yield welcome_page

@pytest.fixture(scope='function')
def register_page(welcome_page):
    register_page: RegisterPage= welcome_page.click_register()
    yield register_page

@pytest.fixture(scope='function')
def login_page(welcome_page):
    login_page = welcome_page.click_login()
    yield login_page

@pytest.fixture(scope='function')
def main_page(login_page, test_user):
    login, password = test_user
    main_page: MainPage = login_page.login(login, password)
    yield main_page

@pytest.fixture(scope='function')
def profile_page(main_page):
    profile_page: ProfilePage = main_page.header.go_profile()
    yield profile_page

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

def test_welcome_page(welcome_page):
    assert welcome_page.is_visible(welcome_page.locators['welcome_text'])

def test_welcome_page_login_button(welcome_page):
    login_page: LoginPage = welcome_page.click_login()
    assert login_page.is_visible(login_page.locators['signin_text'])

def test_welcome_page_register_button(welcome_page):
    register_page: RegisterPage= welcome_page.click_register()
    assert register_page.is_visible(register_page.locators['signup_text'])

def test_registration(welcome_page, user_credentials):
    login, password = user_credentials
    register_page: RegisterPage= welcome_page.click_register()
    register_page.register(login, password, password)
    assert register_page.is_visible(RegisterPage.locators['success_registration_text'])

def test_login(login_page, test_user):
    login, password = test_user
    main_page: MainPage = login_page.login(login, password)
    assert main_page.is_visible(main_page.locators['history_of_spendings_text'])

def test_redirect_to_login_from_register_page(register_page):
    login_page: LoginPage = register_page.click_signin_button()
    signin_text = login_page.locators['signin_text']
    assert login_page.is_visible(signin_text)

def test_redirect_to_register_from_login_page(login_page):
    register_page: RegisterPage = login_page.click_signup_button()
    signup_text = register_page.locators['signup_text']
    assert register_page.is_visible(signup_text)


def test_logout(main_page):
    welcome_page: WelcomePage = main_page.header.click_logout()
    assert welcome_page.is_visible(welcome_page.locators['welcome_text'])

def test_success_add_new_category(profile_page):
    category_name = fake.word()
    profile_page.create_category(category_name)
    assert profile_page.is_category_in_category_list(category_name)

def test_fail_add_new_category(profile_page):
    profile_page.create_category(' ')
    error_text = profile_page.locators['cant_add_new_category_alert']
    assert profile_page.is_visible(error_text)




