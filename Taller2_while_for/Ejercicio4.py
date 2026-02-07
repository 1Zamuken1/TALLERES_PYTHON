def ejercicio_estudiantes_computadores():
    """
    Calcula si sobran o faltan computadores en un aula según la cantidad de estudiantes.
    """
    print("---------------------------------------")
    print("|   ESTUDIANTES Y COMPUTADORES        |")
    print("---------------------------------------")
    
    # Solicitar cantidad de estudiantes con validación
    while True:
        try:
            estudiantes = int(input("\nCuantos estudiantes hay en el aula?: "))
            if estudiantes < 0:
                print("La cantidad de estudiantes no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Solicitar cantidad de computadores con validación
    while True:
        try:
            computadores = int(input("Cuantos computadores hay en el aula?: "))
            if computadores < 0:
                print("La cantidad de computadores no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Calcular y mostrar resultado
    print(f"\nEstudiantes: {estudiantes}")
    print(f"Computadores: {computadores}")
    
    if computadores > estudiantes:
        sobran = computadores - estudiantes
        print(f"\nSOBRAN COMPUTADORES")
        print(f"Computadores sobrantes: {sobran}")
        print(f"Todos los estudiantes tienen computador.")
    elif computadores < estudiantes:
        faltan = estudiantes - computadores
        sin_computador = estudiantes - computadores
        print(f"\nFALTAN COMPUTADORES")
        print(f"Computadores faltantes: {faltan}")
        print(f"Estudiantes sin computador: {sin_computador}")
    else:
        print(f"\nCANTIDAD EXACTA")
        print(f"Hay la cantidad justa de computadores.")
        print(f"Todos los estudiantes tienen computador.")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_estudiantes_computadores()
