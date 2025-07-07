# src.utils.utils.py

import os
import platform as pltf

class Utils:
    """ Recursive functions """

    @staticmethod
    def clear_terminal():
        """ Clears the terminal """

        os.system("cls" if pltf.system() == "Windows" else "clear")
