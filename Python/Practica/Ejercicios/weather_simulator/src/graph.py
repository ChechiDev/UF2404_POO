import matplotlib.pyplot as plt
from .utils.json_builder import JsonBuilder
from .weather import WeatherStation
import os
import pprint
import json

class GraphGenerator:
    def __init__(self):
        self.data = JsonBuilder.read_json()
        self.city_names = list(self.data.keys()) if self.data else []

        self.w_st = WeatherStation(self.city_names)
        self._days = self.w_st._max_days


    def get_data(self):

        plot_result = {}

        for city in self.city_names:
            city_key = self.data.get(city)
            # print(city_key)
            min_temp = []
            med_temp = []
            max_temp = []

            for i in range(1,  self._days + 1):
                data_day = city_key.get(f"Day-{i}")
                # print(data_day)

                # si hay datos...
                if data_day:
                    min_temp.append(data_day.get("min_temp", 0))
                    med_temp.append(data_day.get("med_temp", 0))
                    max_temp.append(data_day.get("max_temp", 0))

            plot_result[city] = [min_temp, med_temp, max_temp]
            # print(json.dumps(plot_result, indent=4))

        return plot_result


    def plot_temp(self):
        data = self.get_data()

        for city, temps in data.items():
            min_temp = temps[0]
            med_temp = temps[1]
            max_temp = temps[2]
            print(city, min_temp, med_temp, max_temp)



if __name__ == "__main__":
    os.system("cls")
    # graph = GraphGenerator("Barcelona", days=30)
    # graph.plot_temp()
    g = GraphGenerator()
    g.plot_temp()
    # pprint.pprint(g.data)
