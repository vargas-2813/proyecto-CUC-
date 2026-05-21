class Producto:
    def __init__(self, codigo, nombre, precio, cantidad_en_stock, stock_minimo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock
        self.stock_minimo = stock_minimo

    def mostrar_info(self):
        print(f"[{self.codigo}] {self.nombre} - $ {self.precio:,.0f} (Stock: {self.cantidad_en_stock})")

    def actualizar_stock(self, cantidad):
        self.cantidad_en_stock = self.cantidad_en_stock + cantidad

    def hay_suficiente_stock(self, cantidad_pedida):
        if cantidad_pedida <= self.cantidad_en_stock:
            return True
        else:
            return False

    def __str__(self):
        return f"Producto[{self.codigo}] - {self.nombre} - $ {self.precio:,.0f}"
