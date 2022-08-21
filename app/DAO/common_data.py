import json
from json import JSONDecodeError

from exceptions.data_exceptions import DataSourceError


class CommonData:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)

        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из {self.path}')

        return data
