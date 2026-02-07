def ejercicio_numeros_impares():
    """
    Muestra todos los números impares del 1 al 100.
    """
    print("---------------------------------------")
    print("|     NUMEROS IMPARES 1 AL 100        |")
    print("---------------------------------------")
    
    print("\nNumeros impares del 1 al 100:")
    
    contador = 0
    # Recorrer números del 1 al 100
    for numero in range(1, 101):
        if numero % 2 != 0:
            print(f"{numero:3}", end=" ")
            contador += 1
            # Salto de línea cada 10 números para mejor visualización
            if contador % 10 == 0:
                print()
    
    print(f"\n\nTotal de numeros impares: {contador}")
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_numeros_impares()
