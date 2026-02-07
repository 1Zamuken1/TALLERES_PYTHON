def ejercicio_cambio_dolares():
    """
    Elabora una tabla de conversión de dólares (1 a 100) a la moneda local.
    """
    print("---------------------------------------")
    print("|      CAMBIO DE DOLARES              |")
    print("---------------------------------------")
    
    # Solicitar tipo de cambio con validación
    while True:
        try:
            tipo_cambio = float(input("\nIngresa el tipo de cambio actual (1 USD = ? en tu moneda): "))
            if tipo_cambio <= 0:
                print("El tipo de cambio debe ser mayor a 0. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    # Solicitar nombre de la moneda
    moneda = input("Nombre de tu moneda (ejemplo: Pesos, Soles, etc.): ").strip()
    
    # Mostrar tabla de conversión
    print(f"\nTABLA DE CONVERSION USD a {moneda}")
    print(f"Tipo de cambio: 1 USD = {tipo_cambio} {moneda}")
    print(f"\nDolares |  {moneda}")
    print("--------|-------------")
    
    for dolares in range(1, 101):
        equivalente = dolares * tipo_cambio
        print(f" {dolares:3} USD | {equivalente:10,.2f}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_cambio_dolares()
