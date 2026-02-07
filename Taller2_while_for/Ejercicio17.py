def ejercicio_formatos_pelicula():
    """
    Calcula el costo de una película según su formato.
    """
    print("---------------------------------------")
    print("|      FORMATOS DE PELICULA           |")
    print("---------------------------------------")
    
    print("\nFormatos disponibles:")
    print("BETA - $2.000")
    print("VHS  - $3.000")
    print("VCD  - $4.000")
    print("DVD  - $5.000")
    
    # Solicitar formato
    formato = input("\nIngresa el formato de la pelicula: ").strip().upper()
    
    # Evaluar formato
    print(f"\nFormato seleccionado: {formato}")
    
    if formato == "BETA":
        precio = 2000
        print(f"Precio: ${precio:,}")
    elif formato == "VHS":
        precio = 3000
        print(f"Precio: ${precio:,}")
    elif formato == "VCD":
        precio = 4000
        print(f"Precio: ${precio:,}")
    elif formato == "DVD":
        precio = 5000
        print(f"Precio: ${precio:,}")
    else:
        print("Formato no valido")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_formatos_pelicula()
