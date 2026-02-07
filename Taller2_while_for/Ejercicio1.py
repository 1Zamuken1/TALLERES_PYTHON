def ejercicio_suma_pares():
    """
    Suma todos los números pares del 1 al 100.
    """
    print("---------------------------------------")
    print("|      SUMA DE NUMEROS PARES          |")
    print("---------------------------------------")
    
    suma = 0
    print("\nNumeros pares del 1 al 100:")
    
    # Recorrer números del 1 al 100
    for numero in range(1, 101):
        if numero % 2 == 0:
            suma += numero
            print(numero, end=" ")
    
    print(f"\n\nLa suma de todos los numeros pares del 1 al 100 es: {suma}")
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_suma_pares()
