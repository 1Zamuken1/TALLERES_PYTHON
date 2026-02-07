from datetime import datetime

def ejercicio_dias_entre_citas():
    """
    Calcula cuántos días faltan entre la fecha de hoy y la fecha de una cita.
    """
    print("---------------------------------------")
    print("|      CALCULO DE DIAS HASTA CITA     |")
    print("---------------------------------------")
    
    # Solicitar fecha de hoy con validación
    while True:
        try:
            fecha_hoy = input("\nIngresa la fecha de hoy (formato DD/MM/AAAA): ")
            dia_hoy, mes_hoy, anio_hoy = map(int, fecha_hoy.split('/'))
            fecha_actual = datetime(anio_hoy, mes_hoy, dia_hoy)
            break
        except ValueError:
            print("Formato incorrecto. Usa DD/MM/AAAA (ejemplo: 15/03/2024).")
        except:
            print("Fecha invalida. Intenta de nuevo.")
    
    # Solicitar fecha de la cita con validación
    while True:
        try:
            fecha_cita_str = input("Ingresa la fecha de tu cita (formato DD/MM/AAAA): ")
            dia_cita, mes_cita, anio_cita = map(int, fecha_cita_str.split('/'))
            fecha_cita = datetime(anio_cita, mes_cita, dia_cita)
            
            # Validar que la cita sea en el futuro
            if fecha_cita < fecha_actual:
                print("La fecha de la cita debe ser posterior a la fecha de hoy.")
                continue
            break
        except ValueError:
            print("Formato incorrecto. Usa DD/MM/AAAA (ejemplo: 20/05/2024).")
        except:
            print("Fecha invalida. Intenta de nuevo.")
    
    # Calcular diferencia de días
    diferencia = fecha_cita - fecha_actual
    dias_faltantes = diferencia.days
    
    print(f"\nFecha de hoy: {fecha_actual.strftime('%d/%m/%Y')}")
    print(f"Fecha de la cita: {fecha_cita.strftime('%d/%m/%Y')}")
    print(f"Faltan {dias_faltantes} dias para tu cita.")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_dias_entre_citas()
