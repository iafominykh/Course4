from requests_classes.abs import Service
import requests
import json


class SJ_request(Service):
    """Класс запроса вакансий на SJ"""

    def __init__(self, text='python'):
        self.text = text
        self.headers = {
            'X-Api-App-Id':
                'v3.r.137578346.d369b9f6bdbcf0adbcff50a82b9bcef11cfc4ce9.bceb8d7fcabc04dec025dead632d4051f66acd3d',
        }
        self.params = [
            ("keywords", [("srws", 1), ("skwc", "particular"), ("keys", self.text)]),

            ("period", 0),
            ("count", 100)
        ]
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    @staticmethod
    def autorization():
        """Метод авторизации"""
        respon = requests.get(
            url=f'https://api.superjob.ru/2.0/oauth2/password/',
            headers={
                'X-Api-App-Id':
                    'v3.r.137578346.d369b9f6bdbcf0adbcff50a82b9bcef11cfc4ce9.bceb8d7fcabc04dec025dead632d4051f66acd3d',
            },
            params={
                'login': 'dronramone@mail.ru',
                'password': 'Created_1990',
                'client_id': '2265',
                'client_secret':
                    'v3.r.137578346.d369b9f6bdbcf0adbcff50a82b9bcef11cfc4ce9.bceb8d7fcabc04dec025dead632d4051f66acd3d',
            }
        )
        print(respon.text)

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            headers=self.headers,
            params=self.params,
        )
        return respon.json()
