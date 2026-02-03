def dividir_cuenta():
    """
    Tres campistas van a almorzar. Divide la cuenta entre ellos.
    """
    print("---------------------------------------")
    print("|       División de cuenta            |")
    print("---------------------------------------")
    
    # Solicitar total del almuerzo con validación
    while True:
        try:
            total_almuerzo = float(input("Ingresa el total del almuerzo: $"))
            if total_almuerzo <= 0:
                print("El total debe ser mayor a cero. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    numero_campistas = 3
    pago_por_persona = total_almuerzo / numero_campistas
    
    print(f"\nTotal de la cuenta: ${total_almuerzo:.2f}")
    print(f"Número de campistas: {numero_campistas}")
    print(f"Cada campista debe pagar: ${pago_por_persona:.2f}")
    input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    dividir_cuenta()
    