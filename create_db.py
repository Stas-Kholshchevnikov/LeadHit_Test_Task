def create_form_tiny(db):
    """
    Функция наполнения данными БД
    :param db:
    :return:
    """

    db.truncate()

    form = {"form_name": "test", "+7 988 497 42 00": "telephone", "xcd85@mail.ru": "email"}
    form1 = {"form_name": "test1", "+7 917 832 18 25": "telephone", "mail85@mail.ru": "email", "09.01.2023": "date"}
    form2 = {"form_name": "test2", "+7 888 451 00 17": "telephone", "10.01.2023": "date"}
    form3 = {"form_name": "test3", "Test text": "text", "11.01.2023": "date"}

    db.insert_multiple([form, form1, form2, form3])
