import matplotlib.pyplot as plt
from .utils.json_builder import JsonBuilder
from .weather import WeatherStation
import os

class GraphGenerator:
    def __init__(self, days: int = 0):
        self._days = days
        self.data = JsonBuilder.read_json()
        self.city_names = list(self.data.keys()) if self.data else []

        self.w_st = WeatherStation(self.city_names)


    def get_data(self, cities_name = None, days = None):

        plot_result = {}

        for city in self.city_names:
            # print(self.data[city])
            for day, temp in self.data[city].items():
                print(f"{city}: min_temp = {temp['min_temp']}")



    def plot_temp(self):
        pass


if __name__ == "__main__":
    import pprint
    os.system("cls")
    # graph = GraphGenerator("Barcelona", days=30)
    # graph.plot_temp()
    g = GraphGenerator()
    print(g.get_data())
    # pprint.pprint(g.data)
