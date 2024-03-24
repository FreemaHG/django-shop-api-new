from rest_framework.exceptions import APIException


class NotFoundResponseException(APIException):
    """
    Исключение для возврата ответа при отсутствии запрашиваемой записи
    """

    status_code = 404
    default_detail = 'Запись не найдена'


class InvalidDataResponseException(APIException):
    """
    Исключение для возврата ответа при передаче невалидных данных
    """

    status_code = 400
    default_detail = 'Переданы невалидные данные'
