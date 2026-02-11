"""
Modulo de Validaciones
Contiene funciones para validar entrada de usuario y garantizar datos correctos.

Principio SOLID aplicado:
- Single Responsibility: Cada funcion valida un tipo especifico de dato
- Open/Closed: Facilmente extensible para nuevos tipos de validacion
"""

from datetime import datetime


def validar_entero(mensaje):
    """
    Solicita un numero entero al usuario y valida que sea numerico y positivo.
    Evita que el programa se cierre por errores de ValueError.
    
    Esta funcion implementa un ciclo infinito que solo se rompe cuando
    el usuario ingresa un valor valido. Maneja excepciones de conversion
    y valida que el numero no sea negativo.
    
    Args:
        mensaje (str): El texto que se le muestra al usuario como prompt
    
    Returns:
        int: El numero entero validado y positivo
    
    Example:
        >>> edad = validar_entero("Ingresa tu edad: ")
        Ingresa tu edad: -5
        Error: El numero no puede ser negativo
        Ingresa tu edad: veinte
        Error: Entrada invalida. Por favor ingresa un valor entero
        Ingresa tu edad: 25
        >>> print(edad)
        25
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El numero no puede ser negativo")
                continue
            return valor
        except ValueError:
            print("Error: Entrada invalida. Por favor ingresa un valor entero")


def validar_si_no(mensaje):
    """
    Valida que el usuario ingrese 'si' o 'no' (case-insensitive).
    
    Convierte la respuesta a minusculas y elimina espacios en blanco
    para hacer la validacion mas flexible. Solo acepta 'si' o 'no'
    como respuestas validas.
    
    Args:
        mensaje (str): Pregunta a mostrar al usuario
    
    Returns:
        bool: True si la respuesta es 'si', False si es 'no'
    
    Example:
        >>> desea_desayuno = validar_si_no("Desea desayuno? (si/no): ")
        Desea desayuno? (si/no): SI
        >>> print(desea_desayuno)
        True
    """
    while True:
        respuesta = input(mensaje).lower().strip()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        print("Error: Por favor responda 'si' o 'no'.")


def validar_fecha(mensaje):
    """
    Valida que el usuario ingrese una fecha en formato DD/MM/AAAA.
    
    Intenta convertir el string ingresado a un objeto datetime.
    Si la conversion falla, solicita nuevamente la fecha.
    
    Args:
        mensaje (str): Texto a mostrar solicitando la fecha
    
    Returns:
        str: Fecha en formato DD/MM/AAAA validada
    
    Example:
        >>> fecha = validar_fecha("Ingrese fecha (DD/MM/AAAA): ")
        Ingrese fecha (DD/MM/AAAA): 32/13/2024
        Error: Fecha invalida. Use formato DD/MM/AAAA
        Ingrese fecha (DD/MM/AAAA): 15/03/2024
        >>> print(fecha)
        15/03/2024
    """
    formato = "%d/%m/%Y"
    while True:
        fecha_str = input(mensaje).strip()
        try:
            datetime.strptime(fecha_str, formato)
            return fecha_str
        except ValueError:
            print("Error: Fecha invalida. Use formato DD/MM/AAAA")


def validar_tipo_habitacion():
    """
    Valida que el usuario seleccione un tipo de habitacion valido.
    
    Muestra las opciones disponibles con sus precios y solo acepta
    'sencilla', 'doble' o 'suite' como valores validos (case-insensitive).
    
    Returns:
        str: Tipo de habitacion en minusculas ('sencilla', 'doble', 'suite')
    
    Example:
        >>> tipo = validar_tipo_habitacion()
        Opciones de habitacion:
        1. Sencilla - $80,000
        2. Doble - $150,000
        3. Suite - $250,000
        Escriba el tipo: Suite
        >>> print(tipo)
        suite
    """
    print("\nOpciones de habitacion:")
    print("1. Sencilla - $80,000")
    print("2. Doble - $150,000")
    print("3. Suite - $250,000")
    
    while True:
        tipo_input = input("Escriba el tipo: ").lower().strip()
        if tipo_input in ["sencilla", "doble", "suite"]:
            return tipo_input
        print("Error: Tipo de habitacion no reconocido. Intente de nuevo")


def validar_texto_no_vacio(mensaje):
    """
    Valida que el usuario ingrese texto no vacio.
    
    Elimina espacios en blanco al inicio y final, y verifica
    que el resultado no sea un string vacio.
    
    Args:
        mensaje (str): Texto a mostrar al usuario
    
    Returns:
        str: Texto validado (no vacio)
    
    Example:
        >>> nombre = validar_texto_no_vacio("Ingrese su nombre: ")
        Ingrese su nombre:    
        Error: Este campo no puede estar vacio
        Ingrese su nombre: Juan
        >>> print(nombre)
        Juan
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: Este campo no puede estar vacio")
