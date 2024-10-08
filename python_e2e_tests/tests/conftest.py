import dotenv
dotenv.load_dotenv()

from python_e2e_tests.helper.niffler_auth_database import NifflerAuthDB
from python_e2e_tests.helper.niffler_currency_database import NifflerCurrencyDB
from python_e2e_tests.helper.niffler_spend_database import NifflerSpendDB
from python_e2e_tests.helper.niffler_userdata_database import NifflerUserdataDB


import pytest
from playwright.sync_api import Browser, Page, sync_playwright



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
def niffler_auth_db():
    niffler_auth_db = NifflerAuthDB()
    yield niffler_auth_db

@pytest.fixture(scope='session')
def niffler_currency_db():
    niffler_currency_db = NifflerCurrencyDB()
    yield niffler_currency_db


@pytest.fixture(scope='session')
def niffler_userdata_db():
    niffler_userdata_db = NifflerUserdataDB()
    yield niffler_userdata_db

@pytest.fixture(scope='session')
def niffler_spend_db():
    niffler_spend_db = NifflerSpendDB()
    yield niffler_spend_db


