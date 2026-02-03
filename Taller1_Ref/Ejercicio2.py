def promedio_temperaturas():
    """
    Un campista mide la temperatura en la mañana, tarde y noche. Calcula y muestra el promedio.
    """
    print("---------------------------------------")
    print("|        PROMEDIO TEMPERATURAS        |")
    print("---------------------------------------")
    
    # Solicitar temperatura de la mañana
    try:
        temperatura_manana = float(input("Ingresa la temperatura de la mañana °C: "))
    except ValueError:
        print("Por favor ingresa número válido")
        
    # Solicitar temperatura de la tarde
    try:
        temperatura_tarde = float(input("Ingresa la temperatura de la tarde °C: "))
    except ValueError:
        print("Por favor ingresa número válido")
    
    # Solicitar temperatura de la noche
    try:
        temperatura_noche = float(input("Ingresa la temperatura de la noche °C: "))
    except ValueError:
        print("Por favor ingresa número válido")
    
    # Calcular y mostrar resultado
    promedio_total = (temperatura_manana + temperatura_tarde + temperatura_noche) / 3
    print(f"\nEl promedio de la temperatura del día es de: {promedio_total}C°")
    input("Presiona Enter para continuar...")

if __name__ == "__main__":
    promedio_temperaturas()