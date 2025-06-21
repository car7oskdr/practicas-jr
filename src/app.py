"""
Main application module.
"""

import logging

from .operaciones.suma import suma


class App:
    """Calculadora sencilla para sumas, restas, multiplicacion y division"""

    def __init__(self) -> None:
        """Initialize the application."""

        self.logger = self._setup_logging()

    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration.

        Returns:
            Configured logger instance
        """
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        return logging.getLogger(self.__class__.__name__)

    def run(self) -> None:
        """Interfaz de usuario para la calculadora."""
        while True:
            print("Seleccione la operacion a realizar: ")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicacion")
            print("4. Division")
            print("5. Salir")
            opcion = input("Ingrese la opcion: ")
            if opcion == "1":
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                print(f"El resultado de la suma es: {suma(num1, num2)}")
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                break
            else:
                print("Opcion no valida")
