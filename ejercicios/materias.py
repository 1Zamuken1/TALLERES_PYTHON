def ejercicio_asignaturas():
    """
    Gestiona el ingreso y muestra notas por asignatura
    """
    # Definición de lista
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje", "Programación"]
    
    boletin_notas = {}
    
    print("╔════════════════════════════════════╗")
    print("║    REGISTRO DE NOTIFICACIONES      ║")
    print("╚════════════════════════════════════╝")
    
    # Captura datos
    for asignatura in materias:
        while True:
            try:
                nota = float(input(f"Que nota has sacado en {asignatura}? (1.0 - 5.0): "))
                if 1.0 <= nota <= 5.0:
                    boletin_notas[asignatura] = nota
                    break
                else:
                    print("Error, la nota debe estar entre 1.0 y 5.0")
            except ValueError:
                print("Error. Por favor ingresa un número válido")

    # Mostrar datos
    print("╔════════════════════════════════════╗")
    print("║    RESULTADOS DEL CURSO:           ║")
    print("╚════════════════════════════════════╝")
    for asignatura, nota in boletin_notas.items():
        print(f"En {asignatura} has sacado {nota}")
    print("--"*30)
    
if __name__=="__main__":
    ejercicio_asignaturas()