import json

from django.http import QueryDict


def reading_data_from_request(raw_data: QueryDict | dict) -> dict:
    """
    Преобразование и возврат сырых данных, переданных из запроса, в виде словаря

    Т.к. из фронта и swagger данные приходят в разном виде (в виде json-строки и словаря соответственно),
    проверяем и возвращаем преобразованные данные для дальнейшей обработки
    """

    if isinstance(raw_data, QueryDict):
        data = list(dict(raw_data).keys())[0]  # Достаем ключ из QueryDict - словарь с данными
        return json.loads(data)

    return raw_data
