from tinydb import TinyDB


def connect_to_db_tinydb():
    """
    Создание подклчения к таблице testleadhit БД tinydb
    :return:
    """
    connect = TinyDB('leadhit.json')
    return connect
