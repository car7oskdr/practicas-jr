"""Modulo para realizar la suma de dos numeros."""

import logging

logger = logging.getLogger(__name__)


def suma(num1: int, num2: int) -> int:
    """Realiza la suma de dos numeros.

    Args:
        num1: Primer numero a sumar.
        num2: Segundo numero a sumar.

    Returns:
        Resultado de la suma.
    """
    logger.info("Sumando %s y %s", num1, num2)
    return num1 + num2
