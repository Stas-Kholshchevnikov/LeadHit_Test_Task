

class PatternDAO:
    """
    Класс работы с БД
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Функция получения всех записей из БД
        :return:
        """
        try:
            return self.session.all()
        except Exception as err:
            return err


