import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import glob
from ..repositories.empleado_repository import EmpleadoRepository
from ..repositories.cargo_repository import CargoRepository
from ..repositories.departamento_repository import DepartamentoRepository
from ..reportes.reporte_txt_strategy import ReporteTXTStrategy

class ReporteView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.empleado_repo = EmpleadoRepository()
        self.cargo_repo = CargoRepository()
        self.depto_repo = DepartamentoRepository()
        self.reporte_strategy = ReporteTXTStrategy()
        
        self.var_depto = tk.StringVar()
        self.create_widgets()
        self.cargar_reportes_anteriores()

    def create_widgets(self):
        # Frame principal
        frame_main = ttk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # === Panel Superior: Generación ===
        frame_top = ttk.Frame(frame_main)
        frame_top.pack(fill=tk.X, pady=(0, 10))
        
        # --- Reporte por Departamento ---
        frame_depto = ttk.LabelFrame(frame_top, text="Reporte por Departamento")
        frame_depto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        frame_sel = ttk.Frame(frame_depto)
        frame_sel.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_sel, text="Departamento:").pack(side=tk.LEFT, padx=(0, 5))
        self.combo_depto = ttk.Combobox(frame_sel, textvariable=self.var_depto, state="readonly", width=30)
        self.combo_depto.pack(side=tk.LEFT, padx=(0, 10))
        self.actualizar_combo_deptos()
        
        ttk.Button(frame_sel, text="Generar", command=self.generar_reporte_depto).pack(side=tk.LEFT)
        
        # --- Reporte General ---
        frame_general = ttk.LabelFrame(frame_top, text="Reporte General")
        frame_general.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        frame_btn_gen = ttk.Frame(frame_general)
        frame_btn_gen.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_btn_gen, text="Todos los departamentos:").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(frame_btn_gen, text="Generar Reporte General", command=self.generar_reporte_general).pack(side=tk.LEFT)
        
        # === Panel Inferior: Vista Previa + Reportes Anteriores ===
        paned = ttk.PanedWindow(frame_main, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # --- Reportes Anteriores ---
        frame_hist = ttk.LabelFrame(paned, text="Reportes Anteriores")
        paned.add(frame_hist, weight=1)
        
        self.list_reportes = tk.Listbox(frame_hist, font=("Helvetica", 9))
        scroll_list = ttk.Scrollbar(frame_hist, orient=tk.VERTICAL, command=self.list_reportes.yview)
        self.list_reportes.configure(yscrollcommand=scroll_list.set)
        
        self.list_reportes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_list.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.list_reportes.bind("<<ListboxSelect>>", self.ver_reporte_anterior)
        
        # --- Vista previa ---
        frame_preview = ttk.LabelFrame(paned, text="Vista Previa del Reporte")
        paned.add(frame_preview, weight=3)
        
        self.text_preview = tk.Text(frame_preview, wrap=tk.NONE, font=("Consolas", 9))
        
        scroll_y = ttk.Scrollbar(frame_preview, orient=tk.VERTICAL, command=self.text_preview.yview)
        scroll_x = ttk.Scrollbar(frame_preview, orient=tk.HORIZONTAL, command=self.text_preview.xview)
        self.text_preview.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        self.text_preview.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        
        frame_preview.rowconfigure(0, weight=1)
        frame_preview.columnconfigure(0, weight=1)

    def actualizar_combo_deptos(self):
        deptos = self.depto_repo.obtener_todos().values()
        opciones = [f"{d['codigo']} - {d['nombre']}" for d in deptos]
        self.combo_depto['values'] = opciones

    def cargar_reportes_anteriores(self):
        """Carga la lista de reportes .txt existentes en la carpeta 'reportes/'."""
        self.list_reportes.delete(0, tk.END)
        self.reportes_paths = []
        
        if os.path.exists("reportes"):
            archivos = sorted(glob.glob("reportes/*.txt"), reverse=True)
            for archivo in archivos:
                nombre = os.path.basename(archivo)
                self.list_reportes.insert(tk.END, nombre)
                self.reportes_paths.append(archivo)

    def ver_reporte_anterior(self, event):
        """Muestra el contenido de un reporte seleccionado de la lista."""
        seleccion = self.list_reportes.curselection()
        if not seleccion:
            return
        
        ruta = self.reportes_paths[seleccion[0]]
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
            self.text_preview.delete("1.0", tk.END)
            self.text_preview.insert("1.0", contenido)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

    def _preguntar_guardar(self, contenido, nombre_sugerido):
        """Abre un diálogo 'Guardar como' para que el usuario elija dónde guardar."""
        # Carpeta de descargas por defecto
        descargas = os.path.join(os.path.expanduser("~"), "Downloads")
        if not os.path.exists(descargas):
            descargas = os.path.expanduser("~")
        
        ruta = filedialog.asksaveasfilename(
            title="Guardar Reporte",
            initialdir=descargas,
            initialfile=nombre_sugerido,
            defaultextension=".txt",
            filetypes=[("Archivo de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if ruta:
            try:
                with open(ruta, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                messagebox.showinfo("Éxito", f"Reporte guardado en:\n{ruta}")
                return ruta
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar:\n{e}")
        return None

    def generar_reporte_depto(self):
        depto_sel = self.var_depto.get()
        if not depto_sel:
            messagebox.showwarning("Aviso", "Seleccione un departamento")
            return
            
        cod_depto = depto_sel.split(" - ")[0]
        departamento = self.depto_repo.buscar_por_codigo(cod_depto)
        if not departamento:
            messagebox.showerror("Error", "Departamento no encontrado")
            return
        
        empleados = self._obtener_empleados_depto(cod_depto)
        cargos = self.cargo_repo.obtener_todos()
        
        # Adaptar datos: en el reporte, emp['cargo'] es el codigo_cargo
        empleados_adaptados = []
        for emp in empleados:
            emp_copy = dict(emp)
            if 'cargo' not in emp_copy:
                emp_copy['cargo'] = emp_copy.get('codigo_cargo', 'N/A')
            empleados_adaptados.append(emp_copy)
        
        contenido = self.reporte_strategy.generar_reporte_departamento(departamento, empleados_adaptados, cargos)
        
        # Mostrar vista previa
        self.text_preview.delete("1.0", tk.END)
        self.text_preview.insert("1.0", contenido)
        
        # Diálogo "Guardar como"
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre = f"reporte_{cod_depto}_{timestamp}.txt"
        self._preguntar_guardar(contenido, nombre)
        self.cargar_reportes_anteriores()

    def generar_reporte_general(self):
        deptos = self.depto_repo.obtener_todos()
        cargos = self.cargo_repo.obtener_todos()
        
        departamentos_data = []
        for cod, depto in deptos.items():
            empleados = self._obtener_empleados_depto(cod)
            empleados_adaptados = []
            for emp in empleados:
                emp_copy = dict(emp)
                if 'cargo' not in emp_copy:
                    emp_copy['cargo'] = emp_copy.get('codigo_cargo', 'N/A')
                empleados_adaptados.append(emp_copy)
            departamentos_data.append((depto, empleados_adaptados, cargos))
        
        contenido = self.reporte_strategy.generar_reporte_general(departamentos_data)
        
        self.text_preview.delete("1.0", tk.END)
        self.text_preview.insert("1.0", contenido)
        
        # Diálogo "Guardar como"
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre = f"reporte_general_{timestamp}.txt"
        self._preguntar_guardar(contenido, nombre)
        self.cargar_reportes_anteriores()

    def _obtener_empleados_depto(self, cod_depto):
        """Obtiene empleados cuyo cargo pertenece al departamento dado."""
        todos_emp = self.empleado_repo.obtener_todos()
        cargos_depto = self.cargo_repo.buscar_por_departamento(cod_depto)
        codigos_cargos_depto = {c['codigo'] for c in cargos_depto}
        
        resultado = []
        for doc, emp in todos_emp.items():
            cod_cargo = emp.get('cargo', emp.get('codigo_cargo', ''))
            if cod_cargo in codigos_cargos_depto:
                resultado.append(emp)
        return resultado
