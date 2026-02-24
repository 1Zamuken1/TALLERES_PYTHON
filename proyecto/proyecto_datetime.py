"""
Ejercicio - Gestion de Proyecto Formativo
Calcula dias habiles restantes para la entrega del proyecto.

Libreria principal: datetime
- Calculo de diferencia de fechas
- Exclusion de fines de semana
- Exclusion de festivos colombianos 2026
"""

from datetime import datetime, timedelta


def calcular_dias_habiles(fecha_inicio, fecha_fin, festivos):
    """
    Calcula los dias habiles entre dos fechas excluyendo fines de semana y festivos.
    
    Args:
        fecha_inicio (datetime): Fecha de inicio del proyecto
        fecha_fin (datetime): Fecha de entrega del proyecto
        festivos (list): Lista de fechas festivas
    
    Returns:
        int: Numero de dias habiles
    
    Example:
        >>> inicio = datetime(2026, 1, 29)
        >>> fin = datetime(2026, 4, 9)
        >>> festivos = [datetime(2026, 3, 23)]
        >>> dias = calcular_dias_habiles(inicio, fin, festivos)
        >>> print(dias)
        50
    """
    dias_habiles = 0
    fecha_actual = fecha_inicio
    
    while fecha_actual <= fecha_fin:
        # weekday(): 0=Lunes, 1=Martes, ..., 5=Sabado, 6=Domingo
        # Si es dia de semana (0-4) y NO es festivo
        if fecha_actual.weekday() < 5 and fecha_actual not in festivos:
            dias_habiles += 1
        
        # Avanzar al siguiente dia
        fecha_actual += timedelta(days=1)
    
    return dias_habiles


