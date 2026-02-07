def ejercicio_agencia_modelaje():
    """
    Evalúa si un candidato cumple con los requisitos para ser contratado como modelo.
    """
    print("---------------------------------------")
    print("|      AGENCIA DE MODELAJE            |")
    print("---------------------------------------")
    
    print("\nRequisitos para ser contratado:")
    print("- Ser hombre")
    print("- Edad menor o igual a 20 anos")
    print("- Estatura mayor o igual a 1.75 m")
    print("- Peso menor o igual a 70 kg")
    print("- Ojos color azul")
    
    # Solicitar datos con validación
    genero = input("\nGenero (hombre/mujer): ").strip().lower()
    
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    while True:
        try:
            estatura = float(input("Estatura en metros (ejemplo: 1.75): "))
            if estatura < 0:
                print("La estatura no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    while True:
        try:
            peso = float(input("Peso en kg: "))
            if peso < 0:
                print("El peso no puede ser negativo. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un numero valido.")
    
    color_ojos = input("Color de ojos: ").strip().lower()
    
    # Evaluar requisitos
    print("\nEVALUACION:")
    
    cumple_genero = genero == "hombre"
    cumple_edad = edad <= 20
    cumple_estatura = estatura >= 1.75
    cumple_peso = peso <= 70
    cumple_ojos = color_ojos == "azul"
    
    print(f"Es hombre: {'SI' if cumple_genero else 'NO'}")
    print(f"Edad <= 20: {'SI' if cumple_edad else 'NO'} (Edad: {edad})")
    print(f"Estatura >= 1.75: {'SI' if cumple_estatura else 'NO'} (Estatura: {estatura})")
    print(f"Peso <= 70: {'SI' if cumple_peso else 'NO'} (Peso: {peso})")
    print(f"Ojos azules: {'SI' if cumple_ojos else 'NO'} (Color: {color_ojos})")
    
    # Resultado final
    if cumple_genero and cumple_edad and cumple_estatura and cumple_peso and cumple_ojos:
        print("\nResultado: CONTRATADO")
    else:
        print("\nResultado: DESCARTADO")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_agencia_modelaje()
