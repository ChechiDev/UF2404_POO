from .weather import WeatherStation
from .utils import (
    Utils,
    Validation,
    DictBuilder,
    JsonBuilder
)
from time import sleep

class BaseMenu:
    def __init__(self):
        self.weather_station = None


    def main_menu(self):
        opts = ["New Station seach", "Show Station Data"]

        while True:
            Utils.clear_terminal()
            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}\n")

            user_opt = input("Select an option: ")

            if user_opt == "1":
                self.new_weather_st()

            else:
                print("Wrong option...")
                sleep(2)


    def new_weather_st(self):

        # Limpiamos JSON para nueva búsqueda:
        JsonBuilder.clear_json()

        while True:
            Utils.clear_terminal()
            JsonBuilder.get_cities()
            name = input("New weather station: ").strip().title()

            # Comprobamos si name existe
            if JsonBuilder.check_city(name):
                print(f"The station '{name}' already exists. Choose another name.")
                sleep(2)
                continue

            if Validation.is_valid_name(name):
                w_st = WeatherStation(name)

                # Generamos el dict:
                dbuild = DictBuilder(w_st)
                st_dict = dbuild.to_dict()

                # Actualizamos el JSON:
                JsonBuilder.write_json(st_dict)
                print(f"{name} added succesfully!")

                # Mostramos la city que se ha agregado
                Utils.clear_terminal()
                JsonBuilder.get_cities()

                # Se quiere agregar mas ?
                new_input = input("Do you want to add another city? (y/n): ").strip().lower()
                if new_input != "y":
                    return w_st

            else:
                Utils.clear_terminal()
                print("Wrong station name...")
                sleep(2)


if __name__ == "__main__":
    Utils.clear_terminal()
    menu = BaseMenu()
    menu.main_menu()