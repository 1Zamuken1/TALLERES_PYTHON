def ejercicio_contar_vocales_consonantes():
    """
    Cuenta cuántas y cuáles vocales y consonantes hay en una frase.
    """
    print("---------------------------------------")
    print("|  CONTADOR DE VOCALES Y CONSONANTES  |")
    print("---------------------------------------")
    
    # Solicitar frase con validación
    while True:
        frase = input("\nIngresa una frase: ").strip()
        if len(frase) == 0:
            print("La frase no puede estar vacia. Intenta de nuevo.")
            continue
        break
    
    # Definir vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    
    # Contadores
    vocales_encontradas = []
    consonantes_encontradas = []
    otros_caracteres = []
    
    # Contar cada tipo de carácter
    for caracter in frase:
        if caracter.isalpha():  # Si es una letra
            if caracter in vocales:
                vocales_encontradas.append(caracter.lower())
            else:
                consonantes_encontradas.append(caracter.lower())
        elif not caracter.isspace():  # Si no es letra ni espacio
            otros_caracteres.append(caracter)
    
    # Contar ocurrencias de cada vocal
    conteo_vocales = {}
    for vocal in "aeiouáéíóú":
        cantidad = vocales_encontradas.count(vocal)
        if cantidad > 0:
            conteo_vocales[vocal] = cantidad
    
    # Contar ocurrencias de cada consonante
    conteo_consonantes = {}
    for consonante in set(consonantes_encontradas):
        cantidad = consonantes_encontradas.count(consonante)
        conteo_consonantes[consonante] = cantidad
    
    # Mostrar resultados
    print(f"\nFrase analizada: '{frase}'")
    
    # Vocales
    print(f"\nVOCALES:")
    print(f"   Total de vocales: {len(vocales_encontradas)}")
    if conteo_vocales:
        print(f"   Vocales encontradas:")
        for vocal, cantidad in sorted(conteo_vocales.items()):
            print(f"      '{vocal}' aparece {cantidad} vez/veces")
    else:
        print(f"   No se encontraron vocales.")
    
    # Consonantes
    print(f"\nCONSONANTES:")
    print(f"   Total de consonantes: {len(consonantes_encontradas)}")
    if conteo_consonantes:
        print(f"   Consonantes encontradas:")
        for consonante, cantidad in sorted(conteo_consonantes.items()):
            print(f"      '{consonante}' aparece {cantidad} vez/veces")
    else:
        print(f"   No se encontraron consonantes.")
    
    # Otros caracteres
    if otros_caracteres:
        print(f"\nOTROS CARACTERES (numeros, simbolos): {len(otros_caracteres)}")
        print(f"   {', '.join(otros_caracteres)}")
    
    # Resumen final
    total_letras = len(vocales_encontradas) + len(consonantes_encontradas)
    print(f"\nRESUMEN:")
    print(f"  Total de letras: {total_letras}")
    print(f"  Vocales: {len(vocales_encontradas)}")
    print(f"  Consonantes: {len(consonantes_encontradas)}")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_contar_vocales_consonantes()
