import json
from pathlib import Path
from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        
        print("\n--- INVENTARIO ---")
        for producto in self.productos:
            producto.mostrar_info()
            if producto.cantidad_en_stock <= producto.stock_minimo:
                print(f"  ⚠ STOCK BAJO")

    def __str__(self):
        return f"Inventario con {len(self.productos)} productos"


def guardar_inventario(lista_productos, ruta):
    productos_dict = []
    for producto in lista_productos:
        producto_data = {
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "cantidad_en_stock": producto.cantidad_en_stock,
            "stock_minimo": producto.stock_minimo
        }
        productos_dict.append(producto_data)
    
    ruta_path = Path(ruta)
    with open(ruta_path, 'w') as archivo:
        json.dump(productos_dict, archivo, indent=4)
    print(f"✓ Inventario guardado en {ruta}")


def cargar_inventario(ruta):
    ruta_path = Path(ruta)
    if not ruta_path.exists():
        print(f"No se encontró el archivo {ruta}. Retornando lista vacía.")
        return []
    
    with open(ruta_path, 'r') as archivo:
        productos_dict = json.load(archivo)
    
    productos_lista = []
    for producto_data in productos_dict:
        producto = Producto(
            producto_data["codigo"],
            producto_data["nombre"],
            producto_data["precio"],
            producto_data["cantidad_en_stock"],
            producto_data["stock_minimo"]
        )
        productos_lista.append(producto)
    
    print(f"✓ {len(productos_lista)} productos cargados desde {ruta}")
    return productos_lista
