"""
Data Seeder para el Sistema de Inventario Cloudata
Limpia y puebla la base de datos con datos de ejemplo
"""

import json
import os

# Ruta al archivo JSON dentro de cloudata_app/
ARCHIVO_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "productos.json")

def limpiar_y_seedear():
    """Limpia el archivo JSON y lo puebla con datos de ejemplo"""
    
    productos_ejemplo = [
        {
            "nombre": "Laptop Dell XPS 13",
            "codigo": 1001,
            "tipo_producto": 2,
            "tipo_flete": 2,
            "cantidad": 15,
            "costo_sin_iva": 3500000
        },
        {
            "nombre": "Servicio de Consultoría IT",
            "codigo": 2001,
            "tipo_producto": 1,
            "tipo_flete": 1,
            "cantidad": 5,
            "costo_sin_iva": 2000000
        },
        {
            "nombre": "Mouse Logitech MX Master 3",
            "codigo": 1002,
            "tipo_producto": 2,
            "tipo_flete": 2,
            "cantidad": 50,
            "costo_sin_iva": 150000
        },
        {
            "nombre": "Teclado Mecánico Keychron K2",
            "codigo": 1003,
            "tipo_producto": 2,
            "tipo_flete": 2,
            "cantidad": 30,
            "costo_sin_iva": 250000
        },
        {
            "nombre": "Monitor Samsung 27\" 4K",
            "codigo": 1004,
            "tipo_producto": 2,
            "tipo_flete": 1,
            "cantidad": 20,
            "costo_sin_iva": 1200000
        },
        {
            "nombre": "Servicio de Mantenimiento Anual",
            "codigo": 2002,
            "tipo_producto": 1,
            "tipo_flete": 1,
            "cantidad": 10,
            "costo_sin_iva": 500000
        },
        {
            "nombre": "Auriculares Sony WH-1000XM5",
            "codigo": 1005,
            "tipo_producto": 2,
            "tipo_flete": 2,
            "cantidad": 25,
            "costo_sin_iva": 800000
        },
        {
            "nombre": "Webcam Logitech Brio 4K",
            "codigo": 1006,
            "tipo_producto": 2,
            "tipo_flete": 2,
            "cantidad": 40,
            "costo_sin_iva": 450000
        },
        {
            "nombre": "Servicio de Soporte Técnico",
            "codigo": 2003,
            "tipo_producto": 1,
            "tipo_flete": 1,
            "cantidad": 8,
            "costo_sin_iva": 300000
        },
        {
            "nombre": "Escritorio Eléctrico Ajustable",
            "codigo": 1007,
            "tipo_producto": 2,
            "tipo_flete": 1,
            "cantidad": 12,
            "costo_sin_iva": 1500000
        }
    ]
    
    try:
        with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
            json.dump(productos_ejemplo, f, indent=4, ensure_ascii=False)
        
        print(f"✓ Datos de ejemplo generados exitosamente")
        print(f"✓ Ruta: {ARCHIVO_DB}")
        print(f"✓ Total de productos: {len(productos_ejemplo)}")
        
    except Exception as e:
        print(f"✗ Error al crear el seeder: {e}")

if __name__ == "__main__":
    print("╔════════════════════════════════════════════════╗")
    print("║   SEEDER - INVENTARIO CLOUDATA SAS             ║")
    print("╚════════════════════════════════════════════════╝")
    print()
    limpiar_y_seedear()
    print()
    input("Presiona Enter para continuar...")
