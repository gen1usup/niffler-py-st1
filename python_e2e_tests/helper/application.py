import json

import dotenv
from typing import Dict, Any

from python_e2e_tests.helper.path_finder import get_path_to_file

dotenv.load_dotenv()

class App:
    def __init__(self, env):
        self.configs = self.load_configs(env)
        self.base_url = None
        self.auth_url = None
        for config, value in self.configs.items():
            setattr(self, config, value)
        self.niffler_auth_db_config = self.database.get('niffler_auth')
        self.niffler_spend_db_config = self.database.get('niffler_spend')
        self.niffler_userdata_db_config = self.database.get('niffler_userdata')
        self.niffler_currency_db_config = self.database.get('niffler_currency')
        self.paths = Paths()

    def load_configs(self, env) -> Dict[str, Any]:
        path_to_config = get_path_to_file('configs.json')
        with open(path_to_config, 'r') as file:
            configs = json.load(file)
        env_configs = configs.get(env)
        if not env_configs:
            raise ValueError(f"Configuration for environment '{env}' not found.")
        return env_configs


class Paths:
    def __init__(self):
        self.login_page = '/login'
        self.main_page = '/main'
        self.profile_page = '/profile'
        self.register_page = '/register'
        self.welcome_page = '/'

