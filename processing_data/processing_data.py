from processing_json.class_json import JsonProcessing
from filtering.filtering_hh import Vacancies
from filtering.filtering_SJ import Vacancies_SJ
from pydantic import ValidationError


class ProcessingData:
    """Класс создания списка вакансий"""

    @staticmethod
    def get_vacancies_list(choice_servis):
        """Создать список вакансий"""
        global parametr, objection
        vacancies_list = []
        if choice_servis == "2":
            parametr = "objects"
            objection = Vacancies_SJ
        elif choice_servis == "1":
            parametr = 'items'
            objection = Vacancies

        for number, key in enumerate(JsonProcessing.get_data_from_json().get(parametr)):
            try:
                vacancies_list.append(objection(**key))
            except ValidationError:
                print(f'Не валидные данные в вакансии №{number}')
                continue
        return vacancies_list
    