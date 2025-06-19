import os
import platform as plat


class Utils:
    def clear_terminal():
        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")