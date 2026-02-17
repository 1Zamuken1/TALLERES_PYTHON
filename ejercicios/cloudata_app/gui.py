"""
GUI del Sistema de Inventario Cloudata SAS
Interfaz gráfica con Tkinter siguiendo el estilo de GestionEmpleados.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from cloudata_app.services import InventarioService


# ══════════════════════════════════════════════
#                   ESTILOS
# ══════════════════════════════════════════════

# Paleta de colores
BG_COLOR     = "#f0f0f0"
HEADER_BG    = "#2c3e50"
HEADER_FG    = "#ecf0f1"
ACCENT       = "#3498db"
ACCENT_HOVER = "#2980b9"
SUCCESS      = "#27ae60"
WARNING      = "#e67e22"
DANGER       = "#e74c3c"
PURPLE       = "#8e44ad"
CARD_BG      = "white"
TEXT_COLOR   = "#2c3e50"
TEXT_MUTED   = "#7f8c8d"

# Tipografía
FONT_FAMILY  = "Helvetica"
FONT_TITLE   = (FONT_FAMILY, 14, "bold")
FONT_HEADING = (FONT_FAMILY, 12, "bold")
FONT_BODY    = (FONT_FAMILY, 10)
FONT_SMALL   = (FONT_FAMILY, 9)
FONT_STAT    = (FONT_FAMILY, 22, "bold")
FONT_TAB     = (FONT_FAMILY, 10, "bold")


def aplicar_estilos(root):
    """Configura los estilos globales de la aplicación"""
    style = ttk.Style(root)
    try:
        style.theme_use('clam')
    except Exception:
        pass

    root.configure(bg=BG_COLOR)

    # Frames
    style.configure("TFrame", background=BG_COLOR)
    style.configure("Card.TFrame", background=CARD_BG)

    # Labels
    style.configure("TLabel", background=BG_COLOR, font=FONT_BODY, foreground=TEXT_COLOR)
    style.configure("Header.TLabel", background=HEADER_BG, foreground=HEADER_FG, font=FONT_TITLE, padding=12)
    style.configure("Card.TLabel", background=CARD_BG, font=FONT_BODY, foreground=TEXT_COLOR)
    style.configure("CardTitle.TLabel", background=CARD_BG, font=FONT_HEADING, foreground=TEXT_COLOR)
    style.configure("Muted.TLabel", background=CARD_BG, font=FONT_SMALL, foreground=TEXT_MUTED)

    # Buttons
    style.configure("TButton", font=FONT_BODY, padding=5)
    style.map("TButton",
        background=[('active', ACCENT_HOVER), ('!disabled', ACCENT)],
        foreground=[('!disabled', 'white')]
    )
    style.configure("Success.TButton", font=FONT_BODY, padding=5)
    style.map("Success.TButton",
        background=[('active', '#229954'), ('!disabled', SUCCESS)],
        foreground=[('!disabled', 'white')]
    )
    style.configure("Danger.TButton", font=FONT_BODY, padding=5)
    style.map("Danger.TButton",
        background=[('active', '#c0392b'), ('!disabled', DANGER)],
        foreground=[('!disabled', 'white')]
    )

    # Notebook (Tabs)
    style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
    style.configure("TNotebook.Tab",
        background="#bdc3c7",
        foreground=TEXT_COLOR,
        padding=[16, 8],
        font=FONT_TAB)
    style.map("TNotebook.Tab",
        background=[('selected', ACCENT)],
        foreground=[('selected', 'white')])

    # Treeview
    style.configure("Treeview",
        background="white",
        fieldbackground="white",
        foreground=TEXT_COLOR,
        font=FONT_BODY,
        rowheight=28)
    style.configure("Treeview.Heading",
        font=(FONT_FAMILY, 10, "bold"),
        background=HEADER_BG,
        foreground=HEADER_FG)
    style.map("Treeview.Heading",
        background=[('active', ACCENT)])
    style.map("Treeview",
        background=[('selected', ACCENT)],
        foreground=[('selected', 'white')])

    # LabelFrame
    style.configure("TLabelframe", background=BG_COLOR)
    style.configure("TLabelframe.Label", background=BG_COLOR, font=FONT_HEADING, foreground=ACCENT)

    # Radiobutton
    style.configure("TRadiobutton", background=CARD_BG, font=FONT_BODY, foreground=TEXT_COLOR)

    # Entry
    style.configure("TEntry", font=FONT_BODY)


# ══════════════════════════════════════════════
#              VISTA: REGISTRO
# ══════════════════════════════════════════════

class RegistroView(ttk.Frame):
    """Pestaña de registro de productos"""

    def __init__(self, parent, service, on_producto_registrado=None):
        super().__init__(parent)
        self.service = service
        self.on_producto_registrado = on_producto_registrado

        # Variables de control
        self.var_nombre = tk.StringVar()
        self.var_codigo = tk.StringVar()
        self.var_tipo_producto = tk.IntVar(value=1)
        self.var_tipo_flete = tk.IntVar(value=1)
        self.var_cantidad = tk.StringVar()
        self.var_costo = tk.StringVar()

        self._crear_widgets()

    def _crear_widgets(self):
        # Layout: PanedWindow (form izquierda, preview derecha)
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Panel Izquierdo: Formulario ---
        frame_form = ttk.LabelFrame(paned, text="Datos del Producto")
        paned.add(frame_form, weight=2)

        # Campos del formulario
        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=8, pady=8)
        ttk.Entry(frame_form, textvariable=self.var_nombre, width=35).grid(row=0, column=1, sticky=tk.EW, padx=8, pady=8)

        ttk.Label(frame_form, text="Código:").grid(row=1, column=0, sticky=tk.W, padx=8, pady=8)
        ttk.Entry(frame_form, textvariable=self.var_codigo, width=35).grid(row=1, column=1, sticky=tk.EW, padx=8, pady=8)

        ttk.Label(frame_form, text="Tipo de Producto:").grid(row=2, column=0, sticky=tk.W, padx=8, pady=8)
        tipo_frame = ttk.Frame(frame_form)
        tipo_frame.grid(row=2, column=1, sticky=tk.W, padx=8, pady=8)
        ttk.Radiobutton(tipo_frame, text="Servicio", variable=self.var_tipo_producto, value=1).pack(side=tk.LEFT, padx=(0, 15))
        ttk.Radiobutton(tipo_frame, text="Físico", variable=self.var_tipo_producto, value=2).pack(side=tk.LEFT)

        ttk.Label(frame_form, text="Tipo de Flete:").grid(row=3, column=0, sticky=tk.W, padx=8, pady=8)
        flete_frame = ttk.Frame(frame_form)
        flete_frame.grid(row=3, column=1, sticky=tk.W, padx=8, pady=8)
        ttk.Radiobutton(flete_frame, text="Nacional", variable=self.var_tipo_flete, value=1).pack(side=tk.LEFT, padx=(0, 15))
        ttk.Radiobutton(flete_frame, text="Internacional", variable=self.var_tipo_flete, value=2).pack(side=tk.LEFT)

        ttk.Label(frame_form, text="Cantidad:").grid(row=4, column=0, sticky=tk.W, padx=8, pady=8)
        ttk.Entry(frame_form, textvariable=self.var_cantidad, width=35).grid(row=4, column=1, sticky=tk.EW, padx=8, pady=8)

        ttk.Label(frame_form, text="Costo sin IVA:").grid(row=5, column=0, sticky=tk.W, padx=8, pady=8)
        ttk.Entry(frame_form, textvariable=self.var_costo, width=35).grid(row=5, column=1, sticky=tk.EW, padx=8, pady=8)

        # Botones
        frame_btns = ttk.Frame(frame_form)
        frame_btns.grid(row=6, column=0, columnspan=2, pady=20)

        ttk.Button(frame_btns, text="Guardar", command=self._registrar, style="Success.TButton").pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_btns, text="Limpiar", command=self._limpiar).pack(side=tk.LEFT, padx=5)

        frame_form.columnconfigure(1, weight=1)

        # --- Panel Derecho: Preview del último registro ---
        frame_preview = ttk.LabelFrame(paned, text="Vista Previa")
        paned.add(frame_preview, weight=1)

        self.preview_text = tk.Text(frame_preview, wrap=tk.WORD, state=tk.DISABLED,
                                    bg=CARD_BG, fg=TEXT_COLOR, font=FONT_BODY,
                                    relief=tk.FLAT, padx=15, pady=15)
        self.preview_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Mostrar mensaje inicial
        self._mostrar_preview("Registre un producto para ver\nla vista previa de los cálculos\naquí.")

    def _mostrar_preview(self, texto):
        self.preview_text.config(state=tk.NORMAL)
        self.preview_text.delete("1.0", tk.END)
        self.preview_text.insert("1.0", texto)
        self.preview_text.config(state=tk.DISABLED)

    def _registrar(self):
        try:
            nombre = self.var_nombre.get().strip()
            if not nombre:
                messagebox.showerror("Error", "El nombre es obligatorio")
                return

            codigo = int(self.var_codigo.get())
            cantidad = int(self.var_cantidad.get())
            costo = float(self.var_costo.get())

            if cantidad <= 0 or costo <= 0:
                messagebox.showerror("Error", "Cantidad y costo deben ser mayores a 0")
                return

            producto = self.service.registrar_producto(
                nombre=nombre,
                codigo=codigo,
                tipo_producto=self.var_tipo_producto.get(),
                tipo_flete=self.var_tipo_flete.get(),
                cantidad=cantidad,
                costo_sin_iva=costo
            )

            # Mostrar preview
            tipo_prod = "Servicio" if producto.tipo_producto == 1 else "Físico"
            tipo_flete = "Nacional" if producto.tipo_flete == 1 else "Internacional"
            preview = (
                f"═══ PRODUCTO REGISTRADO ═══\n\n"
                f"  Nombre:     {producto.nombre}\n"
                f"  Código:     {producto.codigo}\n"
                f"  Tipo:       {tipo_prod}\n"
                f"  Flete:      {tipo_flete}\n"
                f"  Cantidad:   {producto.cantidad}\n\n"
                f"═══ CÁLCULOS ═══\n\n"
                f"  Costo unitario:   ${producto.calcular_costo_final_unitario():,.0f}\n"
                f"  Precio venta:     ${producto.calcular_precio_venta_unitario():,.0f}\n"
                f"  Total lote:       ${producto.calcular_costo_total_lote():,.0f}\n"
                f"  Ganancia total:   ${producto.calcular_ganancia_total_lote():,.0f}\n"
            )
            self._mostrar_preview(preview)

            # Notificar para actualizar otras pestañas
            if self.on_producto_registrado:
                self.on_producto_registrado()

            self._limpiar()
            messagebox.showinfo("Éxito", f"Producto '{nombre}' registrado correctamente")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para código, cantidad y costo")
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar: {str(e)}")

    def _limpiar(self):
        self.var_nombre.set("")
        self.var_codigo.set("")
        self.var_cantidad.set("")
        self.var_costo.set("")
        self.var_tipo_producto.set(1)
        self.var_tipo_flete.set(1)


# ══════════════════════════════════════════════
#             VISTA: INVENTARIO
# ══════════════════════════════════════════════

class InventarioView(ttk.Frame):
    """Pestaña de inventario con tabla de productos"""

    def __init__(self, parent, service):
        super().__init__(parent)
        self.service = service
        self._crear_widgets()
        self.cargar_datos()

    def _crear_widgets(self):
        # Frame principal
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame de la tabla
        frame_table = ttk.LabelFrame(container, text="Lista de Productos")
        frame_table.pack(fill=tk.BOTH, expand=True)

        # Columnas
        columns = ("nombre", "codigo", "tipo", "flete", "cantidad", "costo_unit", "precio_venta", "total")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings", selectmode="browse")

        headers =  ["Nombre", "Código", "Tipo", "Flete", "Cantidad", "Costo Unit.", "Precio Venta", "Total Lote"]
        widths =   [200,       80,       100,    120,      80,         120,           120,             130]
        anchors =  [tk.W,      tk.CENTER, tk.CENTER, tk.CENTER, tk.CENTER, tk.E, tk.E, tk.E]

        for col, header, width, anchor in zip(columns, headers, widths, anchors):
            self.tree.heading(col, text=header)
            self.tree.column(col, width=width, anchor=anchor)

        # Scrollbars
        scroll_y = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scroll_y.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Alternar colores de filas
        self.tree.tag_configure('odd', background='#ecf0f1')
        self.tree.tag_configure('even', background='white')

    def cargar_datos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        productos = self.service.obtener_todos_productos()
        for idx, p in enumerate(productos):
            tipo = "Servicio" if p.tipo_producto == 1 else "Físico"
            flete = "Nacional" if p.tipo_flete == 1 else "Internacional"
            tag = 'even' if idx % 2 == 0 else 'odd'

            self.tree.insert("", tk.END, values=(
                p.nombre,
                p.codigo,
                tipo,
                flete,
                p.cantidad,
                f"${p.calcular_costo_final_unitario():,.0f}",
                f"${p.calcular_precio_venta_unitario():,.0f}",
                f"${p.calcular_costo_total_lote():,.0f}"
            ), tags=(tag,))


# ══════════════════════════════════════════════
#              VISTA: RESUMEN
# ══════════════════════════════════════════════

class ResumenView(ttk.Frame):
    """Pestaña de resumen con KPIs y tabla de desglose"""

    def __init__(self, parent, service):
        super().__init__(parent)
        self.service = service
        self.labels_valor = {}
        self._crear_widgets()
        self.actualizar()

    def _crear_widgets(self):
        # PanedWindow vertical (KPIs arriba, tabla abajo)
        paned = ttk.PanedWindow(self, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Panel Superior: KPIs ---
        frame_kpis = ttk.LabelFrame(paned, text="Indicadores Clave")
        paned.add(frame_kpis, weight=1)

        # Grid de KPIs (2 filas x 3 columnas)
        kpi_defs = [
            ("total_costo",     "Costo Total",      ACCENT),
            ("total_ganancia",  "Ganancia Total",    SUCCESS),
            ("total_venta",     "Venta Total",       PURPLE),
            ("total_fletes",    "Fletes Total",      WARNING),
            ("total_sin_flete", "Costo sin Flete",   HEADER_BG),
            ("num_productos",   "Total Productos",   DANGER),
        ]

        for i, (key, titulo, color) in enumerate(kpi_defs):
            row, col = divmod(i, 3)
            kpi = self._crear_kpi(frame_kpis, titulo, "$0", color)
            kpi.grid(row=row, column=col, padx=8, pady=8, sticky=(tk.W, tk.E, tk.N, tk.S))

        for c in range(3):
            frame_kpis.columnconfigure(c, weight=1)
        for r in range(2):
            frame_kpis.rowconfigure(r, weight=1)

        # --- Panel Inferior: Tabla de desglose por producto ---
        frame_desglose = ttk.LabelFrame(paned, text="Desglose por Producto")
        paned.add(frame_desglose, weight=1)

        columns = ("nombre", "costo_lote", "ganancia", "fletes", "venta_total")
        self.tree_desglose = ttk.Treeview(frame_desglose, columns=columns,
                                          show="headings", selectmode="browse")

        headers = ["Producto", "Costo Lote", "Ganancia", "Fletes", "Venta Total"]
        widths  = [250, 150, 150, 130, 150]

        for col, header, width in zip(columns, headers, widths):
            self.tree_desglose.heading(col, text=header)
            anchor = tk.W if col == "nombre" else tk.E
            self.tree_desglose.column(col, width=width, anchor=anchor)

        scroll_y = ttk.Scrollbar(frame_desglose, orient=tk.VERTICAL,
                                 command=self.tree_desglose.yview)
        self.tree_desglose.configure(yscroll=scroll_y.set)

        self.tree_desglose.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree_desglose.tag_configure('odd', background='#ecf0f1')
        self.tree_desglose.tag_configure('even', background='white')

    def _crear_kpi(self, parent, titulo, valor, color):
        """Crea un indicador KPI con estilo profesional"""
        # Frame contenedor con borde sutil
        kpi = tk.Frame(parent, bg=CARD_BG, relief=tk.FLAT, bd=0)

        # Barra de color lateral izquierda
        barra = tk.Frame(kpi, bg=color, width=5)
        barra.pack(side=tk.LEFT, fill=tk.Y)

        # Contenido
        contenido = tk.Frame(kpi, bg=CARD_BG)
        contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=12)

        # Título del KPI
        lbl_titulo = tk.Label(contenido, text=titulo.upper(),
                             font=(FONT_FAMILY, 8, "bold"),
                             bg=CARD_BG, fg=TEXT_MUTED, anchor=tk.W)
        lbl_titulo.pack(fill=tk.X)

        # Valor del KPI
        lbl_valor = tk.Label(contenido, text=valor,
                            font=(FONT_FAMILY, 18, "bold"),
                            bg=CARD_BG, fg=color, anchor=tk.W)
        lbl_valor.pack(fill=tk.X, pady=(4, 0))

        # Guardar referencia al label de valor
        self.labels_valor[titulo] = lbl_valor

        return kpi

    def actualizar(self):
        resumen = self.service.obtener_resumen_global()
        productos = self.service.obtener_todos_productos()

        # Actualizar KPIs
        kpi_datos = {
            "Costo Total":      f"${resumen['total_costo']:,.0f}",
            "Ganancia Total":    f"${resumen['total_ganancia']:,.0f}",
            "Venta Total":       f"${resumen['total_venta']:,.0f}",
            "Fletes Total":      f"${resumen['total_fletes']:,.0f}",
            "Costo sin Flete":   f"${resumen['total_costo_sin_flete']:,.0f}",
            "Total Productos":   str(len(productos)),
        }

        for titulo, valor in kpi_datos.items():
            if titulo in self.labels_valor:
                self.labels_valor[titulo].config(text=valor)

        # Actualizar tabla de desglose
        for item in self.tree_desglose.get_children():
            self.tree_desglose.delete(item)

        for idx, p in enumerate(productos):
            tag = 'even' if idx % 2 == 0 else 'odd'
            self.tree_desglose.insert("", tk.END, values=(
                p.nombre,
                f"${p.calcular_costo_total_lote():,.0f}",
                f"${p.calcular_ganancia_total_lote():,.0f}",
                f"${p.calcular_flete_total_lote():,.0f}",
                f"${p.calcular_venta_total_lote():,.0f}"
            ), tags=(tag,))


# ══════════════════════════════════════════════
#            VENTANA PRINCIPAL
# ══════════════════════════════════════════════

class CloudataGUI:
    """Ventana principal de la aplicación GUI de Cloudata"""

    def __init__(self, service=None):
        self.service = service if service else InventarioService()

        self.root = tk.Tk()
        self.root.title("Sistema de Inventario Cloudata SAS")
        self.root.geometry("1280x720")
        self.root.minsize(900, 600)
        self.root.resizable(True, True)

        # Aplicar estilos
        aplicar_estilos(self.root)

        # Contenedor principal
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Header (barra oscura)
        header = ttk.Label(main_container,
                          text="SISTEMA DE INVENTARIO CLOUDATA SAS",
                          style="Header.TLabel",
                          anchor="center")
        header.pack(fill=tk.X, pady=(0, 10))

        # Notebook (pestañas)
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestañas
        self.tab_registro = RegistroView(self.notebook, self.service,
                                         on_producto_registrado=self._on_producto_registrado)
        self.tab_inventario = InventarioView(self.notebook, self.service)
        self.tab_resumen = ResumenView(self.notebook, self.service)

        self.notebook.add(self.tab_registro,   text=" Registro ")
        self.notebook.add(self.tab_inventario, text=" Inventario ")
        self.notebook.add(self.tab_resumen,    text=" Resumen ")

        # Status bar
        self.status_var = tk.StringVar(value="Listo")
        status_bar = ttk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _on_producto_registrado(self):
        """Actualiza las pestañas de inventario y resumen"""
        self.tab_inventario.cargar_datos()
        self.tab_resumen.actualizar()
        self.status_var.set("Producto registrado exitosamente")

    def cerrar(self):
        self.root.destroy()

    def ejecutar(self):
        self.root.mainloop()
