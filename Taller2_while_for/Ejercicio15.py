def ejercicio_personaje_historico():
    """
    Identifica personajes históricos y muestra un mensaje asociado.
    """
    print("---------------------------------------")
    print("|      PERSONAJE HISTORICO            |")
    print("---------------------------------------")
    
    # Solicitar nombre del personaje
    personaje = input("\nIngresa el nombre de un personaje historico: ").strip().upper()
    
    # Evaluar personaje
    print(f"\nPersonaje: {personaje}")
    
    if personaje == "BOLIVAR":
        print("Mensaje: LIBERTADOR")
    elif personaje == "MADRE TERESA":
        print("Mensaje: SERVICIO A LOS POBRES")
    elif personaje == "GANDHI":
        print("Mensaje: LIBERTAD A LA INDIA")
    else:
        print("Mensaje: NO IDENTIFICADO")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_personaje_historico()
