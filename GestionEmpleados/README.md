# Sistema de Gestión de Empleados - Documentación Técnica

Este módulo implementa un gestión completa de Recursos Humanos utilizando Python, Tkinter y persistencia en archivos de texto plano (.txt). El sistema sigue principios SOLID y Patrones de Diseño para asegurar mantenibilidad y escalabilidad.

## 1. Arquitectura de Datos y Persistencia (CRUD)

El sistema utiliza **Diccionarios de Python en memoria** como base de datos principal para operaciones rápidas, y **Archivos de Texto (.txt)** para persistencia.

### Estructura de Datos

- **Empleados**: Se almacenan en un diccionario donde la clave es el `documento` (único) y el valor es otro diccionario con los datos.
  ```python
  empleados = {
      "12345": {"nombre": "Juan", "cargo": "DEV01", ...},
      "67890": {"nombre": "Maria", "cargo": "RH01", ...}
  }
  ```
- **Cargos y Departamentos**: Siguen la misma lógica (clave única = código).

### Flujo de Persistencia

1. **Carga Inicial (Init)**: Al iniciar la aplicación, la clase `BaseDatos` (Singleton) lee los archivos .txt línea por línea y reconstruye los diccionarios en memoria.
2. **Operaciones CRUD**:
   - **Create (Agregar)**: Se añade una entrada al diccionario `self.empleados[doc] = data`.
   - **Read (Leer)**: Se busca directamente en el diccionario por clave `self.empleados.get(doc)`.
   - **Update (Modificar)**: Se sobrescribe la entrada en el diccionario.
   - **Delete (Eliminar)**: Se usa `del self.empleados[doc]`.
3. **Guardado (Commit)**: Inmediatamente después de cualquier modificación (Agregar, Modificar, Eliminar), se llama a `guardar_en_archivo()`, que sobrescribe todo el archivo .txt con el estado actual del diccionario.

---

## 2. Principios SOLID Aplicados

- **S - Single Responsibility (Responsabilidad Única)**:
  - `EmpleadoRepository`: Solo maneja el acceso a datos (lectura/escritura).
  - `EmpleadoService` (o View): Solo maneja la lógica de negocio y validaciones.
  - `ReporteTXTStrategy`: Solo se encarga de formatear y generar reportes.
- **O - Open/Closed (Abierto/Cerrado)**:
  - El sistema de reportes está abierto a extensión (podríamos agregar `ReportePDFStrategy`) sin modificar el código que llama a la generación del reporte, gracias al patrón Strategy.

- **D - Dependency Inversion (Inversión de Dependencias)**:
  - Los servicios y vistas dependen de abstracciones (Repositorios) y no directamente de los archivos de texto. Si cambiáramos los .txt por una base de datos SQL en el Repositorio, el resto del sistema seguiría funcionando sin cambios.

---

## 3. Patrones de Diseño Implementados

### 1. Singleton (Base de Datos)

- **Ubicación**: `database/db_singleton.py`
- **Propósito**: Garantiza que exista **una única instancia** de la base de datos en toda la ejecución del programa.
- **Ventaja**: Evita conflictos de lectura/escritura y asegura que todos los módulos (GUI, Consola, Reportes) vean los mismos datos en tiempo real.

### 2. Repository (Repositorio)

- **Ubicación**: `repositories/`
- **Propósito**: Abstrae la lógica de acceso a datos. El resto del código no sabe si los datos vienen de un TXT, SQL o memoria; solo llama a `repo.agregar()` o `repo.buscar()`.
- **Implementación**: `EmpleadoRepository`, `CargoRepository`, `DepartamentoRepository`.

### 3. Factory (Fábrica)

- **Ubicación**: `factories/empleado_factory.py`
- **Propósito**: Centraliza la creación de objetos (diccionarios de empleados).
- **Ventaja**: Si la estructura de un empleado cambia (ej: agregamos campo "fecha_nacimiento"), solo modificamos la Fábrica y no todo el código donde se crean empleados.

### 4. Strategy (Estrategia)

- **Ubicación**: `reportes/reporte_txt_strategy.py`
- **Propósito**: Define una familia de algoritmos (generación de reportes) y los hace intercambiables.
- **Uso**: La vista de reportes utiliza esta estrategia para generar el texto final, desacoplando la lógica de presentación de la lógica de generación.

