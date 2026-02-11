"""
Modulo de Reportes
Genera informes y visualizaciones de datos usando la libreria tabulate.

DOCUMENTACION DE TABULATE:
--------------------------
Tabulate es una libreria de Python que permite crear tablas formateadas
en ASCII art, perfectas para mostrar datos estructurados en consola.

Instalacion:
    pip install tabulate

Uso basico:
    from tabulate import tabulate
    data = [["Nombre", "Edad"], ["Juan", 25], ["Ana", 30]]
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

Formatos disponibles (tablefmt):
    - "plain": Sin bordes, solo espacios
    - "simple": Lineas simples horizontales
    - "grid": Bordes completos estilo ASCII (recomendado)
    - "fancy_grid": Bordes decorativos con caracteres especiales
    - "pipe": Formato estilo Markdown
    - "html": Genera tabla HTML
    - "latex": Genera tabla LaTeX

Headers:
    - headers="firstrow": Primera fila como encabezados
    - headers=["Col1", "Col2"]: Lista personalizada de encabezados
    - Sin headers: Solo muestra los datos

Ejemplo completo:
    datos = [
        ["Juan Perez", 30, "Colombia"],
        ["Ana Garcia", 25, "Mexico"]
    ]
    headers = ["Nombre", "Edad", "Pais"]
    print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    
    Salida:
    ╒══════════════╤═══════╤═══════════╕
    │ Nombre       │ Edad  │ Pais      │
    ╞══════════════╪═══════╪═══════════╡
    │ Juan Perez   │    30 │ Colombia  │
    ├──────────────┼───────┼───────────┤
    │ Ana Garcia   │    25 │ Mexico    │
    ╘══════════════╧═══════╧═══════════╛

Principio SOLID aplicado:
- Single Responsibility: Solo genera visualizaciones
- Open/Closed: Facil agregar nuevos tipos de reportes
"""

from tabulate import tabulate
from reservas import obtener_todas_reservas


def generar_informe_general():
    """
    Genera un informe completo de todas las reservas del hotel.
    
    Este informe es utilizado por los administradores para tener una
    vista general del estado de las reservas. Muestra informacion clave
    como codigo, cliente, contacto, habitacion y costo total.
    
    Utiliza tabulate con formato 'fancy_grid' para crear una tabla
    visualmente atractiva y facil de leer en consola.
    
    La tabla incluye las siguientes columnas:
    - Codigo: Identificador unico de la reserva
    - Cliente: Nombre completo del huesped
    - ID: Numero de identificacion
    - Contacto: Telefono de contacto
    - Habitacion: Numero de habitacion asignada
    - Tipo: Tipo de habitacion (sencilla/doble/suite)
    - Noches: Numero de noches de estadia
    - Personas: Numero total de huespedes
    - Desayuno: Si/No
    - Total: Costo total de la reserva
    
    Returns:
        None: Imprime directamente en consola
    
    Example:
        >>> generar_informe_general()
        =======================================
        INFORME GENERAL DE RESERVAS
        =======================================
        Total de reservas: 3
        
        [Tabla formateada con todas las reservas]
    """
    reservas = obtener_todas_reservas()
    
    print("\n=======================================")
    print("INFORME GENERAL DE RESERVAS")
    print("=======================================")
    
    if not reservas:
        print("No hay reservas registradas en el sistema.")
        return
    
    print(f"Total de reservas: {len(reservas)}\n")
    
    # Preparar datos para la tabla
    tabla = []
    for r in reservas:
        fila = [
            r["codigo"],
            r["nombre_completo"].title(),  # Capitalizar nombres
            r["identificacion"],
            r["contacto"],
            r["num_habitacion"],
            r["tipo_habitacion"].capitalize(),
            r["noches"],
            r["total_personas"],
            "Si" if r["con_desayuno"] else "No",
            f"${r['total_pagar']:,}"
        ]
        tabla.append(fila)
    
    # Definir encabezados
    headers = ["Codigo", "Cliente", "ID", "Contacto", "Habitacion", 
               "Tipo", "Noches", "Personas", "Desayuno", "Total"]
    
    # Imprimir tabla con formato fancy_grid
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
    
    # Calcular total de ingresos
    total_ingresos = sum(r["total_pagar"] for r in reservas)
    print(f"\nTotal ingresos: ${total_ingresos:,}")


