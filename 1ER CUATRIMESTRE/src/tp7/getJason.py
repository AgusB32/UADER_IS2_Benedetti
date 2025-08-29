# Este script recupera un valor desde un archivo JSON según la clave proporcionada como argumento.
# Por defecto, recupera el valor asociado a "token1".

import json
from json_reader_base import AbstractJSONReader

class LegacyJSONReader(AbstractJSONReader):
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = {}

    def get_value(self, key):
        return self.data.get(key, f"Clave '{key}' no encontrada (legacy).")