def ejercicio_gestion_proyecto():
    """
    Muestra un informe completo del estado del proyecto formativo.
    
    Calcula:
    - Dias totales del proyecto
    - Dias habiles (sin fines de semana ni festivos)
    - Dias transcurridos
    - Dias restantes
    - Porcentaje de avance basado en tiempo
    - Estado del proyecto (En curso, Vencido, Completado)
    
    Fechas del proyecto:
    - Inicio: 29 de enero de 2026
    - Entrega: 9 de abril de 2026
    
    Festivos colombianos 2026 incluidos:
    - 9 marzo (Dia de San Jose)
    - 13 abril (Domingo de Ramos)
    - 17 abril (Jueves Santo)
    - 18 abril (Viernes Santo)
    """
    # Fechas del proyecto
    fecha_inicio = datetime(2026, 1, 29)
    fecha_entrega = datetime(2026, 4, 9)
    fecha_hoy = datetime.now()
    
    # Festivos colombianos 2026 (entre enero y abril)
    festivos = [
        datetime(2026, 1, 1),   # Ano Nuevo (jueves)
        datetime(2026, 1, 12),  # Dia de los Reyes Magos (lunes)
        datetime(2026, 3, 23),  # Dia de San Jose (lunes)
        datetime(2026, 4, 2),   # Jueves Santo
        datetime(2026, 4, 3),   # Viernes Santo
    ]
    
    # Datos del proyecto
    nombre_proyecto = "Gestor de Finanzas Personales - GASTU"
    lider = "David Coba"
    integrantes = [
        "Juan Barrios",
        "Valeria Gonzalez",
        "Jaider Rodríguez"
    ]
    
    # Calculos
    dias_totales_proyecto = (fecha_entrega - fecha_inicio).days
    dias_habiles_totales = calcular_dias_habiles(fecha_inicio, fecha_entrega, festivos)
    
    # Determinar estado y calculos segun fecha actual
    if fecha_hoy < fecha_inicio:
        # Proyecto aun no inicia
        estado = "POR INICIAR"
        dias_transcurridos = 0
        dias_habiles_transcurridos = 0
        dias_restantes = dias_totales_proyecto
        dias_habiles_restantes = dias_habiles_totales
        porcentaje_avance = 0.0
    elif fecha_hoy > fecha_entrega:
        # Proyecto vencido
        estado = "VENCIDO"
        dias_transcurridos = (fecha_hoy - fecha_inicio).days
        dias_habiles_transcurridos = calcular_dias_habiles(fecha_inicio, fecha_entrega, festivos)
        dias_restantes = 0
        dias_habiles_restantes = 0
        dias_retraso = (fecha_hoy - fecha_entrega).days
        porcentaje_avance = 100.0
    else:
        # Proyecto en curso
        estado = "EN CURSO"
        dias_transcurridos = (fecha_hoy - fecha_inicio).days
        dias_habiles_transcurridos = calcular_dias_habiles(fecha_inicio, fecha_hoy, festivos)
        dias_restantes = (fecha_entrega - fecha_hoy).days
        dias_habiles_restantes = calcular_dias_habiles(fecha_hoy, fecha_entrega, festivos)
        
        # Porcentaje basado en dias habiles transcurridos
        if dias_habiles_totales > 0:
            porcentaje_avance = (dias_habiles_transcurridos / dias_habiles_totales) * 100
        else:
            porcentaje_avance = 0.0
    
    # Determinar si esta completado (esto seria manual en la realidad)
    # Por ahora, consideramos completado si llego a la fecha de entrega
    if fecha_hoy >= fecha_entrega:
        estado_completado = "COMPLETADO"  # Podria ser "VENCIDO" si no se entrego
    else:
        estado_completado = estado
    
    # Mostrar informe
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          INFORME DE PROYECTO FORMATIVO                   ║")
    print("╚══════════════════════════════════════════════════════════╝")
    
    print(f"\nProyecto: {nombre_proyecto}")
    print(f"Lider del Proyecto: {lider}")
    
    print("\nIntegrantes del equipo:")
    for i, integrante in enumerate(integrantes, 1):
        print(f"  {i}. {integrante}")
    
    print("\n" + "─" * 60)
    print("FECHAS DEL PROYECTO")
    print("─" * 60)
    print(f"Fecha de inicio:    {fecha_inicio.strftime('%d de %B de %Y')}")
    print(f"Fecha de entrega:   {fecha_entrega.strftime('%d de %B de %Y')}")
    print(f"Fecha actual:       {fecha_hoy.strftime('%d de %B de %Y')}")
    
    print("\n" + "─" * 60)
    print("TIEMPO DEL PROYECTO")
    print("─" * 60)
    print(f"Duracion total:            {dias_totales_proyecto} dias calendario")
    print(f"Dias habiles totales:      {dias_habiles_totales} dias")
    print(f"Festivos en el periodo:    {len(festivos)} dias")
    
    print("\n" + "─" * 60)
    print("AVANCE Y TIEMPO RESTANTE")
    print("─" * 60)
    print(f"Dias transcurridos:        {dias_transcurridos} dias calendario")
    print(f"Dias habiles trabajados:   {dias_habiles_transcurridos} dias")
    print(f"Dias restantes:            {dias_restantes} dias calendario")
    print(f"Dias habiles restantes:    {dias_habiles_restantes} dias")
    
    # Barra de progreso visual
    barra_longitud = 40
    progreso_lleno = int((porcentaje_avance / 100) * barra_longitud)
    barra = "█" * progreso_lleno + "░" * (barra_longitud - progreso_lleno)
    
    print("\n" + "─" * 60)
    print("ESTADO DEL PROYECTO")
    print("─" * 60)
    print(f"Estado:                    {estado_completado}")
    print(f"Porcentaje de avance:      {porcentaje_avance:.1f}%")
    print(f"Progreso: [{barra}] {porcentaje_avance:.1f}%")
    
    if estado == "VENCIDO":
        print(f"\nALERTA: El proyecto lleva {dias_retraso} dias de retraso")
    elif dias_habiles_restantes <= 5 and dias_habiles_restantes > 0:
        print(f"\nADVERTENCIA: Solo quedan {dias_habiles_restantes} dias habiles!")
    
    print("\n" + "═" * 60)
    
    # Festivos proximos
    festivos_pendientes = [f for f in festivos if f > fecha_hoy and f < fecha_entrega]
    if festivos_pendientes and estado == "EN CURSO":
        print("\nFestivos pendientes:")
        for festivo in festivos_pendientes:
            print(f"  - {festivo.strftime('%d de %B de %Y')}")
        print()
    
    input("Presiona Enter para continuar...")


if __name__ == "__main__":
    ejercicio_gestion_proyecto()
