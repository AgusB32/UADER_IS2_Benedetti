from abc import ABC, abstractmethod

class AbstractJSONReader(ABC):
    @abstractmethod
    def get_value(self, key):
        pass
