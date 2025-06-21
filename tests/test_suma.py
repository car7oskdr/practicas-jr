"""
Unit tests for the suma module.
"""

import unittest

from src.operaciones.suma import suma


class TestSuma(unittest.TestCase):
    """Test cases for the suma function."""

    def test_suma_positivos(self):
        """Test suma with positive numbers."""
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(10, 20), 30)
        self.assertEqual(suma(0, 5), 5)

    def test_suma_negativos(self):
        """Test suma with negative numbers."""
        self.assertEqual(suma(-5, -3), -8)
        self.assertEqual(suma(-10, 5), -5)
        self.assertEqual(suma(5, -3), 2)

    def test_suma_cero(self):
        """Test suma with zero."""
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(10, 0), 10)
        self.assertEqual(suma(0, 10), 10)

    def test_suma_numeros_grandes(self):
        """Test suma with large numbers."""
        self.assertEqual(suma(1000000, 2000000), 3000000)
        self.assertEqual(suma(999999, 1), 1000000)

    def test_suma_tipos_datos(self):
        """Test suma with different data types."""
        # La función espera int, pero Python puede convertir automáticamente
        self.assertEqual(suma(5, 3.0), 8)  # float se convierte a int
        self.assertEqual(suma(True, 5), 6)  # True se convierte a 1

    def test_suma_docstring(self):
        """Test that the suma function has proper documentation."""
        self.assertIsNotNone(suma.__doc__)
        self.assertIn("suma", suma.__doc__.lower())


if __name__ == "__main__":
    unittest.main()
