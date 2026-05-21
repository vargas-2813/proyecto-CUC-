import json
from pathlib import Path


class Cliente:
    def __init__(self, identificacion, nombre, telefono):
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.historial_compras = []

    def agregar_compra(self, venta):
        self.historial_compras.append(venta)

    def mostrar_historial(self):
        if not self.historial_compras:
            print(f"El cliente {self.nombre} no tiene compras registradas.")
            return
        print(f"\n--- Historial de {self.nombre} ---")
        for venta in self.historial_compras:
            print(venta)

    def __str__(self):
        return f"Cliente[{self.identificacion}] - {self.nombre} - Tel: {self.telefono}"


def guardar_clientes(lista_clientes, ruta):
    clientes_dict = []
    for cliente in lista_clientes:
        cliente_data = {
            "identificacion": cliente.identificacion,
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "historial_compras": []
        }
        clientes_dict.append(cliente_data)
    
    ruta_path = Path(ruta)
    with open(ruta_path, 'w') as archivo:
        json.dump(clientes_dict, archivo, indent=4)
    print(f"✓ Clientes guardados en {ruta}")


def cargar_clientes(ruta):
    ruta_path = Path(ruta)
    if not ruta_path.exists():
        print(f"No se encontró el archivo {ruta}. Retornando lista vacía.")
        return []
    
    with open(ruta_path, 'r') as archivo:
        clientes_dict = json.load(archivo)
    
    clientes_lista = []
    for cliente_data in clientes_dict:
        cliente = Cliente(
            cliente_data["identificacion"],
            cliente_data["nombre"],
            cliente_data["telefono"]
        )
        clientes_lista.append(cliente)
    
    print(f"✓ {len(clientes_lista)} clientes cargados desde {ruta}")
    return clientes_lista

