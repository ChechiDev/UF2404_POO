import matplotlib.pyplot as plt
from .utils.json_builder import JsonBuilder
from .weather import WeatherStation
import os

class GraphGenerator:
    def __init__(self, cityname: list = None, days: int = None):
        self._city_name = cityname
        self._days = days
        self.data = None

        self.w_st = WeatherStation(cityname)

    def plot_temp(self):
        data = JsonBuilder.read_json()
        city_data = data.get(self._city_name)

        if not data:
            print(f"No data found...")
            return

        min_temp = []
        med_temp = []
        max_temp = []

        for i in range(1, self._days + 1):
            day_data = city_data.get(f"Day-{i}")
            if day_data:
                min_temp.append(day_data.get("min_temp", 0))
                med_temp.append(day_data.get("med_temp", 0))
                max_temp.append(day_data.get("max_temp", 0))

        print("min: ", min_temp)
        print("med: ", med_temp)
        print("max: ", max_temp)



if __name__ == "__main__":
    os.system("cls")
    graph = GraphGenerator("Barcelona", days=30)
    graph.plot_temp()
