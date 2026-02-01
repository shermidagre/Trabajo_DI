# -*- coding: utf-8 -*-

"""
Módulo de Calculadora

Este módulo contiene una clase para realizar operaciones aritméticas básicas.
Es un ejemplo para demostrar cómo documentar código con Sphinx.
"""

class Calculadora:
    """
    Esta clase implementa una calculadora simple.
    """

    def sumar(self, a, b):
        """
        Suma dos números y devuelve el resultado.

        :param a: El primer número.
        :type a: int or float
        :param b: El segundo número.
        :type b: int or float
        :return: La suma de a y b.
        :rtype: int or float
        :raises TypeError: si los operandos no son números.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Ambos operandos deben ser números.")
        return a + b

    def restar(self, a, b):
        """
        Resta el segundo número del primero.

        :param a: El número del que se resta.
        :type a: int or float
        :param b: El número a restar.
        :type b: int or float
        :return: La diferencia entre a y b.
        :rtype: int or float
        """
        return a - b

def funcion_ejemplo(arg1, arg2):
    """
    Esta es una función de ejemplo a nivel de módulo.

    No hace nada útil, pero sirve para mostrar cómo documentar funciones
    que no están dentro de una clase.

    :param arg1: Descripción del primer argumento.
    :param arg2: Descripción del segundo argumento.
    """
    pass