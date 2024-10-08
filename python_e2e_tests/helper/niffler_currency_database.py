import os

from python_e2e_tests.helper.base_database import BaseDatabase
from python_e2e_tests.models.user_userdata import User


class NifflerCurrencyDB(BaseDatabase):
    def __init__(self):
        self.db_url = f'postgresql://{os.getenv("DB_NIFFLER_CURRENCY_USER")}:{os.getenv("DB_NIFFLER_CURRENCY_PASSWORD")}@{os.getenv("HOST_DB_IN_DOCKER")}:{os.getenv("PORT_DB")}/{os.getenv("DB_NAME_NIFFLER_CURRENCY")}'
        super().__init__(self.db_url)

