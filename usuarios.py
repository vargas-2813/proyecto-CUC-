import json
from pathlib import Path
from datetime import datetime


def registrar_acceso(username, accion):
    ruta = Path.cwd() / "accesos.json"
    
    acceso_data = {
        "usuario": username,
        "accion": accion,
        "fecha_hora": datetime.now().isoformat()
    }
    
    accesos = []
    if ruta.exists():
        with open(ruta, 'r') as archivo:
            accesos = json.load(archivo)
    
    accesos.append(acceso_data)
    
    with open(ruta, 'w') as archivo:
        json.dump(accesos, archivo, indent=4)


def guardar_usuario(username, password):
    ruta = Path.cwd() / "usuarios.json"
    
    usuarios = []
    if ruta.exists():
        with open(ruta, 'r') as archivo:
            usuarios = json.load(archivo)
    
    usuario_data = {
        "username": username,
        "password": password
    }
    usuarios.append(usuario_data)
    
    with open(ruta, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)
    
    print(f"✓ Usuario {username} registrado")
    registrar_acceso(username, "registro")


def login_usuario(username, password):
    ruta = Path.cwd() / "usuarios.json"
    
    if not ruta.exists():
        print("⚠ No hay usuarios registrados.")
        return False
    
    with open(ruta, 'r') as archivo:
        usuarios = json.load(archivo)
    
    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print(f"✓ Bienvenido {username}")
            registrar_acceso(username, "login")
            return True
    
    print("⚠ Usuario o contraseña incorrectos")
    return False


def exportar_resumen(ruta):
    ruta_path = Path(ruta)
    ruta_accesos = Path.cwd() / "accesos.json"
    
    if not ruta_accesos.exists():
        print("No hay registros de accesos.")
        return
    
    with open(ruta_accesos, 'r') as archivo:
        accesos = json.load(archivo)
    
    with open(ruta_path, 'w') as archivo:
        json.dump(accesos, archivo, indent=4)
    
    print(f"✓ Resumen de accesos guardado en {ruta}")
    
    with open(ruta_path, 'r') as archivo:
        contenido = json.load(archivo)
    
    print(f"✓ Verificación: {len(contenido)} registros guardados correctamente")
