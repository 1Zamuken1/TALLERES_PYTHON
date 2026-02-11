"""
Modulo de Calculos
Contiene funciones para realizar calculos relacionados con reservas.

Principio SOLID aplicado:
- Single Responsibility: Cada funcion calcula un aspecto especifico
- Dependency Inversion: No depende de implementaciones concretas
"""

import random
from datetime import datetime


def calcular_noches(fecha_inicio_str, fecha_fin_str):
    """
    Calcula la diferencia de dias entre dos fechas.
    
    Esta funcion es crucial para el sistema de reservas ya que determina
    cuantas noches el huesped se quedara en el hotel. La fecha de inicio
    representa la fecha de llegada (check-in) y la fecha fin representa
    la fecha de salida (check-out).
    
    Importante: La fecha de salida debe ser posterior a la de entrada.
    El calculo se hace en dias completos, por lo que si el usuario llega
    el dia 1 y sale el dia 3, son 2 noches (dia 1-2 y dia 2-3).
    
    Args:
        fecha_inicio_str (str): Fecha de inicio en formato DD/MM/AAAA
        fecha_fin_str (str): Fecha de fin en formato DD/MM/AAAA
    
    Returns:
        int: Numero de noches entre las fechas
             -1 si la fecha fin no es posterior a la fecha inicio (fechas illogicas)
             -2 si el formato de alguna fecha es incorrecto
    
    Example:
        >>> noches = calcular_noches("10/02/2026", "13/02/2026")
        >>> print(noches)
        3
        
        >>> noches = calcular_noches("13/02/2026", "10/02/2026")
        >>> print(noches)
        -1
    """
    formato = "%d/%m/%Y"
    try:
        inicio = datetime.strptime(fecha_inicio_str, formato)
        fin = datetime.strptime(fecha_fin_str, formato)
        
        if fin <= inicio:
            return -1
        
        diferencia = fin - inicio
        return diferencia.days
    except ValueError:
        return -2


def calcular_total(tipo_habitacion, noches, numero_personas, tiene_desayuno):
    """
    Calcula el costo total de la reserva.
    
    El costo total se compone de:
    1. Costo de la habitacion: (precio_habitacion * numero_noches)
    2. Costo de desayunos: (precio_desayuno * personas * noches) si aplica
    
    Los precios base son:
    - Sencilla: $80,000 por noche
    - Doble: $150,000 por noche  
    - Suite: $250,000 por noche
    - Desayuno: $30,000 por persona por dia
    
    Args:
        tipo_habitacion (str): Tipo de habitacion ('sencilla', 'doble', 'suite')
        noches (int): Numero de noches de estadia
        numero_personas (int): Numero total de personas (huesped + acompanantes)
        tiene_desayuno (bool): True si desean desayuno incluido
    
    Returns:
        int: Costo total de la reserva en pesos
    
    Example:
        >>> total = calcular_total("doble", 3, 2, True)
        >>> print(total)
        630000
        # Calculo: (150000 * 3) + (30000 * 2 * 3) = 450000 + 180000 = 630000
    """
    precios_habitacion = {
        "sencilla": 80000,
        "doble": 150000,
        "suite": 250000
    }
    precio_desayuno = 30000
    
    costo_habitacion = precios_habitacion.get(tipo_habitacion.lower(), 0) * noches
    
    # Solo suma el costo de desayuno si el usuario lo solicito
    costo_desayuno = 0
    if tiene_desayuno:
        costo_desayuno = precio_desayuno * numero_personas * noches
    
    return costo_habitacion + costo_desayuno


def generar_codigo_ticket(id_cliente):
    """
    Genera un codigo unico para identificar la reserva.
    
    El codigo generado tiene el formato: HTL-XXX-NNNN
    donde:
    - HTL: Prefijo fijo del hotel
    - XXX: Ultimos 3 digitos del ID del cliente
    - NNNN: Numero aleatorio entre 1000 y 9999
    
    Este codigo es unico porque combina informacion del cliente
    con un numero aleatorio, haciendo extremadamente improbable
    que dos reservas tengan el mismo codigo.
    
    Args:
        id_cliente (str): Numero de identificacion del cliente
    
    Returns:
        str: Codigo de ticket en formato HTL-XXX-NNNN
    
    Example:
        >>> codigo = generar_codigo_ticket("1234567890")
        >>> print(codigo)
        HTL-890-3456
        
        >>> codigo = generar_codigo_ticket("123")
        >>> print(codigo)
        HTL-123-7891
    """
    rand_num = random.randint(1000, 9999)
    # Toma los ultimos 3 caracteres del ID, o todo el ID si es mas corto
    fragmento_id = id_cliente[-3:] if len(id_cliente) >= 3 else id_cliente
    return f"HTL-{fragmento_id}-{rand_num}"


def calcular_desglose_costos(tipo_habitacion, noches, numero_personas, tiene_desayuno):
    """
    Calcula el desglose detallado de costos de la reserva.
    
    Similar a calcular_total pero retorna un diccionario con el desglose
    completo de costos, util para mostrar al usuario el detalle de su factura.
    
    Args:
        tipo_habitacion (str): Tipo de habitacion
        noches (int): Numero de noches
        numero_personas (int): Numero de personas
        tiene_desayuno (bool): Si incluye desayuno
    
    Returns:
        dict: Diccionario con el desglose de costos conteniendo:
            - costo_habitacion_noche: Precio por noche de la habitacion
            - costo_habitacion_total: Costo total de habitacion
            - costo_desayuno_persona_dia: Precio de desayuno por persona por dia
            - costo_desayuno_total: Costo total de desayunos
            - costo_total: Suma total
    
    Example:
        >>> desglose = calcular_desglose_costos("doble", 2, 2, True)
        >>> print(desglose)
        {
            'costo_habitacion_noche': 150000,
            'costo_habitacion_total': 300000,
            'costo_desayuno_persona_dia': 30000,
            'costo_desayuno_total': 120000,
            'costo_total': 420000
        }
    """
    precios_habitacion = {
        "sencilla": 80000,
        "doble": 150000,
        "suite": 250000
    }
    precio_desayuno = 30000
    
    costo_hab_noche = precios_habitacion.get(tipo_habitacion.lower(), 0)
    costo_hab_total = costo_hab_noche * noches
    
    costo_des_total = 0
    if tiene_desayuno:
        costo_des_total = precio_desayuno * numero_personas * noches
    
    return {
        "costo_habitacion_noche": costo_hab_noche,
        "costo_habitacion_total": costo_hab_total,
        "costo_desayuno_persona_dia": precio_desayuno,
        "costo_desayuno_total": costo_des_total,
        "costo_total": costo_hab_total + costo_des_total
    }
