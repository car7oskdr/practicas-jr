"""
Unit tests for the main application module.
"""

import unittest
from unittest.mock import patch

from src.app import App


class TestApp(unittest.TestCase):
    """Test cases for the App class."""

    def setUp(self):
        """Set up test fixtures."""
        self.app = App()

    def test_app_initialization(self):
        """Test app initialization."""
        app = App()
        self.assertIsNotNone(app.logger)
        self.assertEqual(app.logger.name, "App")

    def test_setup_logging(self):
        """Test logging setup."""
        logger = self.app._setup_logging()
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "App")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_run_with_suma_option(self, mock_print, mock_input):
        """Test run method with suma option."""
        # Simular entrada del usuario:
        # opción 1 (suma), números 5 y 3, luego salir
        mock_input.side_effect = ["1", "5", "3", "5"]

        self.app.run()

        # Verificar que se llamó a print con el resultado correcto
        mock_print.assert_any_call("El resultado de la suma es: 8")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_run_with_invalid_option(self, mock_print, mock_input):
        """Test run method with invalid option."""
        # Simular entrada inválida, luego salir
        mock_input.side_effect = ["6", "5"]

        self.app.run()

        # Verificar que se mostró el mensaje de opción inválida
        mock_print.assert_any_call("Opcion no valida")


if __name__ == "__main__":
    unittest.main()
