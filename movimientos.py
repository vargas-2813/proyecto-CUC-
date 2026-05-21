class Movimiento:
    def __init__(self, fecha, tipo, producto, cantidad, valor_unitario, cuenta_debito, cuenta_credito, descripcion=""):
        self.fecha = fecha
        self.tipo = tipo  # 'venta' o 'compra'
        self.producto = producto
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario
        self.cuenta_debito = cuenta_debito
        self.cuenta_credito = cuenta_credito
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.fecha} | {self.tipo.upper()} | {self.producto.nombre} x{self.cantidad} | ${self.valor_unitario} | Debe: {self.cuenta_debito.codigo} | Haber: {self.cuenta_credito.codigo} | {self.descripcion}"

class Factura:
    contador = 1
    def __init__(self, cliente, productos_vendidos, total, fecha):
        self.numero = Factura.contador
        Factura.contador += 1
        self.cliente = cliente
        self.productos_vendidos = productos_vendidos  # lista de tuplas (Producto, cantidad, precio_unitario)
        self.total = total
        self.fecha = fecha

    def __str__(self):
        return f"Factura #{self.numero} | Cliente: {self.cliente} | Total: ${self.total} | Fecha: {self.fecha}"

class Proveedor:
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit
    def __str__(self):
        return f"Proveedor[{self.nit}] - {self.nombre}"
