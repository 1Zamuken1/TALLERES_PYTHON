def ejercicio_comprar_gaseosa():
    """
    Un campista compra una gaseosa que cuesta $2.500 y paga con un billete de $5.000. Calcula el cambio.
    """
    print("---------------------------------------")
    print("|           COMPRAR GASEOSA           |")
    print("---------------------------------------")
    
    # Solicitar precio
    while True:
        try:
            precio_gaseosa = float(input("Ingresa el precio de la gaseosa: $"))
            if precio_gaseosa < 0:
                print("El precio no puede ser negativo. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un valor válido")
            
    # Solicitar pago
    while True:
        try:
            pago_billete = float(input("Ingresa el valor del billete: "))
            if pago_billete < 0:
                print("El pago no puede ser negativo. Intenta de nuevo")
            elif pago_billete < precio_gaseosa:
                print("El pago no puede ser menor que el producto. Intenta de nuevo")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
            
    # Calcular cambio
    cambio = pago_billete - precio_gaseosa
    print(f"Precio gaseosa: ${precio_gaseosa}\nPago: ${pago_billete}\nCambio: ${cambio}")
    input("Presiona Enter para continuar...")
    
if __name__ == "__main__":
    ejercicio_comprar_gaseosa()
    