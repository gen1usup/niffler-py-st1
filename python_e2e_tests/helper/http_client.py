import requests
from bs4 import BeautifulSoup


class HttpClient:
    def __init__(self, app):
        self.session = requests.Session()
        self.app = app
        self.base_url= self.app.base_url
        self.auth_url = self.app.auth_url

    def get_csrf_token(self, register_url):
        get_response = self.session.get(register_url)
        soup = BeautifulSoup(get_response.text, 'html.parser')
        csrf_token_input = soup.find('input', {'name': '_csrf'})
        if csrf_token_input:
            csrf_token = csrf_token_input.get('value')
        else:
            raise ValueError("CSRF token not found in the registration page.")
        return csrf_token

    def register(self, username, password, submit_password):
        register_url = self.auth_url + self.app.paths['RegisterPage']
        csrf_token = self.get_csrf_token(register_url)
        data = {
            'username': username,
            'password': password,
            'passwordSubmit': submit_password,
            '_csrf': csrf_token
        }
        response = self.session.post(register_url, data=data)
        return response