"""
Modulo de Habitaciones
Gestiona el inventario de habitaciones del hotel y su disponibilidad.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja la logica de habitaciones
- Open/Closed: Facil agregar nuevos tipos de habitaciones
"""

# Inventario de habitaciones del hotel
# Organizadas por tipo con rangos de numeros
HABITACIONES_HOTEL = {
    "sencilla": list(range(101, 131)),  # 30 habitaciones (101-130)
    "doble": list(range(201, 221)),     # 20 habitaciones (201-220)
    "suite": list(range(301, 306))      # 5 habitaciones (301-305)
}

# Set para almacenar habitaciones actualmente ocupadas
# Usamos set por su eficiencia en busqueda O(1)
habitaciones_ocupadas = set()


def obtener_habitacion_disponible(tipo):
    """
    Busca y asigna una habitacion disponible del tipo solicitado.
    
    Recorre la lista de habitaciones del tipo especificado y retorna
    la primera que no este ocupada. Si la encuentra, la marca como
    ocupada para evitar asignaciones duplicadas.
    
    Esta funcion es crucial para el sistema de reservas ya que garantiza
    que dos huespedes no reciban la misma habitacion.
    
    Args:
        tipo (str): Tipo de habitacion ('sencilla', 'doble', 'suite')
    
    Returns:
        int: Numero de habitacion asignada
        None: Si no hay habitaciones disponibles de ese tipo
    
    Example:
        >>> habitacion = obtener_habitacion_disponible("doble")
        >>> print(habitacion)
        201
        
        >>> habitacion = obtener_habitacion_disponible("suite")
        >>> habitacion = obtener_habitacion_disponible("suite")
        >>> # Despues de asignar todas las suites
        >>> habitacion = obtener_habitacion_disponible("suite")
        >>> print(habitacion)
        None
    """
    tipo_lower = tipo.lower()
    
    if tipo_lower not in HABITACIONES_HOTEL:
        return None
    
    for num_habitacion in HABITACIONES_HOTEL[tipo_lower]:
        if num_habitacion not in habitaciones_ocupadas:
            habitaciones_ocupadas.add(num_habitacion)
            return num_habitacion
    
    return None


def liberar_habitacion(num_habitacion):
    """
    Libera una habitacion cuando se cancela una reserva.
    
    Remueve el numero de habitacion del set de habitaciones ocupadas,
    permitiendo que pueda ser asignada a un nuevo huesped.
    
    Usa discard en lugar de remove para evitar errores si la habitacion
    no estaba en el set (discard no lanza excepcion).
    
    Args:
        num_habitacion (int): Numero de habitacion a liberar
    
    Returns:
        None
    
    Example:
        >>> liberar_habitacion(201)
        >>> # La habitacion 201 ahora esta disponible nuevamente
    """
    habitaciones_ocupadas.discard(num_habitacion)


def contar_disponibles(tipo):
    """
    Cuenta cuantas habitaciones estan disponibles de un tipo especifico.
    
    Args:
        tipo (str): Tipo de habitacion ('sencilla', 'doble', 'suite')
    
    Returns:
        int: Numero de habitaciones disponibles de ese tipo
    
    Example:
        >>> disponibles = contar_disponibles("doble")
        >>> print(disponibles)
        20
    """
    tipo_lower = tipo.lower()
    
    if tipo_lower not in HABITACIONES_HOTEL:
        return 0
    
    total = len(HABITACIONES_HOTEL[tipo_lower])
    ocupadas = sum(1 for h in HABITACIONES_HOTEL[tipo_lower] if h in habitaciones_ocupadas)
    
    return total - ocupadas


def mostrar_disponibilidad():
    """
    Muestra un resumen de la disponibilidad de habitaciones por tipo.
    
    Imprime en consola cuantas habitaciones hay disponibles de cada tipo,
    util para que el usuario conozca las opciones antes de reservar.
    
    Returns:
        None
    
    Example:
        >>> mostrar_disponibilidad()
        Disponibilidad de habitaciones:
        - Sencilla: 30/30 disponibles
        - Doble: 18/20 disponibles
        - Suite: 5/5 disponibles
    """
    print("\nDisponibilidad de habitaciones:")
    
    for tipo in HABITACIONES_HOTEL.keys():
        total = len(HABITACIONES_HOTEL[tipo])
        disponibles = contar_disponibles(tipo)
        print(f"- {tipo.capitalize()}: {disponibles}/{total} disponibles")


def hay_habitaciones_disponibles(tipo):
    """
    Verifica si existen habitaciones disponibles de un tipo.
    
    Funcion auxiliar que retorna un booleano indicando si es posible
    realizar una reserva del tipo especificado.
    
    Args:
        tipo (str): Tipo de habitacion a verificar
    
    Returns:
        bool: True si hay al menos una habitacion disponible, False si no
    
    Example:
        >>> if hay_habitaciones_disponibles("suite"):
        ...     print("Podemos reservar una suite")
        ... else:
        ...     print("No hay suites disponibles")
    """
    return contar_disponibles(tipo) > 0