def mostrar_ticket(reserva):
    """
    Muestra el ticket detallado de una reserva especifica.
    
    Presenta toda la informacion de la reserva en formato de ticket,
    incluyendo datos del cliente, fechas, habitacion y costos.
    
    Args:
        reserva (dict): Diccionario con los datos de la reserva
    
    Returns:
        None: Imprime directamente en consola
    
    Example:
        >>> reserva = buscar_reserva_por_codigo("HTL-890-3456")
        >>> mostrar_ticket(reserva)
        =======================================
        TICKET DE RESERVA
        =======================================
        [Detalles de la reserva en formato tabla]
    """
    print("\n=======================================")
    print("TICKET DE RESERVA")
    print("=======================================")
    
    # Preparar datos para mostrar
    datos = [
        ["Codigo de Reserva", reserva["codigo"]],
        ["Fecha de Reserva", reserva["fecha_reserva"]],
        ["", ""],
        ["DATOS DEL HUESPED", ""],
        ["Nombre", reserva["nombre_completo"].title()],
        ["Identificacion", reserva["identificacion"]],
        ["Contacto", reserva["contacto"]],
        ["", ""],
        ["DETALLES DE ESTADIA", ""],
        ["Fecha Entrada", reserva["fecha_inicio"]],
        ["Fecha Salida", reserva["fecha_fin"]],
        ["Noches", reserva["noches"]],
        ["Habitacion", f"No. {reserva['num_habitacion']}"],
        ["Tipo", reserva["tipo_habitacion"].capitalize()],
        ["Total Personas", reserva["total_personas"]],
        ["Desayuno Incluido", "Si" if reserva["con_desayuno"] else "No"],
        ["", ""],
        ["COSTO TOTAL", f"${reserva['total_pagar']:,}"]
    ]
    
    # Usar formato grid para el ticket
    print(tabulate(datos, tablefmt="grid"))
    print("\nPresente este codigo al momento del check-in")


def generar_informe_detallado(reserva):
    """
    Genera un informe detallado con desglose de costos.
    
    Muestra informacion completa incluyendo el calculo detallado
    de los costos de habitacion y desayunos.
    
    Args:
        reserva (dict): Diccionario con los datos de la reserva
    
    Returns:
        None: Imprime directamente en consola
    """
    from calculos import calcular_desglose_costos
    
    print("\n=======================================")
    print("INFORME DETALLADO DE RESERVA")
    print("=======================================")
    
    # Informacion general
    info_general = [
        ["Codigo", reserva["codigo"]],
        ["Cliente", reserva["nombre_completo"].title()],
        ["ID", reserva["identificacion"]],
        ["Habitacion", f"No. {reserva['num_habitacion']} ({reserva['tipo_habitacion'].capitalize()})"],
        ["Periodo", f"{reserva['fecha_inicio']} al {reserva['fecha_fin']}"],
        ["Noches", reserva["noches"]]
    ]
    
    print("\nInformacion General:")
    print(tabulate(info_general, tablefmt="simple"))
    
    # Desglose de costos
    desglose = calcular_desglose_costos(
        reserva["tipo_habitacion"],
        reserva["noches"],
        reserva["total_personas"],
        reserva["con_desayuno"]
    )
    
    costos = [
        ["Concepto", "Detalle", "Monto"],
        ["Habitacion por noche", f"${desglose['costo_habitacion_noche']:,}", ""],
        ["Total habitacion", f"{reserva['noches']} noches", f"${desglose['costo_habitacion_total']:,}"]
    ]
    
    if reserva["con_desayuno"]:
        costos.extend([
            ["Desayuno por persona/dia", f"${desglose['costo_desayuno_persona_dia']:,}", ""],
            ["Total desayunos", f"{reserva['total_personas']} personas x {reserva['noches']} dias", 
             f"${desglose['costo_desayuno_total']:,}"]
        ])
    
    costos.append(["", "TOTAL A PAGAR", f"${desglose['costo_total']:,}"])
    
    print("\nDesglose de Costos:")
    print(tabulate(costos, headers="firstrow", tablefmt="fancy_grid"))


def generar_resumen_estadistico():
    """
    Genera estadisticas generales del hotel.
    
    Muestra metricas como:
    - Total de reservas
    - Ocupacion por tipo de habitacion
    - Ingresos totales
    - Promedio de estadia
    
    Returns:
        None: Imprime directamente en consola
    """
    reservas = obtener_todas_reservas()
    
    if not reservas:
        print("No hay datos para generar estadisticas.")
        return
    
    print("\n=======================================")
    print("ESTADISTICAS DEL HOTEL")
    print("=======================================")
    
    # Calcular metricas
    total_reservas = len(reservas)
    total_ingresos = sum(r["total_pagar"] for r in reservas)
    promedio_noches = sum(r["noches"] for r in reservas) / total_reservas
    total_huespedes = sum(r["total_personas"] for r in reservas)
    
    # Contar por tipo de habitacion
    tipos = {}
    for r in reservas:
        tipo = r["tipo_habitacion"]
        tipos[tipo] = tipos.get(tipo, 0) + 1
    
    # Tabla de estadisticas
    estadisticas = [
        ["Total Reservas", total_reservas],
        ["Total Huespedes", total_huespedes],
        ["Promedio Noches/Reserva", f"{promedio_noches:.1f}"],
        ["Ingresos Totales", f"${total_ingresos:,}"],
        ["Ingreso Promedio/Reserva", f"${total_ingresos/total_reservas:,.0f}"]
    ]
    
    print(tabulate(estadisticas, headers=["Metrica", "Valor"], tablefmt="fancy_grid"))
    
    # Ocupacion por tipo
    print("\nOcupacion por Tipo de Habitacion:")
    ocupacion = [[tipo.capitalize(), cantidad] for tipo, cantidad in tipos.items()]
    print(tabulate(ocupacion, headers=["Tipo", "Reservas"], tablefmt="grid"))
