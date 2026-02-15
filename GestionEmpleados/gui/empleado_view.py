import tkinter as tk
from tkinter import ttk, messagebox
from ..repositories.empleado_repository import EmpleadoRepository
from ..repositories.cargo_repository import CargoRepository
from ..factories.empleado_factory import EmpleadoFactory

class EmpleadoView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.empleado_repo = EmpleadoRepository()
        self.cargo_repo = CargoRepository()
        
        # Variables de control
        self.var_documento = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_celular = tk.StringVar()
        self.var_correo = tk.StringVar()
        self.var_cargo = tk.StringVar()
        
        self.create_widgets()
        self.cargar_datos()

    def create_widgets(self):
        # Layout principal: Izquierda (Form), Derecha (Tabla)
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # --- Panel Izquierdo: Formulario ---
        frame_form = ttk.LabelFrame(paned, text="Datos del Empleado")
        paned.add(frame_form, weight=1)
        
        # Grid layout para el formulario
        ttk.Label(frame_form, text="Documento:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_doc = ttk.Entry(frame_form, textvariable=self.var_documento)
        self.entry_doc.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Nombre Completo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.var_nombre).grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Celular:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.var_celular).grid(row=2, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Correo:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.var_correo).grid(row=3, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Label(frame_form, text="Cargo:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.combo_cargo = ttk.Combobox(frame_form, textvariable=self.var_cargo, state="readonly")
        self.combo_cargo.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=5)
        self.actualizar_combo_cargos()
        
        # Botones
        frame_btns = ttk.Frame(frame_form)
        frame_btns.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(frame_btns, text="Guardar", command=self.guardar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Actualizar", command=self.actualizar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Eliminar", command=self.eliminar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Limpiar", command=self.limpiar_form).pack(side=tk.LEFT, padx=5)

        frame_form.columnconfigure(1, weight=1)

        # --- Panel Derecho: Tabla ---
        frame_table = ttk.LabelFrame(paned, text="Lista de Empleados")
        paned.add(frame_table, weight=3)
        
        columns = ("documento", "nombre", "cargo", "celular", "correo")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("documento", text="Documento")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("cargo", text="Cargo")
        self.tree.heading("celular", text="Celular")
        self.tree.heading("correo", text="Correo")
        
        self.tree.column("documento", width=100)
        self.tree.column("nombre", width=200)
        self.tree.column("cargo", width=150)
        self.tree.column("celular", width=100)
        self.tree.column("correo", width=200)
        
        scrollbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind seleccion
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_empleado)

    def actualizar_combo_cargos(self):
        cargos = self.cargo_repo.obtener_todos().values()
        opciones = [f"{c['codigo']} - {c['nombre']}" for c in cargos]
        self.combo_cargo['values'] = opciones

    def cargar_datos(self):
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        empleados = self.empleado_repo.obtener_todos()
        cargos = self.cargo_repo.obtener_todos()
        
        for doc, emp in empleados.items():
            # Buscar nombre del cargo (la Factory guarda la llave como 'cargo')
            cod_cargo = emp.get('cargo', emp.get('codigo_cargo', 'N/A'))
            nombre_cargo = "Desconocido"
            if cod_cargo in cargos:
                nombre_cargo = cargos[cod_cargo]['nombre']
            
            self.tree.insert("", tk.END, values=(
                doc,
                emp['nombre'],
                nombre_cargo,
                emp['celular'],
                emp['correo']
            ))

    def validar_datos(self):
        if not self.var_documento.get().strip():
            messagebox.showerror("Error", "El documento es obligatorio")
            return False
        if not self.var_nombre.get().strip():
            messagebox.showerror("Error", "El nombre es obligatorio")
            return False
        if not self.var_cargo.get():
            messagebox.showerror("Error", "Debe seleccionar un cargo")
            return False
        return True

    def guardar_empleado(self):
        if not self.validar_datos():
            return
            
        doc = self.var_documento.get().strip()
        if self.empleado_repo.existe_documento(doc):
            messagebox.showerror("Error", "Ya existe un empleado con ese documento")
            return
            
        # Extraer codigo cargo del string "COD - Nombre"
        cod_cargo = self.var_cargo.get().split(" - ")[0]
        
        empleado = EmpleadoFactory.crear_empleado(
            documento=doc,
            nombre=self.var_nombre.get().strip(),
            celular=self.var_celular.get().strip(),
            correo=self.var_correo.get().strip(),
            codigo_cargo=cod_cargo
        )
        
        if self.empleado_repo.agregar(empleado):
            messagebox.showinfo("Éxito", "Empleado agregado correctamente")
            self.limpiar_form()
            self.cargar_datos()
        else:
            messagebox.showerror("Error", "No se pudo guardar el empleado")

    def actualizar_empleado(self):
        if not self.validar_datos():
            return
        
        doc = self.var_documento.get().strip()
        # En actualizar, el documento debe existir (es la llave)
        # Ojo: si cambió el documento en el entry, intentará actualizar otro ID o fallará si no existe.
        # Por seguridad, deberíamos bloquear el entry de documento al editar.
        
        if not self.empleado_repo.existe_documento(doc):
            messagebox.showerror("Error", "No se encuentra el empleado con ese documento")
            return

        cod_cargo = self.var_cargo.get().split(" - ")[0]
        
        empleado_actualizado = EmpleadoFactory.crear_empleado(
            documento=doc,
            nombre=self.var_nombre.get().strip(),
            celular=self.var_celular.get().strip(),
            correo=self.var_correo.get().strip(),
            codigo_cargo=cod_cargo
        )
        
        if self.empleado_repo.modificar(doc, empleado_actualizado):
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.limpiar_form()
            self.cargar_datos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar")

    def eliminar_empleado(self):
        doc = self.var_documento.get().strip()
        if not doc:
            messagebox.showwarning("Aviso", "Seleccione un empleado para eliminar")
            return
            
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al empleado {doc}?"):
            if self.empleado_repo.eliminar(doc):
                messagebox.showinfo("Éxito", "Empleado eliminado")
                self.limpiar_form()
                self.cargar_datos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")

    def seleccionar_empleado(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return
            
        item = self.tree.item(seleccion[0])
        valores = item['values']
        # valores = (doc, nombre, nombre_cargo, celular, correo)
        
        self.var_documento.set(valores[0])
        self.var_nombre.set(valores[1])
        self.var_celular.set(valores[3])
        self.var_correo.set(valores[4])
        
        # Seleccionar cargo en el combo
        # El treeview tiene el NOMBRE del cargo, pero necesito el CODIGO para el combo
        # Buscar el codigo basado en el nombre (ineficiente pero funcional) o buscar en el empleado original
        empleado_data = self.empleado_repo.buscar_por_documento(str(valores[0])) # valores[0] puede ser int
        if empleado_data:
            cod_cargo = empleado_data.get('cargo', empleado_data.get('codigo_cargo'))
            # Buscar en los values del combo cual empieza con ese codigo
            for val in self.combo_cargo['values']:
                if val.startswith(f"{cod_cargo} -"):
                    self.combo_cargo.set(val)
                    break

        # Opcional: Deshabilitar el entry de documento para evitar que cambien la PK al editar
        # self.entry_doc.config(state='disabled')

    def limpiar_form(self):
        self.var_documento.set("")
        self.var_nombre.set("")
        self.var_celular.set("")
        self.var_correo.set("")
        self.var_cargo.set("")
        self.entry_doc.config(state='normal')
        self.tree.selection_remove(self.tree.selection())
