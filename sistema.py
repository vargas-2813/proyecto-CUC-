from empresa import Empresa
from producto import Producto
from cliente import Cliente, guardar_clientes, cargar_clientes
from venta import Venta
from empleado import Empleado, Cajero
from inventario import Inventario, guardar_inventario, cargar_inventario
from puc import CuentaPUC, sugerir_cuenta, buscar_cuenta, PUC_TIENDA_BARRIO
from movimientos import Movimiento, Factura, Proveedor
from usuarios import login_usuario, guardar_usuario, registrar_acceso
from datetime import datetime
from pathlib import Path
import json


empresas = []
clientes = []
empleados = []
usuario_actual = None


def cargar_datos_iniciales():
    """Carga automáticamente usuarios, accesos y empresas guardadas al iniciar"""
    global empresas, clientes
    
    ruta_usuarios = Path.cwd() / "usuarios.json"
    ruta_accesos = Path.cwd() / "accesos.json"
    
    print("\n" + "="*50)
    print("📂 Cargando datos del sistema...")
    print("="*50)
    
    if not ruta_usuarios.exists():
        print("✓ Creando archivo usuarios.json")
        with open(ruta_usuarios, 'w') as f:
            json.dump([], f, indent=4)
    
    if not ruta_accesos.exists():
        print("✓ Creando archivo accesos.json")
        with open(ruta_accesos, 'w') as f:
            json.dump([], f, indent=4)
    
    print("✓ Sistema listo\n")


def autenticar_usuario():
    """Sistema de login y registro de usuario"""
    global usuario_actual
    
    while True:
        print("\n" + "="*50)
        print("        🔐 SISTEMA DE AUTENTICACIÓN")
        print("="*50)
        print("1. Login (Usuario Existente)")
        print("2. Registrarse (Nuevo Usuario)")
        print("3. Salir")
        print("="*50)
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            if login_usuario(username, password):
                usuario_actual = username
                return True
        
        elif opcion == '2':
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            guardar_usuario(username, password)
            usuario_actual = username
            return True
        
        elif opcion == '3':
            registrar_acceso(usuario_actual if usuario_actual else "anonimo", "salida_sin_autenticar")
            print("\n¡Hasta luego!")
            return False
        
        else:
            print("⚠ Opción no válida.")


def menu_persona():
    while True:
        print("\n" + "="*50)
        print("        === MINI SIIGO ===")
        print("="*50)
        print("1. Ver empresas registradas")
        print("2. Registrar nueva empresa")
        print("3. Salir")
        print("="*50)
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            if not empresas:
                print("\n⚠ No hay empresas registradas.")
                continue
            print("\n--- Empresas Registradas ---")
            for idx, e in enumerate(empresas):
                print(f"{idx + 1}. {e}")
            try:
                seleccion = int(input("Seleccione el número de la empresa: "))
                if 1 <= seleccion <= len(empresas):
                    empresa = empresas[seleccion - 1]
                    pwd = input(f"Ingrese la contraseña para {empresa.nombre}: ").strip()
                    if pwd == empresa.password:
                        menu_empresa(empresa)
                    else:
                        print("⚠ Contraseña incorrecta.")
                else:
                    print("⚠ Selección inválida.")
            except ValueError:
                print("⚠ Entrada inválida.")
        
        elif opcion == '2':
            print("\n--- Registrar Nueva Empresa ---")
            nit = input("NIT de la empresa: ").strip()
            nombre = input("Nombre de la empresa: ").strip()
            password = input("Contraseña de la empresa: ").strip()
            empresas.append(Empresa(nit, nombre, password))
            print(f"✓ Empresa {nombre} registrada.")
        
        elif opcion == '3':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("⚠ Opción no válida.")


