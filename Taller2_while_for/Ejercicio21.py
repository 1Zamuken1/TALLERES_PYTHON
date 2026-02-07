def ejercicio_goles_jugadores():
    """
    Registra los goles de 11 jugadores en 5 partidos y calcula estadísticas.
    """
    print("---------------------------------------")
    print("|    ESTADISTICAS EQUIPO DE FUTBOL    |")
    print("---------------------------------------")
    
    print("\nRegistro de goles - Temporada 2007")
    print("5 partidos oficiales - 11 jugadores")
    
    # Almacenar datos de jugadores
    jugadores = []
    
    # Ingresar datos para cada jugador
    for i in range(11):
        print(f"\n--- JUGADOR {i + 1} ---")
        
        while True:
            nombre = input("Nombre del jugador: ").strip()
            if len(nombre) == 0:
                print("El nombre no puede estar vacio. Intenta de nuevo.")
                continue
            break
        
        goles_partidos = []
        total_goles = 0
        
        # Registrar goles por partido
        for partido in range(1, 6):
            while True:
                try:
                    goles = int(input(f"  Goles en partido {partido}: "))
                    if goles < 0:
                        print("  Los goles no pueden ser negativos. Intenta de nuevo.")
                        continue
                    goles_partidos.append(goles)
                    total_goles += goles
                    break
                except ValueError:
                    print("  Por favor ingresa un numero valido.")
        
        jugadores.append({
            'nombre': nombre,
            'goles_partidos': goles_partidos,
            'total': total_goles
        })
    
    # Mostrar estadísticas
    print("\n" + "="*60)
    print("ESTADISTICAS FINALES")
    print("="*60)
    
    print("\nRESUMEN POR JUGADOR:")
    total_equipo = 0
    
    for i, jugador in enumerate(jugadores, 1):
        print(f"\n{i}. {jugador['nombre']}")
        print(f"   Goles por partido: {jugador['goles_partidos']}")
        print(f"   Total de goles: {jugador['total']}")
        total_equipo += jugador['total']
    
    # Estadísticas del equipo
    print("\n" + "="*60)
    print("ESTADISTICAS DEL EQUIPO:")
    print(f"Total de goles del equipo: {total_equipo}")
    print(f"Promedio de goles por jugador: {total_equipo / 11:.2f}")
    print(f"Promedio de goles por partido: {total_equipo / 5:.2f}")
    
    # Encontrar máximo goleador
    max_goleador = max(jugadores, key=lambda x: x['total'])
    print(f"\nMaximo goleador: {max_goleador['nombre']} con {max_goleador['total']} goles")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_goles_jugadores()
