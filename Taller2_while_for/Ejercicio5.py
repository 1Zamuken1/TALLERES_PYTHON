def ejercicio_contar_palabras():
    """
    Cuenta cuántas palabras hay en una frase ingresada por el usuario.
    """
    print("---------------------------------------")
    print("|      CONTADOR DE PALABRAS           |")
    print("---------------------------------------")
    
    # Solicitar frase con validación
    while True:
        frase = input("\nIngresa una frase: ").strip()
        if len(frase) == 0:
            print("La frase no puede estar vacia. Intenta de nuevo.")
            continue
        break
    
    # Contar palabras
    palabras = frase.split()
    cantidad_palabras = len(palabras)
    
    # Mostrar resultado
    print(f"\nFrase ingresada: '{frase}'")
    print(f"La frase tiene {cantidad_palabras} palabra(s).")
    
    # Mostrar las palabras individualmente
    print(f"\nPalabras encontradas:")
    for i, palabra in enumerate(palabras, 1):
        print(f"  {i}. {palabra}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_contar_palabras()
