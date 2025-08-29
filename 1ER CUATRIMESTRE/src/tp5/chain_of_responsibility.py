class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        handled = self._handle(number)
        if not handled and self.successor:
            self.successor.handle(number)
        elif not handled:
            print(f"{number} no consumido.")

    def _handle(self, number):
        raise NotImplementedError


class ParHandler(Handler):
    def _handle(self, number):
        if number % 2 == 0:
            print(f"{number} consumido por ParHandler.")
            return True
        return False


class PrimoHandler(Handler):
    def _handle(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        print(f"{number} consumido por PrimoHandler.")
        return True


# Crear cadena
handler = ParHandler(PrimoHandler())

for num in range(1, 101):
    handler.handle(num)
