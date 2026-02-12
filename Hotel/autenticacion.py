"""
Modulo de Autenticacion
Maneja el sistema de login y los menus de usuario y administrador.

Principio SOLID aplicado:
- Single Responsibility: Solo maneja autenticacion y navegacion de menus
- Interface Segregation: Menus separados para usuarios y administradores
"""

from .reservas import buscar_reserva_por_id, cancelar_reserva
from .reportes import mostrar_ticket, generar_informe_general, generar_informe_detallado, generar_resumen_estadistico
from .validaciones import validar_si_no


# Credenciales hardcodeadas del administrador
ADMIN_USER = "admin"
ADMIN_PASSWORD = "123456789"


def sistema_login():
    """
    Sistema de login unificado para usuarios y administradores.
    
    Permite el acceso tanto a clientes (usando su numero de identificacion)
    como a administradores (usando credenciales fijas).
    
    Para clientes:
    - Usuario: Numero de identificacion
    - Contrasena: Mismo numero de identificacion
    
    Para administrador:
    - Usuario: admin
    - Contrasena: 123456789
    
    Aplica el principio de Interface Segregation al dirigir a usuarios
    diferentes hacia interfaces especificas (menu_usuario o menu_admin).
    
    Returns:
        None
    
    Example:
        >>> sistema_login()
        Usuario / ID: admin
        Contrasena: 123456789
        [Accede al menu de administrador]
        
        >>> sistema_login()
        Usuario / ID: 1234567890
        Contrasena: 1234567890
        [Accede al menu de usuario]
    """
    print("╔════════════════════════════════════╗")
    print("║            SISTEMA DE LOGIN        ║")
    print("╚════════════════════════════════════╝")
    
    usuario = input("Usuario / ID: ").strip()
    contrasena = input("Contrasena: ").strip()
    
    # Verificar si es administrador
    if usuario == ADMIN_USER and contrasena == ADMIN_PASSWORD:
        print("\nAcceso concedido como ADMINISTRADOR")
        menu_admin()
        return
    
    # Verificar si es un cliente con reserva
    reserva_usuario = buscar_reserva_por_id(usuario)
    
    if reserva_usuario and contrasena == usuario:
        print(f"\nBienvenido, {reserva_usuario['nombre_completo'].title()}")
        menu_usuario(reserva_usuario)
    else:
        print("\nCredenciales incorrectas o usuario sin reserva.")
        print("Verifique sus datos o realice una reserva primero.")
    
    input("\nPresiona Enter para continuar...")


def menu_usuario(reserva):
    """
    Menu interactivo para clientes con reserva.
    
    Permite al cliente:
    1. Ver su ticket de reserva
    2. Ver informe detallado con desglose de costos
    3. Cancelar su reserva
    4. Salir
    
    El menu se mantiene activo hasta que el usuario elija salir o
    cancele su reserva.
    
    Args:
        reserva (dict): Diccionario con los datos de la reserva del usuario
    
    Returns:
        None
    
    Example:
        >>> menu_usuario(reserva_data)
        =======================================
        MENU DE USUARIO
        =======================================
        1. Ver mi ticket
        2. Ver informe detallado
        3. Cancelar reserva
        4. Salir
        Seleccione una opcion: 1
    """
    while True:
        print("╔════════════════════════════════════╗")
        print("║             MENU DE USUARIO        ║")
        print("╚════════════════════════════════════╝")
        print(f"Cliente: {reserva['nombre_completo'].title()}")
        print(f"Codigo: {reserva['codigo']}")
        print("---------------------------------------")
        print("1. Ver mi ticket")
        print("2. Ver informe detallado")
        print("3. Cancelar reserva")
        print("4. Salir")
        print("=======================================")
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            mostrar_ticket(reserva)
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "2":
            generar_informe_detallado(reserva)
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "3":
            print("\nADVERTENCIA: Esta accion es irreversible")
            if validar_si_no("Esta seguro que desea cancelar su reserva? (si/no): "):
                if cancelar_reserva(reserva):
                    print("\nSu reserva ha sido cancelada.")
                    print("Esperamos verle pronto.")
                    input("\nPresiona Enter para continuar...")
                    break
            else:
                print("Cancelacion abortada.")
                
        elif opcion == "4":
            print("\nGracias por usar nuestro sistema.")
            break
            
        else:
            print("Opcion no valida. Intente de nuevo.")


def menu_admin():
    """
    Menu interactivo para administradores del hotel.
    
    Proporciona herramientas de gestion y visualizacion:
    1. Informe general de todas las reservas
    2. Buscar reserva especifica por codigo
    3. Estadisticas del hotel
    4. Salir
    
    Este menu da acceso a funcionalidades privilegiadas que solo
    deben estar disponibles para personal autorizado del hotel.
    
    Returns:
        None
    
    Example:
        >>> menu_admin()
        =======================================
        MENU DE ADMINISTRADOR
        =======================================
        1. Informe general de reservas
        2. Buscar reserva por codigo
        3. Estadisticas del hotel
        4. Salir
        Seleccione una opcion: 1
    """
    while True:
        print("╔════════════════════════════════════╗")
        print("║          MENU DE ADMINISTRADOR     ║")
        print("╚════════════════════════════════════╝")
        print("1. Informe general de reservas")
        print("2. Buscar reserva por codigo")
        print("3. Estadisticas del hotel")
        print("4. Salir")
        print("=======================================")
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            generar_informe_general()
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "2":
            from .reservas import buscar_reserva_por_codigo
            codigo = input("\nIngrese el codigo de reserva: ").strip()
            reserva = buscar_reserva_por_codigo(codigo)
            
            if reserva:
                generar_informe_detallado(reserva)
            else:
                print("No se encontro ninguna reserva con ese codigo.")
            
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "3":
            generar_resumen_estadistico()
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "4":
            print("\nCerrando sesion de administrador...")
            break
            
        else:
            print("Opcion no valida. Intente de nuevo.")
