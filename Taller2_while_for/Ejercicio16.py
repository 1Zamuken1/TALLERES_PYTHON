def ejercicio_elementos_quimicos():
    """
    Identifica elementos químicos por su símbolo.
    """
    print("---------------------------------------")
    print("|       ELEMENTOS QUIMICOS            |")
    print("---------------------------------------")
    
    print("\nElementos disponibles:")
    print("H - Hidrogeno")
    print("O - Oxigeno")
    print("AG - Plata")
    print("CA - Calcio")
    print("C - Carbono")
    print("NA - Sodio")
    print("K - Potasio")
    
    # Solicitar símbolo
    simbolo = input("\nIngresa el simbolo del elemento quimico: ").strip().upper()
    
    # Evaluar símbolo
    print(f"\nSimbolo: {simbolo}")
    
    if simbolo == "H":
        print("Elemento: Hidrogeno")
    elif simbolo == "O":
        print("Elemento: Oxigeno")
    elif simbolo == "AG":
        print("Elemento: Plata")
    elif simbolo == "CA":
        print("Elemento: Calcio")
    elif simbolo == "C":
        print("Elemento: Carbono")
    elif simbolo == "NA":
        print("Elemento: Sodio")
    elif simbolo == "K":
        print("Elemento: Potasio")
    else:
        print("Lo sentimos, no esta disponible")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_elementos_quimicos()
