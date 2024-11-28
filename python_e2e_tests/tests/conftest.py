import os

from dotenv import load_dotenv

from python_e2e_tests.helper.application import App
from python_e2e_tests.databases.niffler_auth_database import NifflerAuthDB
from python_e2e_tests.databases.niffler_currency_database import NifflerCurrencyDB
from python_e2e_tests.databases.niffler_spend_database import NifflerSpendDB
from python_e2e_tests.databases.niffler_userdata_database import NifflerUserdataDB


import pytest
from playwright.sync_api import Browser, Page, sync_playwright

@pytest.fixture(scope='session')
def env():
    load_dotenv()

@pytest.fixture(scope='session')
def app(env):
    app = App(os.getenv('ENVS'))
    yield app

@pytest.fixture(scope='function')
def page() -> Page:
    """Получить WebDriver."""
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(channel="chrome", headless=False)
        page: Page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope='session')
def niffler_auth_db(app):
    niffler_auth_db = NifflerAuthDB(app.niffler_auth_db_config)
    yield niffler_auth_db

@pytest.fixture(scope='session')
def niffler_currency_db(app):
    niffler_currency_db = NifflerCurrencyDB(app.niffler_currency_db_config)
    yield niffler_currency_db


@pytest.fixture(scope='session')
def niffler_userdata_db(app):
    niffler_userdata_db = NifflerUserdataDB(app.niffler_userdata_db_config)
    yield niffler_userdata_db

@pytest.fixture(scope='session')
def niffler_spend_db(app):
    niffler_spend_db = NifflerSpendDB(app.niffler_spend_db_config)
    yield niffler_spend_db


