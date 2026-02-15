import tkinter as tk
from tkinter import ttk
from .styles import aplicar_estilos
from .empleado_view import EmpleadoView
from .cargo_view import CargoView
from .reporte_view import ReporteView

class MainWindow(tk.Tk):
    """
    Ventana principal de la aplicación GUI.
    Contiene un Notebook (pestañas) para navegar entre módulos.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Gestión de Empleados")
        self.geometry("1280x720")
        self.minsize(900, 600)
        
        # Aplicar estilos
        aplicar_estilos(self)
        
        # Contenedor principal
        main_container = ttk.Frame(self)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Titulo
        header = ttk.Label(main_container, text="GESTIÓN DE EMPLEADOS", style="Header.TLabel", anchor="center")
        header.pack(fill=tk.X, pady=(0, 10))
        
        # Notebook (Pestañas)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestañas
        self.tab_empleados = EmpleadoView(self.notebook)
        self.tab_cargos = CargoView(self.notebook)
        self.tab_reportes = ReporteView(self.notebook)
        
        self.notebook.add(self.tab_empleados, text=" Empleados ")
        self.notebook.add(self.tab_cargos, text=" Cargos ")
        self.notebook.add(self.tab_reportes, text=" Reportes ")
        
        # Barra de estado
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
