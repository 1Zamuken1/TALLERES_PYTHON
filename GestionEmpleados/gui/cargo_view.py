import tkinter as tk
from tkinter import ttk, messagebox
from ..repositories.cargo_repository import CargoRepository
from ..repositories.departamento_repository import DepartamentoRepository

class CargoView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.cargo_repo = CargoRepository()
        self.depto_repo = DepartamentoRepository()
        
        self.var_codigo = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_depto = tk.StringVar()
        
        self.create_widgets()
        self.cargar_datos()

    def create_widgets(self):
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # --- Formulario ---
        frame_form = ttk.LabelFrame(paned, text="Datos del Cargo")
        paned.add(frame_form, weight=1)
        
        ttk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_codigo = ttk.Entry(frame_form, textvariable=self.var_codigo)
        self.entry_codigo.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.var_nombre).grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Departamento:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.combo_depto = ttk.Combobox(frame_form, textvariable=self.var_depto, state="readonly")
        self.combo_depto.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        self.actualizar_combo_deptos()
        
        frame_btns = ttk.Frame(frame_form)
        frame_btns.grid(row=3, column=0, columnspan=2, pady=20)
        
        ttk.Button(frame_btns, text="Guardar", command=self.guardar_cargo).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Actualizar", command=self.actualizar_cargo).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Eliminar", command=self.eliminar_cargo).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Limpiar", command=self.limpiar_form).pack(side=tk.LEFT, padx=5)
        
        frame_form.columnconfigure(1, weight=1)
        
        # --- Tabla ---
        frame_table = ttk.LabelFrame(paned, text="Lista de Cargos")
        paned.add(frame_table, weight=3)
        
        columns = ("codigo", "nombre", "departamento")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("departamento", text="Departamento")
        
        self.tree.column("codigo", width=100)
        self.tree.column("nombre", width=250)
        self.tree.column("departamento", width=200)
        
        scrollbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_cargo)

    def actualizar_combo_deptos(self):
        deptos = self.depto_repo.obtener_todos().values()
        opciones = [f"{d['codigo']} - {d['nombre']}" for d in deptos]
        self.combo_depto['values'] = opciones

    def cargar_datos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        cargos = self.cargo_repo.obtener_todos()
        deptos = self.depto_repo.obtener_todos()
        
        for cod, cargo in cargos.items():
            cod_depto = cargo.get('departamento', 'N/A')
            nombre_depto = deptos.get(cod_depto, {}).get('nombre', 'N/A')
            self.tree.insert("", tk.END, values=(cod, cargo['nombre'], nombre_depto))

    def guardar_cargo(self):
        codigo = self.var_codigo.get().strip().upper()
        nombre = self.var_nombre.get().strip()
        depto_sel = self.var_depto.get()
        
        if not codigo or not nombre or not depto_sel:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        if self.cargo_repo.existe_codigo(codigo):
            messagebox.showerror("Error", "Ya existe un cargo con ese código")
            return
            
        cod_depto = depto_sel.split(" - ")[0]
        cargo = {"codigo": codigo, "nombre": nombre, "departamento": cod_depto}
        self.cargo_repo.agregar(cargo)
        messagebox.showinfo("Éxito", "Cargo creado correctamente")
        self.limpiar_form()
        self.cargar_datos()

    def actualizar_cargo(self):
        codigo = self.var_codigo.get().strip().upper()
        nombre = self.var_nombre.get().strip()
        depto_sel = self.var_depto.get()
        
        if not codigo or not nombre or not depto_sel:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        if not self.cargo_repo.existe_codigo(codigo):
            messagebox.showerror("Error", "No se encontró el cargo con ese código")
            return
            
        cod_depto = depto_sel.split(" - ")[0]
        cargo_act = {"codigo": codigo, "nombre": nombre, "departamento": cod_depto}
        if self.cargo_repo.modificar(codigo, cargo_act):
            messagebox.showinfo("Éxito", "Cargo actualizado")
            self.limpiar_form()
            self.cargar_datos()

    def eliminar_cargo(self):
        codigo = self.var_codigo.get().strip().upper()
        if not codigo:
            messagebox.showwarning("Aviso", "Seleccione un cargo para eliminar")
            return
        if messagebox.askyesno("Confirmar", f"¿Eliminar el cargo {codigo}?"):
            if self.cargo_repo.eliminar(codigo):
                messagebox.showinfo("Éxito", "Cargo eliminado")
                self.limpiar_form()
                self.cargar_datos()

    def seleccionar_cargo(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        valores = self.tree.item(seleccion[0])['values']
        self.var_codigo.set(valores[0])
        self.var_nombre.set(valores[1])
        # Buscar el departamento en el combo
        cargo_data = self.cargo_repo.buscar_por_codigo(str(valores[0]))
        if cargo_data:
            cod_depto = cargo_data.get('departamento')
            for val in self.combo_depto['values']:
                if val.startswith(f"{cod_depto} -"):
                    self.combo_depto.set(val)
                    break

    def limpiar_form(self):
        self.var_codigo.set("")
        self.var_nombre.set("")
        self.var_depto.set("")
        self.tree.selection_remove(self.tree.selection())