---

## 4. Interfaz Gráfica (Tkinter)

La interfaz se construye utilizando la librería estándar **Tkinter** con el módulo de widgets temáticos **`ttk`** para una apariencia moderna.

### Componentes Principales

1. **Ventana Principal (`MainWindow`)**:
   - Hereda de `tk.Tk`.
   - Utiliza `ttk.Notebook` para crear un sistema de navegación por pestañas (Empleados, Cargos, Reportes).
   - Define la geometría (1280x720) y aplica estilos globales.

2. **Vistas (`View`)**:
   - Cada pestaña es una clase separada (`EmpleadoView`, `CargoView`) que hereda de `ttk.Frame`.
   - **Layout**: Utilizan `ttk.PanedWindow` para dividir la pantalla en dos áreas redimensionables:
     - **Izquierda (Formulario)**: Campos de entrada (`Entry`, `Combobox`) y botones CRUD.
     - **Derecha (Tabla)**: Widget `ttk.Treeview` para listar los registros con columnas ordenables.
3. **Controladores de Eventos**:
   - Los botones están vinculados a métodos internos (`command=self.guardar_empleado`) que recogen los datos de las variables Tkinter (`StringVar`), llaman al Repositorio para persistir, y actualizan la tabla visualmente.

4. **Reportes con Vista Previa**:
   - La pestaña de Reportes incluye un área de texto (`tk.Text`) que muestra una previsualización en tiempo real del reporte generado por la Estrategia, antes de guardar el archivo en disco.

---

## 5. Guía de Presentación del Código (Paso a Paso)

Si tienes que explicar este proyecto a otra persona, sigue este orden lógico:

### **Paso 1: La Base (El Corazón)**

Empieza explicando dónde se guardan los datos.

1.  **Abre `database/db_singleton.py`**:
    - Explica que usas el patrón **Singleton** para que solo haya una conexión a los archivos de texto.
    - Muestra el método `__init__` donde cargas los archivos `.txt` en diccionarios (`self.empleados = {}`).
    - Muestra `guardar_en_archivo()` para evidenciar cómo se escribe en el disco.

### **Paso 2: Acceso a Datos (Los Repositorios)**

Explica cómo el código accede a esa base de datos.

1.  **Abre `repositories/empleado_repository.py`**:
    - Menciona el patrón **Repository**.
    - Explica que esta clase es el "mensajero" entre la lógica y la base de datos.
    - Muestra métodos simples como `agregar` y `buscar_por_documento` para ver cómo interactúan con el Singleton.

### **Paso 3: Lógica de Negocio (Servicios y Fábricas)**

Explica dónde están las reglas del negocio y validaciones.

1.  **Abre `factories/empleado_factory.py`**:
    - Patrón **Factory**: Muestra cómo centralizas la creación del diccionario del empleado aquí.
2.  **Abre `services/empleado_service.py`**:
    - Aquí está la "carne" del programa para la **consola**. Muestra cómo pide datos (`input`), valida (`validaciones.py`) y llama al repositorio.
    - Destaca las validaciones (ej: verificar que el documento no exista antes de crear).

### **Paso 4: Reportes (Estrategia)**

1.  **Abre `reportes/reporte_txt_strategy.py`**:
    - Patrón **Strategy**: Explica que separaste la lógica de _cómo_ se crea el reporte.
    - Muestra cómo construyes el string línea por línea (concatenación) y usas `tabulate` para las tablas.

### **Paso 5: La Interfaz Gráfica (El Gran Final)**

Cierra mostrando lo que ve el usuario final.

1.  **Abre `gui/main_window.py`**:
    - Muestra la ventana principal y las pestañas (`Notebook`).
2.  **Abre `gui/empleado_view.py`**:
    - Explica cómo usas `Treeview` para la tabla y `Entry` para el formulario.
    - Muestra un evento (ej: `guardar_empleado`) y cómo este llama directamente al `EmpleadoRepository`, reutilizando la lógica que explicaste en el Paso 2.

**Resumen para el oyente**: "Este proyecto separa claramente las capas: Datos (Singleton/Repos), Lógica (Servicios/Factory) y Presentación (Consola/GUI), lo que hace que sea muy fácil de mantener y escalar."

---

_Desarrollado para el Taller de Python - Módulo de Gestión de Empleados._
