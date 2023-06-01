from processing_json.class_json import JsonProcessing
from processing_data.processing_data import ProcessingData
from app_dialog.exceptions import ErrorNotData


class Dialog:

    @staticmethod
    def first_dialog():
        """Вывод приветствия"""
        print('Здравствуйте!\nВас приветствует парсер вакансий Head Hunter и Superjob!')
        print('Для продолжения выберите платформу для парсинга')
        print('1 - Head Hunter')
        print('2 - Superjob\n')

    @staticmethod
    def choice_servise():
        """Выбор сервиса"""
        global service
        input_service = True
        while input_service:
            service = input()
            if service == '1' or service == '2':
                input_service = False
            else:
                print('У нас нет такого сервиса! Попробуйте ещё раз!')
        return service

    @staticmethod
    def input_key():
        """Ввод ключевого слова"""
        global word
        print('Введите слово или фразу для поиска для поиска\n')
        input_word = True

        while input_word:
            word = input()
            if word != '':
                input_word = False
            else:
                print('Нужно ввести хоть что-нибудь')
        return word

    @staticmethod
    def requests(word, service):
        try:
            JsonProcessing.create_file(word, service)
            list_vacancies = ProcessingData.get_vacancies_list(service)
            if len(list_vacancies) == 0:
                raise ErrorNotData
            else:
                for vacancies in list_vacancies:
                    print(vacancies.beautiful_output() + f'\n{"=" * 50}\n')
                    pass
        except ErrorNotData:
            print("Отсутствуют вакансии по указанному ключевому слову")
        return list_vacancies

    @staticmethod
    def sort(list_vacancies):
        if service == "1":
            sort = sorted(list_vacancies, key=lambda d: (d.salary.to, d.salary.from_))
        else:
            sort = sorted(list_vacancies, key=lambda d: (d.payment_to, d.payment_from))

        for element in sort:
            print(element.beautiful_output() + f'\n{"=" * 50}\n')