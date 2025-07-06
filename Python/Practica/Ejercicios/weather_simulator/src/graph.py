import matplotlib.pyplot as plt
from .utils.json_builder import JsonBuilder
from .weather import WeatherStation

class GraphGenerator:
    def __init__(self, cityname: list = None, days: int = None):
        self._city_name = cityname
        self._days = days
        self.data = None

        self.w_st = WeatherStation(cityname)

    def plot_temp(self):
        # data = JsonBuilder.read_json()
        # plt.figure(figsize=(10, 6))

        for i in range(self._days):
            print(f"day {i+1}: {self.w_st.get_daily_temp()}")


if __name__ == "__main__":
    graph = GraphGenerator("Barcelona", days=30)
    graph.plot_temp()