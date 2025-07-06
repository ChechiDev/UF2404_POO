import os
import json

FILENAME = "station_data.json"

class JsonBuilder:
    def __init__(self):
        pass

    @staticmethod
    def create_data_folder():

        # Obtenemos la ruta abs del folder src:
        # Bajamos 2 niveles de carpeta de .utils/src/ desde donde está este archivo
        src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(src_dir, "data")

        # Preguntamos si existe:
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        return data_dir

    @staticmethod
    def read_json():

        data_dir = JsonBuilder.create_data_folder()
        file_path = os.path.join(data_dir, FILENAME)

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r", encoding="UTF-8") as f:
            return json.load(f)

    @staticmethod
    def write_json(new_data):
        data_dir = JsonBuilder.create_data_folder()
        file_path = os.path.join(data_dir, FILENAME)

        # si existe, leemos JSON
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="UTF-8") as f:
                try:
                    data = json.load(f)
                except Exception:
                    data = {}
        else:
            data = {}

        # Actualizar el dict con los nuevos datos
        data.update(new_data)

        # Guardamos el dict actualizado
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def clear_json():
        data_dir = JsonBuilder.create_data_folder()
        file_path = os.path.join(data_dir, FILENAME)

        # Limpiamos el JSON:
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)

    @staticmethod
    def check_city(city_name):
        data_dir = JsonBuilder.create_data_folder()
        file_path = os.path.join(data_dir, FILENAME)

        with open(file_path, "r", encoding="UTF-8") as f:
            data = json.load(f)
            return city_name in data

    @staticmethod
    def get_cities():
        data_dir = JsonBuilder.create_data_folder()
        file_path = os.path.join(data_dir, FILENAME)

        with open(file_path, "r", encoding="UTF-8") as f:
            data = json.load(f)

            if not data:
                print("No cities found...")
                return

            for idx, k in enumerate(data):
                print(f"{idx + 1}. {k}")