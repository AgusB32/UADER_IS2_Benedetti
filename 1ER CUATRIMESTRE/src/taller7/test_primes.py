import unittest
from new_primes_v4 import ClassPrimes

class TestClassPrimes(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada prueba individual."""
        self.primes = ClassPrimes()
    
    def test_primos_basicos(self):
        """Verifica que se identifiquen correctamente algunos números primos conocidos."""
        self.assertTrue(self.primes.compute(2))
        self.assertTrue(self.primes.compute(3))
        self.assertTrue(self.primes.compute(5))
        self.assertTrue(self.primes.compute(7))
        self.assertTrue(self.primes.compute(13))
    
    def test_no_primos_basicos(self):
        """Verifica que se rechacen números compuestos o inválidos como primos."""
        self.assertFalse(self.primes.compute(1))
        self.assertFalse(self.primes.compute(0))
        self.assertFalse(self.primes.compute(-3))
        self.assertFalse(self.primes.compute(4))
        self.assertFalse(self.primes.compute(9))
        self.assertFalse(self.primes.compute(100))
    
    def test_primo_grande(self):
        """Verifica un número primo grande."""
        self.assertTrue(self.primes.compute(7919))  # Primo confirmado

    def test_compuesto_grande(self):
        """Verifica un número compuesto grande."""
        self.assertFalse(self.primes.compute(8000))  # Compuesto

if __name__ == '__main__':
    unittest.main()
