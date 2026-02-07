def ejercicio_invertir_palabra():
    """
    Muestra las letras de una palabra introducida empezando por la última.
    """
    print("---------------------------------------")
    print("|        INVERTIR PALABRA             |")
    print("---------------------------------------")
    
    # Solicitar palabra con validación
    while True:
        palabra = input("\nIngresa una palabra: ").strip()
        if len(palabra) == 0:
            print("La palabra no puede estar vacia. Intenta de nuevo.")
            continue
        break
    
    # Mostrar letras de la última a la primera
    print(f"\nPalabra original: {palabra}")
    print("Letras invertidas:")
    
    for i in range(len(palabra) - 1, -1, -1):
        print(palabra[i])
    
    # Mostrar palabra invertida completa
    palabra_invertida = palabra[::-1]
    print(f"\nPalabra invertida: {palabra_invertida}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_invertir_palabra()
