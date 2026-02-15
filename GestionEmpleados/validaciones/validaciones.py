"""
Funcionalidades de validación de datos de entrada.
El objetivo es encapsular verificaciones comunes usadas por los
servicios y menús interactivos.
"""

import re


def validar_texto_no_vacio(prompt):
    while True:
        valor = input(prompt)
        valor = valor.strip()
        if len(valor) > 0:
            return valor
        print("El valor no puede estar vacío.")


def validar_documento(prompt):
    while True:
        valor = input(prompt)
        valor = valor.strip()
        es_digito = valor.isdigit()
        if es_digito == True:
            return valor
        print("Documento inválido. Solo se permiten dígitos.")


def validar_celular(prompt):
    while True:
        valor = input(prompt).strip()
        if valor.isdigit() and len(valor) == 10:
            return valor
        print("Celular inválido. Debe ser un número de 10 dígitos.")


def validar_correo(prompt):
    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    while True:
        valor = input(prompt).strip().lower()
        if re.match(patron, valor):
            return valor
        print("Correo electrónico no válido.")


def confirmar_accion(prompt):
    respuesta = input(prompt).strip().lower()
    return respuesta in ("si", "s")