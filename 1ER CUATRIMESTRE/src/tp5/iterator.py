class CadenaIterator:
    def __init__(self, cadena, reverso=False):
        self.cadena = cadena
        self.reverso = reverso
        self.index = len(cadena) - 1 if reverso else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverso:
            if self.index < 0:
                raise StopIteration
            char = self.cadena[self.index]
            self.index -= 1
            return char
        else:
            if self.index >= len(self.cadena):
                raise StopIteration
            char = self.cadena[self.index]
            self.index += 1
            return char

cadena = "Hola mundo"
for c in CadenaIterator(cadena):
    print(c, end=' ')
print()
for c in CadenaIterator(cadena, reverso=True):
    print(c, end=' ')
