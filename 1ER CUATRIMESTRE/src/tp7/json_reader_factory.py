from getJason import LegacyJSONReader
from getJasonOO import SingletonJSONReader

class JSONReaderFactory:
    @staticmethod
    def get_reader(filepath, mode="singleton"):
        if mode == "legacy":
            return LegacyJSONReader(filepath)
        return SingletonJSONReader(filepath)
