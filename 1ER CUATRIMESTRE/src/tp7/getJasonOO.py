import json
from json_reader_base import AbstractJSONReader

class SingletonJSONReader(AbstractJSONReader):
    _instance = None

    def __new__(cls, filepath):
        if cls._instance is None:
            cls._instance = super(SingletonJSONReader, cls).__new__(cls)
            cls._instance._init(filepath)
        return cls._instance

    def _init(self, filepath):
        self.filepath = filepath
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = {}

    def get_value(self, key):
        return self.data.get(key, f"Clave '{key}' no encontrada (singleton).")
