from datetime import datetime


class Venta:
    contador = 1
    
    def __init__(self, cliente, productos=[]):
        self.numero = Venta.contador
        Venta.contador = Venta.contador + 1
        self.cliente = cliente
        self.productos = productos
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.estado = "pendiente"

    def agregar_producto(self, producto, cantidad, precio_unitario):
        if not producto.hay_suficiente_stock(cantidad):
            print(f"⚠ Sin stock suficiente para {producto.nombre}")
            return False
        
        producto.actualizar_stock(-cantidad)
        self.productos.append((producto, cantidad, precio_unitario))
        return True

    def calcular_total(self):
        total = 0
        for producto, cantidad, precio_unitario in self.productos:
            total = total + (cantidad * precio_unitario)
        return total

    def mostrar_resumen(self):
        total = self.calcular_total()
        print(f"\n--- Venta #{self.numero} ---")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Fecha: {self.fecha}")
        for producto, cantidad, precio_unitario in self.productos:
            print(f"  {producto.nombre} x {cantidad} - $ {precio_unitario:,.0f} = $ {cantidad * precio_unitario:,.0f}")
        print(f"TOTAL: $ {total:,.0f}")

    def __str__(self):
        total = self.calcular_total()
        return f"Venta #{self.numero} | Cliente: {self.cliente.nombre} | Total: $ {total:,.0f} | Fecha: {self.fecha}"
