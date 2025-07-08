# menu.py (main)

from time import sleep
from src import (
    Utils,
    Validation,
    WeatherStation,
    GraphGenerator,
    DictBuilder,
    JsonBuilder
)

class BaseMenu:
    """ Base class for menu screens and shared menu utilities """
    def __init__(self):
        """ Initializes menu with utility, validation, and graph instances """
        # Instancias:
        self.ut = Utils()
        self.val = Validation()
        self.graph = GraphGenerator()

        self._header_pattern = "="
        self._header_width = 100
        self._header_title = "Weather Station Temperature Data Analysis"

    def center(self, text: str, width: int = None) -> str:
        """ Centers the given text within the specified width """

        if width is None:
            width = self._header_width

        return text.center(width)


    def header(self):
        """ Prints the game header with a centered title and decorative lines. """

        print(self._header_pattern * self._header_width)
        print(self.center("Weather Station Temperature Data Analysis"))
        print(self._header_pattern * self._header_width)


    def separator(self):
        """ Prints a separation barr """

        print("\n" * 2)
        print(self._header_pattern * self._header_width)


    def footer(self):
        """ Prints a footer for the menu """

        print("\n" * 2)
        print("0. Exit")
        print(self._header_pattern * self._header_width)


class ExitMenu(BaseMenu):
    def exit(self):
        """ Shows the exit menu """

        self.ut.clear_terminal()
        self.header()
        print(f"Thank you for visiting us!")
        self.separator()


class LandingMenu(BaseMenu):
    """ Main landing menu for the weather simulator """

    def main_menu(self):
        """ Displays the main menu and handles user navigation """

        opts = ["Add new Weather station to temperature analysis"]

        while True:
            self.ut.clear_terminal()
            self.header()

            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}")

            self.footer()
            user_opt = input("Select an option: ")

            if user_opt == "1":
                self.new_weather_st()

            elif user_opt == "0":
                ExitMenu().exit()
                break

            else:
                print("Wrong option...")
                sleep(1)


    def new_weather_st(self):
        """ Handles the process of adding a new weather station """

        # Limpiamos JSON para nueva búsqueda:
        JsonBuilder.clear_json()

        while True:
            Utils.clear_terminal()
            self.header()
            JsonBuilder.get_cities()

            self.separator()
            name = input("Enter the weather station name for the temperature simulation: \n").strip().title()

            # Comprobamos si name existe
            if JsonBuilder.check_city(name):
                print(f"The station '{name}' already exists. Choose another name.")
                sleep(1)
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
                while True:
                    Utils.clear_terminal()
                    self.header()
                    JsonBuilder.get_cities()

                    # Se quiere agregar mas ?
                    self.separator()
                    new_input = input("Do you want to add another city? (y/n): ").strip().lower()

                    if new_input in ["y", "yes"]:
                        break

                    elif new_input in ["n", "no"]:
                        TempMenu().temp_Opt()
                        return

                    else:
                        print("Wrong option...")
                        sleep(1)
                        continue

            else:
                Utils.clear_terminal()
                self.header()
                JsonBuilder.get_cities()
                self.separator()
                print("Wrong station name...")
                sleep(1)


class TempMenu(BaseMenu):
    """ Menu for starting temperature analysis """

    def temp_Opt(self):
        """ Displays the temperature analysis menu and handles user selection """
        Utils.clear_terminal()
        self.header()
        opts = ["Start Temperature Analysis"]

        while True:
            Utils.clear_terminal()
            self.header()

            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}")

            self.footer()
            user_opt = input("Select an option: ")

            if user_opt == "1":
                SelectionTempMenu().selection_temp()

            elif user_opt == "0":
                ExitMenu().exit()
                break

            else:
                print("Wrong option...")
                sleep(1)
                continue


class SelectionTempMenu(BaseMenu):
    """ Menu for selecting the type of temperature simulation """

    def selection_temp(self):
        """ Displays temperature simulation options and handles user selection """
        Utils.clear_terminal()
        self.header()

        opts = [
            "Minimum Temperature Simulation",
            "Average Temperature Simulation",
            "Maximum Temperature Simulation",
            "All Temperatures Simulation"
        ]

        while True:
            Utils.clear_terminal()
            self.header()
            print("This temperature simulation is performed over 30 days\n")

            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}")

            self.footer()
            user_opt = input("Select an option: ")

            if user_opt == "1":
                self.graph.plot_min_temp()

            elif user_opt == "2":
                self.graph.plot_med_temp()

            elif user_opt == "3":
                self.graph.plot_max_temp()

            elif user_opt == "4":
                self.graph.plot_temp()

            elif user_opt == "0":
                ExitMenu().exit()
                break

            else:
                print("Wrong option...")
                sleep(1)
                continue


if __name__ == "__main__":
    menu = LandingMenu()
    menu.main_menu()
