from ..weather import WeatherStation
from .json_builder import JsonBuilder

class DictBuilder:
    def __init__(self, w_st):
        # Instancia a la clase WeatherStation
        self.w_st = w_st

    def to_dict(self, days: int = 30):
        data = {}

        for i in range (1, days + 1):
            temp_array = self.w_st._temp_range()
            temp_data = {
                "min_temp": int(self.w_st.min_temp(days)),
                "med_temp": int(self.w_st.med_temp(days)),
                "max_temp": int(self.w_st.max_temp(days)),
            }
            data[f"Day-{i}"] = temp_data

        self.w_st._cities_data[self.w_st._name] = data

        return {self.w_st._name: data}


    @staticmethod
    def print_dict(data):
        for k, v in data.items():
            if isinstance(v, dict):
                print(f"{k}: ")

            else:
                print(f"{k}: {v if v else ""}")