import tkinter as tk
from tkinter import ttk

def aplicar_estilos(root):
    """
    Configura los estilos globales de la aplicación Tkinter.
    """
    style = ttk.Style(root)
    # Usar tema 'clam' o 'alt' que suelen ser más configurables y modernos que 'default'
    try:
        style.theme_use('clam')
    except:
        pass

    # Colores
    BG_COLOR = "#f0f0f0"
    HEADER_BG = "#2c3e50"
    HEADER_FG = "#ecf0f1"
    BUTTON_BG = "#3498db"
    BUTTON_FG = "white"
    
    root.configure(bg=BG_COLOR)

    # Estilo para Frames
    style.configure("TFrame", background=BG_COLOR)
    
    # Estilo para Labels
    style.configure("TLabel", background=BG_COLOR, font=("Helvetica", 10))
    style.configure("Header.TLabel", background=HEADER_BG, foreground=HEADER_FG, font=("Helvetica", 14, "bold"), padding=10)
    
    # Estilo para Botones
    style.configure("TButton", font=("Helvetica", 10), padding=5)
    style.map("TButton",
        background=[('active', '#2980b9'), ('!disabled', BUTTON_BG)],
        foreground=[('!disabled', BUTTON_FG)]
    )
    
    # Estilo para Treeview (Tablas)
    style.configure("Treeview", 
        background="white",
        fieldbackground="white",
        font=("Helvetica", 10),
        rowheight=25
    )
    style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
