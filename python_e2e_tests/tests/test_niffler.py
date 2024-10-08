from django.core.checks import register
from faker import  Faker
import pytest
from sqlalchemy import select
from sqlalchemy.testing.suite.test_reflection import users
from unicodedata import category

# from python_e2e_tests.models.authority import Authority
from python_e2e_tests.models.user_auth import UserAuth
from python_e2e_tests.models.user_auth import Authority
from python_e2e_tests.pages.profile_page import ProfilePage
from python_e2e_tests.pages.register_page import RegisterPage
from python_e2e_tests.pages.welcome_page import WelcomePage
from python_e2e_tests.pages.main_page import MainPage
from python_e2e_tests.pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(scope='function')
def test_user(niffler_auth_db, page):
    username = fake.user_name()
    password = fake.password()
    RegisterPage(page).open_register_page().register(username, password, password)
    user_credentials = {'login': username, 'password': password}
    yield user_credentials
    user_id_query = select(UserAuth.id).where(UserAuth.username == username)
    user_id = niffler_auth_db.get_session().execute(user_id_query).scalar()
    authority_ids_query = select(Authority.id).where(Authority.user_id == user_id)
    authority_ids = niffler_auth_db.get_session().execute(authority_ids_query).scalars().all()
    for authority_id in authority_ids:
        niffler_auth_db.delete_by_id(Authority, authority_id)
    niffler_auth_db.delete_by_id(Authority, authority_id)
    niffler_auth_db.delete_by_id(UserAuth, user_id)

@pytest.fixture(scope='function')
def get_user_credentials(niffler_auth_db):
    username = fake.user_name()
    password = fake.password()
    user_credentials = {'login': username, 'password': password}
    yield user_credentials
    user_id_query = select(UserAuth.id).where(UserAuth.username == username)
    user_id = niffler_auth_db.get_session().execute(user_id_query).scalar()
    authority_ids_query = select(Authority.id).where(Authority.user_id == user_id)
    authority_ids = niffler_auth_db.get_session().execute(authority_ids_query).scalars().all()
    for authority_id in authority_ids:
        niffler_auth_db.delete_by_id(Authority, authority_id)
    niffler_auth_db.delete_by_id(Authority, authority_id)
    niffler_auth_db.delete_by_id(UserAuth, user_id)


def test_welcome_page(page):
    welcome_page = WelcomePage(page).open_welcome_page()
    login_page = welcome_page.click_login()
    assert login_page.page.locator(login_page.signin_text).is_visible()

def test_welcome_page_login_button(page):
    welcome_page = WelcomePage(page).open_welcome_page()
    login_page = welcome_page.click_login()
    assert login_page.page.locator(login_page.signin_text).is_visible()

def test_welcome_page_register_button(page):
    welcome_page = WelcomePage(page).open_welcome_page()
    register_page = welcome_page.click_register()
    assert register_page.page.locator(register_page.signup_text).is_visible()

def test_registration(page, get_user_credentials):
    welcome_page = WelcomePage(page).open_welcome_page()
    register_page = welcome_page.click_register()
    register_page.register(get_user_credentials.get('login'), get_user_credentials.get('password'), get_user_credentials.get('password'))
    assert register_page.page.locator(register_page.success_registration_text).is_visible()

def test_login(page, test_user):
    login_page = WelcomePage(page).open_welcome_page().click_login()
    main_page = login_page.login(test_user.get('login'), test_user.get('password'))
    page.wait_for_selector(MainPage.history_of_spendings_text)
    assert main_page.page.locator(MainPage.history_of_spendings_text).is_visible()

def test_redirect_to_login_from_register_page(page, test_user):
    welcome_page = WelcomePage(page).open_welcome_page()
    register_page = welcome_page.click_register()
    login_page = register_page.click_signin_button()
    page.wait_for_selector(login_page.signin_text)
    assert login_page.page.locator(login_page.signin_text).is_visible()

def test_redirect_to_register_from_login_page(page, test_user):
    welcome_page = WelcomePage(page).open_welcome_page()
    login_page = welcome_page.click_login()
    register_page = RegisterPage(login_page.click_signup_button().page)
    page.wait_for_selector(register_page.signup_text)
    assert register_page.page.locator(register_page.signup_text).is_visible()


def test_logout(page, test_user):
    login_page = WelcomePage(page).open_welcome_page().click_login()
    main_page = login_page.login(test_user.get('login'), test_user.get('password'))
    welcome_page = WelcomePage(main_page.logout())
    page.wait_for_selector(WelcomePage.welcome_text)
    assert welcome_page.page.locator(WelcomePage.welcome_text).is_visible()

def test_success_add_new_category(page, test_user):
    login_page = WelcomePage(page).open_welcome_page().click_login()
    main_page = login_page.login(test_user.get('login'), test_user.get('password'))
    profile_page = ProfilePage(main_page.go_profile())
    category_name = fake.word()
    profile_page.create_category(category_name)
    assert profile_page.is_category_in_category_list(category_name)

def test_fail_add_new_category(page, test_user):
    login_page = WelcomePage(page).open_welcome_page().click_login()
    main_page = login_page.login(test_user.get('login'), test_user.get('password'))
    profile_page = ProfilePage(main_page.go_profile())
    profile_page.create_category(' ')
    page.wait_for_selector(profile_page.cant_add_new_category_alert)
    assert profile_page.page.locator(profile_page.cant_add_new_category_alert).is_visible()