def menu_empresa(empresa):
    inventario = Inventario()
    clientes = []
    cuentas_puc = [
        CuentaPUC('1435', 'Mercancías no fabricadas por la empresa'),
        CuentaPUC('1105', 'Caja general'),
        CuentaPUC('1305', 'Clientes'),
        CuentaPUC('2205', 'Proveedores nacionales'),
        CuentaPUC('4135', 'Ventas de mercancías'),
        CuentaPUC('6205', 'Compras de mercancías'),
    ]
    ventas_empresa = []
    movimientos_empresa = []
    
    while True:
        print(f"\n{'='*50}")
        print(f"    === MINI SIIGO - {empresa.nombre} ===")
        print(f"{'='*50}")
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Ver cuentas PUC")
        print("4. Agregar cuenta PUC")
        print("5. Registrar venta")
        print("6. Registrar compra")
        print("7. Ver libro de movimientos contables")
        print("8. Reportes")
        print("9. Guardar datos")
        print("10. Cargar datos guardados")
        print("11. Volver al menú de persona")
        print(f"{'='*50}")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            inventario.mostrar_inventario()
        
        elif opcion == '2':
            print("\n--- Agregar Producto ---")
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            
            sugerencia = sugerir_cuenta(nombre)
            print(f"\n💡 Sugerencia automática de cuenta PUC:")
            print(f"   {sugerencia['cuenta']} - {sugerencia['nombre']}")
            print(f"   Confianza: {sugerencia['confianza']}")
            
            usar_sugerencia = input("\n¿Desea usar esta cuenta sugerida? (s/n): ").strip().lower()
            cuenta_asociada = None
            
            if usar_sugerencia == 's':
                cuentas_encontradas = buscar_cuenta(cuentas_puc, sugerencia['nombre'])
                if cuentas_encontradas:
                    cuenta_asociada = cuentas_encontradas[0]
                else:
                    cuenta_asociada = CuentaPUC(sugerencia['cuenta'], sugerencia['nombre'])
                    cuentas_puc.append(cuenta_asociada)
            else:
                print("\n--- Cuentas PUC disponibles ---")
                for idx, c in enumerate(cuentas_puc):
                    print(f"{idx + 1}. {c}")
                seleccion = input("\nSeleccione el número de la cuenta o escriba el código/nombre: ").strip()
                try:
                    idx = int(seleccion) - 1
                    if 0 <= idx < len(cuentas_puc):
                        cuenta_asociada = cuentas_puc[idx]
                except ValueError:
                    cuentas_encontradas = buscar_cuenta(cuentas_puc, seleccion)
                    if cuentas_encontradas:
                        cuenta_asociada = cuentas_encontradas[0]
                
                if cuenta_asociada is None:
                    print("No se encontró la cuenta, usando sugerencia.")
                    cuenta_asociada = CuentaPUC(sugerencia['cuenta'], sugerencia['nombre'])
                    cuentas_puc.append(cuenta_asociada)
            
            while True:
                try:
                    precio = float(input("Precio del producto: ").strip())
                    break
                except ValueError:
                    print("⚠ Precio inválido. Ingrese un número.")
            
            while True:
                try:
                    cantidad = int(input("Cantidad inicial en stock: ").strip())
                    break
                except ValueError:
                    print("⚠ Cantidad inválida. Ingrese un número entero.")
            
            while True:
                try:
                    stock_minimo = int(input("Stock mínimo recomendado: ").strip())
                    break
                except ValueError:
                    print("⚠ Stock mínimo inválido. Ingrese un número entero.")
            
            producto = Producto(codigo, nombre, precio, cantidad, stock_minimo)
            inventario.agregar_producto(producto)
            print(f"✓ Producto {nombre} agregado con cuenta PUC {cuenta_asociada.codigo}")
        
        elif opcion == '3':
            if cuentas_puc:
                print("\n--- Cuentas PUC ---")
                for c in cuentas_puc:
                    print(c)
            else:
                print("\n⚠ No hay cuentas PUC registradas.")
        
        elif opcion == '4':
            print("\n--- Agregar Cuenta PUC ---")
            codigo = input("Código de la cuenta PUC: ").strip()
            nombre = input("Nombre de la cuenta PUC: ").strip()
            cuentas_puc.append(CuentaPUC(codigo, nombre))
            print(f"✓ Cuenta PUC {codigo} agregada.")
        
        elif opcion == '5':
            print("\n--- Registrar Venta ---")
            nombre_cliente = input("Nombre del cliente: ").strip()
            
            if not inventario.productos:
                print("⚠ Inventario Vacío. No se puede vender.")
                input("Presione Enter para continuar...")
                continue
            
            cliente = None
            for c in clientes:
                if c.nombre.lower() == nombre_cliente.lower():
                    cliente = c
                    break
            
            if cliente is None:
                identificacion = input("Identificación del cliente: ").strip()
                telefono = input("Teléfono del cliente: ").strip()
                cliente = Cliente(identificacion, nombre_cliente, telefono)
                clientes.append(cliente)
            
            venta = Venta(cliente, [])
            
            while True:
                print("\n--- Productos disponibles ---")
                for idx, producto in enumerate(inventario.productos):
                    print(f"{idx + 1}. {producto}")
                
                seleccion = input("\nSeleccione producto a vender (número, vacío para terminar): ").strip()
                if seleccion == '':
                    break
                
                try:
                    idx = int(seleccion) - 1
                    if 0 <= idx < len(inventario.productos):
                        producto = inventario.productos[idx]
                        cant = int(input(f"Cantidad a vender de {producto.nombre}: ").strip())
                        
                        if not producto.hay_suficiente_stock(cant):
                            print(f"⚠ Stock Insuficiente para {producto.nombre}")
                            print(f"   Disponible: {producto.cantidad_en_stock} unidades")
                            input("Presione Enter para seleccionar otro producto...")
                            continue
                        
                        precio_venta = float(input(f"Precio de venta por unidad (actual: $ {producto.precio:,.0f}): ").strip())
                        
                        if venta.agregar_producto(producto, cant, precio_venta):
                            print(f"✓ {cant} unidades agregadas a la venta.")
                        else:
                            print(f"⚠ No se pudo agregar {producto.nombre}.")
                    else:
                        print("⚠ Selección inválida.")
                except ValueError:
                    print("⚠ Entrada inválida.")
            
            if venta.productos:
                venta.mostrar_resumen()
                ventas_empresa.append(venta)
                cliente.agregar_compra(venta)
                
                cuentas_caja = buscar_cuenta(cuentas_puc, '1105')
                if cuentas_caja:
                    cuenta_caja = cuentas_caja[0]
                else:
                    cuenta_caja = CuentaPUC('1105', 'Caja general')
                    cuentas_puc.append(cuenta_caja)
                
                cuentas_ventas = buscar_cuenta(cuentas_puc, '4135')
                if cuentas_ventas:
                    cuenta_ventas = cuentas_ventas[0]
                else:
                    cuenta_ventas = CuentaPUC('4135', 'Ventas de mercancías')
                    cuentas_puc.append(cuenta_ventas)
                
                for prod, cant, precio in venta.productos:
                    movimiento = Movimiento(
                        venta.fecha,
                        'venta',
                        prod,
                        cant,
                        precio,
                        cuenta_caja,
                        cuenta_ventas,
                        f"Venta factura #{venta.numero}"
                    )
                    movimientos_empresa.append(movimiento)
                
                print("✓ Venta registrada y movimientos contables creados.")
                input("Presione Enter para continuar...")
        
        
        elif opcion == '6':
            print("\n--- Registrar Compra ---")
            nombre_prov = input("Nombre del proveedor: ").strip()
            nit_prov = input("NIT del proveedor: ").strip()
            
            proveedor = Proveedor(nombre_prov, nit_prov)
            
            compras = []
            total = 0
            
            while True:
                if not inventario.productos:
                    print("⚠ No hay productos disponibles.")
                    break
                
                print("\n--- Productos ---")
                for idx, producto in enumerate(inventario.productos):
                    print(f"{idx + 1}. {producto}")
                
                seleccion = input("\nSeleccione producto a comprar (número, vacío para terminar): ").strip()
                if seleccion == '':
                    break
                
                try:
                    idx = int(seleccion) - 1
                    if 0 <= idx < len(inventario.productos):
                        prod = inventario.productos[idx]
                        cant = int(input(f"Cantidad a comprar de {prod.nombre}: ").strip())
                        precio_compra = float(input(f"Precio de compra por unidad (actual: $ {prod.precio:,.0f}): ").strip())
                        compras.append((prod, cant, precio_compra))
                        prod.actualizar_stock(cant)
                        total = total + (cant * precio_compra)
                    else:
                        print("⚠ Selección inválida.")
                except ValueError:
                    print("⚠ Entrada inválida.")
            
            if compras:
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                
                cuentas_inventario = buscar_cuenta(cuentas_puc, '1435')
                if cuentas_inventario:
                    cuenta_inventario = cuentas_inventario[0]
                else:
                    cuenta_inventario = CuentaPUC('1435', 'Mercancías no fabricadas por la empresa')
                    cuentas_puc.append(cuenta_inventario)
                
                cuentas_compras = buscar_cuenta(cuentas_puc, '6205')
                if cuentas_compras:
                    cuenta_compras = cuentas_compras[0]
                else:
                    cuenta_compras = CuentaPUC('6205', 'Compras de mercancías')
                    cuentas_puc.append(cuenta_compras)
                
                for prod, cant, precio in compras:
                    movimiento = Movimiento(
                        fecha,
                        'compra',
                        prod,
                        cant,
                        precio,
                        cuenta_inventario,
                        cuenta_compras,
                        f"Compra a {proveedor.nombre}"
                    )
                    movimientos_empresa.append(movimiento)
                
                print(f"✓ Compra registrada por $ {total:,.0f} a {proveedor}")
        
        elif opcion == '7':
            if movimientos_empresa:
                print("\n--- Libro de Movimientos Contables ---")
                for mov in movimientos_empresa:
                    print(mov)
            else:
                print("\n⚠ No hay movimientos registrados.")
        
        elif opcion == '8':
            print(f"\n{'='*50}")
            print("           === REPORTES ===")
            print(f"{'='*50}")
            print("1. Balance por cuenta PUC")
            print("2. Resumen de ventas")
            print("3. Estado de inventario")
            print(f"{'='*50}")
            subop = input("Seleccione reporte: ").strip()
            
            if subop == '1':
                saldo = {}
                for mov in movimientos_empresa:
                    if mov.cuenta_debito.codigo not in saldo:
                        saldo[mov.cuenta_debito.codigo] = 0
                    if mov.cuenta_credito.codigo not in saldo:
                        saldo[mov.cuenta_credito.codigo] = 0
                    
                    saldo[mov.cuenta_debito.codigo] = saldo[mov.cuenta_debito.codigo] + (mov.cantidad * mov.valor_unitario)
                    saldo[mov.cuenta_credito.codigo] = saldo[mov.cuenta_credito.codigo] - (mov.cantidad * mov.valor_unitario)
                
                print("\n--- Saldo por Cuenta PUC ---")
                if saldo:
                    for cod, val in saldo.items():
                        cuentas_encontradas = buscar_cuenta(cuentas_puc, cod)
                        nombre = cuentas_encontradas[0].nombre if cuentas_encontradas else cod
                        print(f"{cod} - {nombre}: $ {val:,.0f}")
                else:
                    print("⚠ No hay movimientos registrados.")
                input("\nPresione Enter para volver al menú...")
            
            elif subop == '2':
                print("\n--- Resumen de Ventas ---")
                if ventas_empresa:
                    total_ventas = 0
                    for venta in ventas_empresa:
                        print(venta)
                        total_ventas = total_ventas + venta.calcular_total()
                    print(f"\n{'='*50}")
                    print(f"TOTAL DE VENTAS: $ {total_ventas:,.0f}")
                    print(f"{'='*50}")
                else:
                    print("⚠ No hay ventas registradas.")
                input("\nPresione Enter para volver al menú...")
            
            elif subop == '3':
                print("\n--- Estado de Inventario ---")
                inventario.mostrar_inventario()
                input("\nPresione Enter para volver al menú...")
            
            else:
                print("⚠ Opción inválida.")
        
        
        elif opcion == '9':
            ruta_productos = Path.cwd() / f"productos_{empresa.nombre}.json"
            ruta_clientes = Path.cwd() / f"clientes_{empresa.nombre}.json"
            
            print("\n--- Guardando Datos ---")
            guardar_inventario(inventario.productos, ruta_productos)
            guardar_clientes(clientes, ruta_clientes)
            
            print("\n--- Verificando Integridad ---")
            try:
                with open(ruta_productos, 'r') as f:
                    productos_verificados = json.load(f)
                print(f"✓ {len(productos_verificados)} productos guardados correctamente")
                
                with open(ruta_clientes, 'r') as f:
                    clientes_verificados = json.load(f)
                print(f"✓ {len(clientes_verificados)} clientes guardados correctamente")
                
                print("✓ Datos guardados y verificados en la carpeta actual")
            except Exception as e:
                print(f"⚠ Error al verificar integridad: {e}")
            
            input("Presione Enter para continuar...")
        
        
        elif opcion == '10':
            ruta_productos = Path.cwd() / f"productos_{empresa.nombre}.json"
            ruta_clientes = Path.cwd() / f"clientes_{empresa.nombre}.json"
            
            productos_cargados = cargar_inventario(ruta_productos)
            clientes_cargados = cargar_clientes(ruta_clientes)
            
            inventario.productos = productos_cargados
            clientes = clientes_cargados
        
        elif opcion == '11':
            break
        
        else:
            print("⚠ Opción no válida.")


if __name__ == "__main__":
    try:
        cargar_datos_iniciales()
        if autenticar_usuario():
            menu_persona()
    except KeyboardInterrupt:
        print("\n\n¡Ejecución interrumpida. ¡Hasta luego!")
