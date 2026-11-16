"""
Calculadora en consola hecha en Python.

Proyecto académico de Ingeniería en Informática (Duoc UC).
Permite realizar operaciones matemáticas desde un menú interactivo,
con validación de entradas y un historial de operaciones.

Autor: Diego Valenzuela
"""

import math


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None  # No se puede dividir por cero
    return a / b


def potencia(a, b):
    return a ** b


def raiz_cuadrada(a):
    if a < 0:
        return None  # No existe raíz cuadrada real de un negativo
    return math.sqrt(a)


def porcentaje(porc, valor):
    """Calcula cuánto es el 'porc'% de 'valor'."""
    return (porc / 100) * valor
