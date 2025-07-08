# src.graph.py

import matplotlib.pyplot as plt
from .utils.json_builder import JsonBuilder
from .weather import WeatherStation

class GraphGenerator:
    """ Generates and plots temperature data graphs for weather stations """
    def __init__(self):
        """ Initializes the graph generator with city data and weather station """
        self.data = JsonBuilder.read_json()
        self._city_names = list(self.data.keys()) if self.data else []

        self.w_st = WeatherStation(self._city_names)
        self._days = self.w_st._max_days


    def get_data(self):
        """ Get temperature data for all cities from JSON """

        plot_result = {}

        for city in self._city_names:
            city_key = self.data.get(city)
            min_temp = []
            med_temp = []
            max_temp = []

            for i in range(1,  self._days + 1):
                data_day = city_key.get(f"Day-{i}")

                # si hay datos...
                if data_day:
                    min_temp.append(data_day.get("min_temp", 0))
                    med_temp.append(data_day.get("med_temp", 0))
                    max_temp.append(data_day.get("max_temp", 0))

            plot_result[city] = [min_temp, med_temp, max_temp]

        return plot_result


    def plot_temp_type(self, temp_index: int, label_name: str):
        """ Plots a specific type of temperature (min, med, max) for all cities """

        data = self.get_data()
        days_list = list(range(1, self._days + 1))
        plt.figure(figsize=(15, 5))

        for city, temps in data.items():
            temp = temps[temp_index]
            plt.plot(days_list, temp, label=f"{city} {label_name}")

        plt.title(f"Temperature comparison for the cities: {', '.join(self._city_names)}")
        plt.xlabel(f"Temperature over {self._days} days")
        plt.ylabel("Temperature (°C)")
        plt.xticks(range(0, self._days + 1))
        plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
        plt.show()


    def plot_min_temp(self):
        """ Plots minimum temperature for all cities """
        self.plot_temp_type(0, "Min. temp.")


    def plot_med_temp(self):
        """ Plots medium temperature for all cities """
        self.plot_temp_type(1, "Med. temp.")


    def plot_max_temp(self):
        """ Plots maximum temperature for all cities """
        self.plot_temp_type(2, "Max. temp.")


    def plot_temp(self):
        """ Plots all temperature types (min, med, max) for all cities """

        data = self.get_data()
        days_list = list(range(1, self._days + 1))
        plt.figure(figsize=(15, 5))

        for city, temps in data.items():
            plt.plot(days_list, temps[0], label=f"{city} Min. temp.")
            plt.plot(days_list, temps[1], label=f"{city} Med. temp.")
            plt.plot(days_list, temps[2], label=f"{city} Max. temp.")

        plt.title(f"Temperature comparison for the cities: {', '.join(self._city_names)}")
        plt.xlabel(f"Temperature over {self._days} days")
        plt.ylabel("Temperature (°C)")
        plt.xticks(range(0, self._days + 1))
        plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
        plt.show()
