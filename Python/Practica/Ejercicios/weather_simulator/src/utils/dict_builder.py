

class DictBuilder:
    def __init__(self, w_st):
        # Instancia a la clase WeatherStation
        self.w_st = w_st

    def to_dict(self):
        if self.w_st._cities_data:
            return self.w_st._cities_data

        else:
            return {
                self.w_st._name: {
                    "name": self.w_st._name,
                    "min_temp": self.w_st._min_temp,
                    "med_temp": self.w_st._med_temp,
                    "max_temp": self.w_st._max_temp
                }
            }


    @staticmethod
    def print_dict(data):
        for k, v in data.items():
            if isinstance(v, dict):
                print(f"{k}: ")

            else:
                print(f"{k}: {v if v else ""}")