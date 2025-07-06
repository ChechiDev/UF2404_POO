import numpy as np
from .utils import DictBuilder, JsonBuilder

class WeatherStation:
    def __init__(self, name: str) -> None:
        self._name = name
        self._min_temp_range = np.random.randint(15, 20)
        self._max_temp_range = np.random.randint(30, 36)
        self._min_temp = self.min_temp()
        self._med_temp = self.med_temp()
        self._max_temp = self.max_temp()
        self._max_days = 30
        self._temp_resume = {}
        self._cities_data = {}

    def _temp_range(self, min_temp = None, max_temp = None, max_days = 30):
        min_temp = self._min_temp_range
        max_temp = self._max_temp_range

        temp = np.random.randint(min_temp, max_temp, max_days)
        return temp

    def min_temp(self, max_days=30):
        temp = np.min(self._temp_range())
        return int(temp)

    def med_temp(self, max_days=30):
        temp = np.mean(self._temp_range())
        return int(temp)

    def max_temp(self, max_days=30):
        temp = np.max(self._temp_range())
        return int(temp)

    def get_daily_temp(self):

        # Devolvemos el array para matplotlib:
        return [self.min_temp(), self.med_temp(), self.max_temp()]

    def temp_resume(self):
        self._temp_resume = {
            "name": self._name,
            "min_temp": self.min_temp(),
            "med_temp": self.med_temp(),
            "max_temp": self.max_temp()
        }
        return self._temp_resume

    def add_city(self, name: str):
        temp_array = self._temp_range()
        data = {
            "name": name,
            "min_temp": int(np.min(temp_array)),
            "med_temp": int(np.mean(temp_array)),
            "max_temp": int(np.max(temp_array))
        }

        self._cities_data[name] = data

        # Generamos el Json:
        self.JsonBuilder.write_json(self._cities_data)

        return data