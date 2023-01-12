import datetime
import re

from dao.pattern import PatternDAO
import phonenumbers


class PatternService:
    def __init__(self, dao: PatternDAO):
        self.dao = dao

    def preparing_data(self, data):
        """
        Преобразование в словарь данных, полуенных из POST запроса
        :param data:
        :return:
        """
        result_list = data.strip().split("&")
        result_dict = {}
        for item in result_list:
            list = item.strip().split("=")
            result_dict[list[0]] = list[1]
        return result_dict

    def check_data(self, data):
        """
        Проверка на валидность данных определнному типу
        :param data:
        :return:
        """
        input_data = {}
        for key, value in data.items():
            if self.is_date(value):
                input_data[value] = "date"
                continue
            if self.is_number(value):
                input_data[value] = "telephone"
                continue
            if self.is_email(value):
                input_data[value] = "email"
                continue
            else:
                input_data[value] = "text"
        data_db = self.dao.get_all()
        result = self.check_form(input_data, data_db)
        if result is not None:
            return result
        else:
            return input_data


    def is_number(self, value):
        """
        Функиция проверки на данные типа "номер телефона"
        :param value:
        :return:
        """
        try:
            number = phonenumbers.parse(value)
            if phonenumbers.is_valid_number(number):
                return True
        except Exception:
            pass
        return False


    def is_email(self, value):
        """
        Функиция проверки на данные типа "электронная почта"
        :param value:
        :return:
        """
        if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", value):
            return True
        else:
            return False

    def is_date(self, value):
        """
        Функиция проверки на данные типа "дата"
        :param value:
        :return:
        """
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return True
        except Exception:
            try:
                datetime.datetime.strptime(value, '%d.%m.%Y')
                return True
            except Exception:
                pass
        return False

    def check_form(self, input_data, data_db):
        """
        Функция сопоставления данных из запроса с данными из БД
        :param input_data:
        :param data_db:
        :return:
        """
        for item_db in data_db:
            count = 0
            for key, value in item_db.items():
                if (key != "_id") and (key != "form_name"):
                    if key in input_data:
                        if item_db[key] == input_data[key]:
                            count += 1
                    else:
                        continue
                else:
                    continue
                if count == len(input_data):
                    return {"form_name": item_db["form_name"]}
        return None
