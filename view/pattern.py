from flask_restx import Resource, Namespace
from flask import request

from implemented import pattern_service

#Создание Namespace
pattern_ns = Namespace("get_form")

@pattern_ns.route("/")
class PatternView(Resource):
    """
    CBV для обработки запросов http
    """
    def post(self):
        data = request.data.decode()
        pre_data = pattern_service.preparing_data(data)
        result = pattern_service.check_data(pre_data)
        return result
