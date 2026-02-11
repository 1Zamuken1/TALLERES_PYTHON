"""
Ejercicio 22 - Sistema de Gestion de Hotel

Punto de entrada para ejecutar el sistema de gestion hotelera
desde el menu principal del Taller 2.

Este archivo actua como wrapper para importar y ejecutar el sistema
completo que esta modularizado en el directorio Ejercicio22_Hotel/.
"""

import sys
import os

# Agregar el directorio del hotel al path para poder importar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Ejercicio22_Hotel'))

from main import sistema_hotel_main


def ejercicio_sistema_hotel():
    """
    Funcion de entrada para el sistema de gestion de hotel.
    
    Esta funcion es llamada desde el menu principal del taller
    y ejecuta el sistema completo de gestion hotelera.
    
    El sistema incluye:
    - Gestion de reservas
    - Asignacion automatica de habitaciones
    - Autenticacion de usuarios y administradores
    - Generacion de informes con tabulate
    
    Returns:
        None
    """
    sistema_hotel_main()


if __name__ == "__main__":
    ejercicio_sistema_hotel()
