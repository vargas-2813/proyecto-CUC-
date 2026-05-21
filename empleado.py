class Empleado:
    def __init__(self, nombre, identificacion, salario):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__salario = salario

    def nombre(self):
        return self.__nombre

    def identificacion(self):
        return self.__identificacion

    def salario(self):
        return self.__salario

    def __str__(self):
        return f"Empleado[{self.__identificacion}] - {self.__nombre}"


class Cajero(Empleado):
    def __init__(self, nombre, identificacion, salario):
        super().__init__(nombre, identificacion, salario)

    def registrar_venta(self, venta):
        venta.mostrar_resumen()
        print(f"\nVenta registrada por: {self.nombre()}")
