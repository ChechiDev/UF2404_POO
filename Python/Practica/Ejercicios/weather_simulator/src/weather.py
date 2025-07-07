# src.weather.py

import numpy as np

class WeatherStation:
    """ Simulates a weather station and generates temperature data """
    def __init__(self, name: str) -> None:
        """ Initializes the weather station with a name and random temperature ranges """
        self._name = name
        self._max_days = 30
        self._min_temp_range = np.random.randint(15, 20)
        self._max_temp_range = np.random.randint(30, 36)
        self._min_temp = self.min_temp()
        self._med_temp = self.med_temp()
        self._max_temp = self.max_temp()
        self._temp_resume = {}
        self._cities_data = {}


    def _temp_range(self, min_temp = None, max_temp = None, max_days = 30):
        """ Generates a random temperature array for the given range and days """

        min_temp = self._min_temp_range
        max_temp = self._max_temp_range

        temp = np.random.randint(min_temp, max_temp, max_days)
        return temp


    def min_temp(self, max_days: int =30) -> int:
        """ Returns the minimum temperature for the max_days """

        temp = np.min(self._temp_range())
        return int(temp)


    def med_temp(self, max_days: int =30) -> int:
        """ Returns the medium temperature for the max_days """

        temp = np.mean(self._temp_range())
        return int(temp)


    def max_temp(self, max_days: int =30) -> int:
        """ Returns the maximum temperature for the max_days """
        temp = np.max(self._temp_range())
        return int(temp)


    def get_daily_temp(self) -> list:
        """ Returns a list with min, med, and max temperature for plotting """

        # Devolvemos el array para matplotlib:
        return [self.min_temp(), self.med_temp(), self.max_temp()]