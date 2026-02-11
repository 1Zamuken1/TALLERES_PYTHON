"""
Modulo de Reservas
Maneja las operaciones CRUD (Create, Read, Update, Delete) de reservas.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja operaciones de reservas
- Dependency Inversion: Usa funciones de otros modulos sin conocer su implementacion
"""

from datetime import datetime
from validaciones import (validar_entero, validar_si_no, validar_fecha, 
                         validar_tipo_habitacion, validar_texto_no_vacio)
from calculos import calcular_noches, calcular_total, generar_codigo_ticket
from habitaciones import (obtener_habitacion_disponible, liberar_habitacion,
                         mostrar_disponibilidad, hay_habitaciones_disponibles)


# Base de datos en memoria para almacenar reservas
# Cada reserva es un diccionario con toda la informacion del huesped
reservas_db = []


def crear_reservacion():
    """
    Flujo completo para crear una nueva reservacion.
    
    Esta es la funcion principal del sistema que guia al usuario a traves
    de todo el proceso de reserva. Realiza las siguientes acciones:
    1. Solicita datos personales del huesped
    2. Valida fechas de entrada y salida
    3. Muestra disponibilidad de habitaciones
    4. Asigna una habitacion disponible
    5. Calcula el costo total
    6. Genera codigo de ticket
    7. Almacena la reserva en la base de datos
    
    Aplica el principio Single Responsibility al delegar validaciones,
    calculos y gestion de habitaciones a otros modulos especializados.
    
    Returns:
        None
    
    Example:
        >>> crear_reservacion()
        =======================================
        NUEVA RESERVACION DEL HOTEL
        =======================================
        Nombres: Juan
        ...
        Reserva completada con exito!
        Codigo de Ticket: HTL-890-3456
    """
    print("=======================================")
    print("NUEVA RESERVACION DEL HOTEL")
    print("=======================================")
    
    # Captura de datos personales
    # Se usa .lower() para normalizar los nombres como indica el ejercicio
    nombres = validar_texto_no_vacio("Nombres: ").lower()
    apellidos = validar_texto_no_vacio("Apellidos: ").lower()
    identificacion = validar_texto_no_vacio("Numero de identificacion: ")
    contacto = validar_texto_no_vacio("Numero de contacto: ")
    
    # Validacion de fechas
    print("\nFechas de estadia:")
    while True:
        f_inicio = validar_fecha("Fecha de Llegada (DD/MM/AAAA): ")
        f_fin = validar_fecha("Fecha de Salida (DD/MM/AAAA): ")
        noches = calcular_noches(f_inicio, f_fin)
        
        if noches == -1:
            print("Error: La fecha de salida debe ser posterior a la de entrada")
        elif noches == -2:
            print("Error: Formato invalido")
        else:
            print(f"Estancia confirmada: {noches} noche(s).")
            break
    
    # Mostrar disponibilidad antes de seleccionar
    mostrar_disponibilidad()
    
    # Validacion de tipo de habitacion y verificacion de disponibilidad
    while True:
        tipo_habitacion = validar_tipo_habitacion()
        
        if not hay_habitaciones_disponibles(tipo_habitacion):
            print(f"Lo sentimos, no hay habitaciones tipo {tipo_habitacion} disponibles.")
            print("Por favor seleccione otro tipo.")
            continue
        
        # Asignar habitacion disponible
        num_habitacion = obtener_habitacion_disponible(tipo_habitacion)
        if num_habitacion:
            print(f"Habitacion asignada: {num_habitacion}")
            break
        else:
            print("Error al asignar habitacion. Intente de nuevo.")
    
    # Numero de acompanantes
    num_acompanantes = validar_entero("Numero de acompanantes (sin contarlo a usted): ")
    total_personas = num_acompanantes + 1
    
    # Desayuno
    tiene_desayuno = validar_si_no("\nDesea incluir desayuno?\n($30,000 por persona/noche)\n(si/no): ")
    
    # Calculos finales
    total_pagar = calcular_total(tipo_habitacion, noches, total_personas, tiene_desayuno)
    codigo = generar_codigo_ticket(identificacion)
    fecha_reserva = datetime.now().strftime("%d/%m/%Y")
    
    # Crear diccionario de reserva
    nueva_reserva = {
        "codigo": codigo,
        "fecha_reserva": fecha_reserva,
        "nombres": nombres,
        "apellidos": apellidos,
        "nombre_completo": f"{nombres} {apellidos}",
        "identificacion": identificacion,
        "contacto": contacto,
        "fecha_inicio": f_inicio,
        "fecha_fin": f_fin,
        "noches": noches,
        "tipo_habitacion": tipo_habitacion,
        "num_habitacion": num_habitacion,
        "acompanantes": num_acompanantes,
        "total_personas": total_personas,
        "con_desayuno": tiene_desayuno,
        "total_pagar": total_pagar
    }
    
    # Guardar en base de datos
    reservas_db.append(nueva_reserva)
    
    # Confirmacion
    print("\n=======================================")
    print("RESERVA COMPLETADA CON EXITO!")
    print("=======================================")
    print(f"Codigo de Ticket: {codigo}")
    print(f"Habitacion: {num_habitacion}")
    print(f"Total a pagar: ${total_pagar:,}")
    print("\nPara consultar su reserva ingrese con:")
    print(f"  Usuario: {identificacion}")
    print(f"  Contrasena: {identificacion}")
    
    input("\nPresiona Enter para continuar...")


def buscar_reserva_por_codigo(codigo):
    """
    Busca una reserva por su codigo de ticket.
    
    Args:
        codigo (str): Codigo de ticket a buscar
    
    Returns:
        dict: Diccionario con la reserva encontrada
        None: Si no se encuentra ninguna reserva con ese codigo
    """
    for reserva in reservas_db:
        if reserva["codigo"] == codigo:
            return reserva
    return None


def buscar_reserva_por_id(identificacion):
    """
    Busca una reserva por el numero de identificacion del cliente.
    
    Args:
        identificacion (str): Numero de identificacion a buscar
    
    Returns:
        dict: Diccionario con la reserva encontrada
        None: Si no se encuentra ninguna reserva con esa identificacion
    """
    for reserva in reservas_db:
        if reserva["identificacion"] == identificacion:
            return reserva
    return None


def cancelar_reserva(reserva):
    """
    Cancela una reserva y libera la habitacion.
    
    Elimina la reserva de la base de datos y libera la habitacion
    para que pueda ser asignada a otro huesped.
    
    Args:
        reserva (dict): Diccionario con los datos de la reserva a cancelar
    
    Returns:
        bool: True si se cancelo exitosamente, False en caso contrario
    """
    try:
        # Liberar la habitacion
        liberar_habitacion(reserva["num_habitacion"])
        
        # Eliminar de la base de datos
        reservas_db.remove(reserva)
        
        print("\nReserva cancelada exitosamente.")
        print(f"Habitacion {reserva['num_habitacion']} liberada.")
        return True
    except Exception as e:
        print(f"Error al cancelar reserva: {e}")
        return False


def obtener_todas_reservas():
    """
    Retorna la lista completa de reservas.
    
    Returns:
        list: Lista con todas las reservas almacenadas
    """
    return reservas_db


def contar_reservas():
    """
    Cuenta el numero total de reservas activas.
    
    Returns:
        int: Numero de reservas en el sistema
    """
    return len(reservas_db)
