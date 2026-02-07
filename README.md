# Talleres Python - SENA

Bienvenida/o a este repositorio estudiantil. Este proyecto contiene una colección de ejercicios de programación en Python organizados por temas y dificultad. Es un espacio para practicar, aprender y mejorar habilidades de programación.

## ¿Qué es este proyecto?

Este es un repositorio educativo creado para estudiantes del SENA que desean practicar y mejorar sus habilidades en programación con Python. Contiene diferentes talleres con ejercicios propuestos en clase y tareas, organizados de manera progresiva para facilitar el aprendizaje.

## Contenido del Proyecto

El repositorio está organizado en los siguientes talleres:

### Taller 1: Variables
Ejercicios básicos para practicar el uso de variables y operaciones matemáticas simples.
- Suma de edades
- Promedio de temperaturas
- División de agua
- Cálculo de cambio
- Y muchos más...

### Taller 2: Cuenta Bancaria
Simulación interactiva de una cuenta bancaria donde puedes:
- Recibir un saludo de bienvenida
- Consultar tu saldo
- Realizar retiros
- Hacer consignaciones (depósitos)

### Taller 3: Ciclos (For y While)
Ejercicios que practican el uso de bucles y estructuras de repetición:
- Operaciones con números (pares, impares, primos)
- Juegos interactivos (número secreto)
- Manipulación de texto
- Y más de 20 ejercicios diferentes

## ¿Qué necesitas para ejecutar el proyecto?

### Requisitos:
1. **Python 3.7 o superior** instalado en tu computadora
   - Descárgalo desde: https://www.python.org/downloads/
   - Asegúrate de marcar la opción **"Add Python to PATH"** durante la instalación

2. **Un editor de código** (opcional pero recomendado):
   - Visual Studio Code
   - PyCharm
   - O cualquier editor de texto

3. **Terminal o Símbolo del sistema** para ejecutar el programa

## Cómo ejecutar el programa

### Paso 1: Abre tu terminal/símbolo del sistema
- En Windows: Presiona `Win + R`, escribe `cmd` y presiona Enter
- En Mac/Linux: Abre la terminal desde aplicaciones

### Paso 2: Navega a la carpeta del proyecto
```
cd ruta/donde/esta/el/proyecto
```

Ejemplo:
```
cd C:\Users\TuUsuario\Downloads\Talleres_Python
```

### Paso 3: Ejecuta el programa
```
python menu.py
```

¡Eso es todo! Deberías ver el menú principal aparecer en tu terminal.

## Cómo usar el programa

Una vez ejecutes `python menu.py`, verás un menú principal con 3 opciones:

### Menú Principal
```
╔════════════════════════════════════╗
║    TALLERES PYTHON                 ║
╠════════════════════════════════════╣
║  1. Taller 1 - Variables           ║
║  2. Taller 2 - Cuenta Bancaria     ║
║  3. Taller 2 - Ciclo for y While   ║
╠════════════════════════════════════╣
║  0. Salir                          ║
╚════════════════════════════════════╝
```

**¿Cómo navegar?**
1. Escribe el número de la opción que deseas
2. Presiona Enter
3. Sigue las instrucciones que aparecen en pantalla
4. Para regresar al menú anterior, selecciona "0" o la opción "Regresar"

### Ejemplo de navegación:
1. Escribe `1` y presiona Enter → Accedes al **Taller 1 - Variables**
2. Verás otro menú con 10 ejercicios diferentes
3. Selecciona el ejercicio que quieres practicar
4. Completa el ejercicio siguiendo las instrucciones
5. Presiona `0` para regresar al menú del Taller 1
6. Vuelve a presionar `0` para regresar al menú principal

## Estructura del proyecto

```
Talleres_Python/
│
├── menu.py                 (↑ Archivo principal - Aquí comienza todo!)
│
├── Taller1_Normal/         (Versión sin optimización de los ejercicios)
├── Taller1_Ref/            (Versión mejorada/referencia del Taller 1)
│
├── Taller2_while_for/      (Ejercicios con bucles for y while)
│
├── cuenta_bancaria/        (Simulador de cuenta bancaria)
│   ├── menu_cuenta.py
│   ├── saludo.py
│   └── __init__.py
│
└── README.md              (Este archivo!)
```

## Consejos para aprovechar mejor el repositorio

**Recomendaciones:**
- Intenta resolver los ejercicios **sin ver la solución** primero
- Lee el código de referencia para entender diferentes formas de resolver problemas
- Practica regularmente, no solo en un día
- Si algo no funciona, revisa el código paso a paso
- Experimenta modificando los ejercicios

**Evita:**
- Copiar respuestas sin entender el código
- Saltarte los ejercicios básicos
- Desistir si algo no funciona a la primera

## ¿Algo no funciona?

Si tienes problemas ejecutando el programa:

1. **Verifica que Python está instalado:**
   ```
   python --version
   ```
   Deberías ver un número de versión (ej: Python 3.9.0)

2. **Verifica que estás en la carpeta correcta:**
   El archivo `menu.py` debe estar en esa carpeta

3. **Intenta ejecutar con `python3` en lugar de `python`:**
   ```
   python3 menu.py
   ```

## Información importante

- **Lenguaje:** Python 3.x
- **Nivel:** Principiante a Intermedio
- **Duración:** Conjunto de ejercicios progresivos
- **Propósito:** Aprendizaje y práctica educativa
