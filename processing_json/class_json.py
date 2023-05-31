from requests_classes.hh_req.hh_req import HH_request
from requests_classes.SJ_request.SJ_req import SJ_request
import json
from app_dialog.exceptions import ErrorServiceName


class JsonProcessing:
    """Класс для создания, заполнения и чтения файла"""
    Urls = 'files/result.json'
    json_file_name = 'files/result.json'

    @classmethod
    def create_file(cls, text, servise_name) -> None:
        """Сохранение файлов в json"""
        with open(cls.json_file_name, 'w', encoding='utf-8') as file:
            if servise_name == "1":
                ex_data = HH_request(text)
            elif servise_name == "2":
                ex_data = SJ_request(text)
            else:
                raise ErrorServiceName
            data = ex_data.get_data()
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_data_from_json(cls):
        """Прочитать файл .json"""
        with open(cls.json_file_name, 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)