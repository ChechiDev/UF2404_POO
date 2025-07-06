import re

class Validation:

    @staticmethod
    def is_valid_name(name):
        """ Validates that name contains only letters and spaces, and is not empty """
        return name.strip() and re.match(r"^[a-zA-Z\s]+$", name.strip())