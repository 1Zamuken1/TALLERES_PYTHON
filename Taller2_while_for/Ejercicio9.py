import random

def ejercicio_torneo_futbol():
    """
    Simula la organización de un torneo de fútbol con enfrentamientos aleatorios.
    """
    print("---------------------------------------")
    print("| SYSTEM FOOTBALL ASSOCIATION (SFA)   |")
    print("---------------------------------------")
    
    # Solicitar cantidad de equipos con validación
    while True:
        try:
            cantidad_equipos = int(input("\nCuantos equipos participaran en el torneo?: "))
            if cantidad_equipos < 2:
                print("Debe haber al menos 2 equipos para hacer un torneo. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Solicitar categoría
    print("\nCategorias disponibles:")
    print("1. Infantil (Sub-12)")
    print("2. Juvenil (Sub-17)")
    print("3. Profesional")
    print("4. Veteranos")
    
    while True:
        try:
            opcion_categoria = int(input("\nSelecciona la categoria (1-4): "))
            if opcion_categoria == 1:
                categoria = "Infantil (Sub-12)"
            elif opcion_categoria == 2:
                categoria = "Juvenil (Sub-17)"
            elif opcion_categoria == 3:
                categoria = "Profesional"
            elif opcion_categoria == 4:
                categoria = "Veteranos"
            else:
                print("Opcion invalida. Selecciona entre 1 y 4.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Ingresar nombres de equipos
    equipos = []
    print(f"\nIngresa los nombres de los {cantidad_equipos} equipos:")
    for i in range(cantidad_equipos):
        while True:
            nombre_equipo = input(f"Equipo {i + 1}: ").strip()
            if len(nombre_equipo) == 0:
                print("El nombre no puede estar vacio. Intenta de nuevo.")
                continue
            if nombre_equipo in equipos:
                print("Este equipo ya fue ingresado. Intenta con otro nombre.")
                continue
            equipos.append(nombre_equipo)
            break
    
    # Mostrar información del torneo
    print(f"\nTORNEO DE FUTBOL - CATEGORIA: {categoria}")
    print(f"Equipos participantes: {cantidad_equipos}")
    print()
    for i, equipo in enumerate(equipos, 1):
        print(f"  {i}. {equipo}")
    
    # Generar enfrentamientos aleatorios
    print(f"\nFIXTURE DE ENFRENTAMIENTOS")
    
    # Mezclar equipos aleatoriamente
    equipos_mezclados = equipos.copy()
    random.shuffle(equipos_mezclados)
    
    # Generar enfrentamientos
    partidos = []
    i = 0
    while i < len(equipos_mezclados) - 1:
        equipo1 = equipos_mezclados[i]
        equipo2 = equipos_mezclados[i + 1]
        partidos.append((equipo1, equipo2))
        i += 2
    
    # Mostrar partidos
    for i, (equipo1, equipo2) in enumerate(partidos, 1):
        print(f"\nPartido {i}:")
        print(f"  {equipo1} VS {equipo2}")
    
    # Si hay un equipo impar
    if len(equipos_mezclados) % 2 != 0:
        equipo_libre = equipos_mezclados[-1]
        print(f"\nEl equipo '{equipo_libre}' tiene fecha libre (BYE).")
    
    print(f"\nTotal de partidos programados: {len(partidos)}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_torneo_futbol()
