from python_e2e_tests.databases.base_database import BaseDatabase


class NifflerCurrencyDB(BaseDatabase):
    def __init__(self, config):
        super().__init__(config)

