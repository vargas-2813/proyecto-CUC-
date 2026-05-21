class Empresa:
    def __init__(self, id_empresa, nombre, password):
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.password = password

    def __str__(self):
        return f"Empresa[{self.id_empresa}] - {self.nombre}"
