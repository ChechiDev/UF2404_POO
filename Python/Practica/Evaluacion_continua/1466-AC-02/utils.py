import os
import re
import platform as plat


class Utils:
    @staticmethod
    def clear_terminal():
        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")

    def valid_column_num() -> int:

        value = input("Enter a column number (0-6): ")
        pattern = r"^[0-6]$"

        while True:
            if re.match(pattern, value):
                return int(value)

            else:
                print("Please enter a valid number.")
                return None
            
    @staticmethod
    def choose_name() -> str:
        """
        Asks the user for their name and returns it.
        """
        name = input("\nPlease, enter your name: ").strip()
        
        return name   
    
    
    def copy_board(board: list) -> list:
        pass