class CuentaPUC:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"PUC[{self.codigo}] - {self.nombre}"

PUC_TIENDA_BARRIO = {
    "1435": "Mercancías no fabricadas por la empresa",
    "1455": "Materiales, repuestos y accesorios",
    "1460": "Envases y empaques",
    "1465": "Inventarios en tránsito",
    "1499": "Provisiones para inventarios",
    "1105": "Caja general",
    "1110": "Bancos",
    "1305": "Clientes",
    "2205": "Proveedores nacionales",
    "4135": "Ventas de mercancías",
    "6135": "Costo de ventas - Comercio al por mayor y al por menor",
    "6205": "Compras de mercancías",
    "5105": "Gastos de administración",
    "5110": "Gastos de ventas",
    "5195": "Gastos diversos",
    "2408": "Impuestos, gravámenes y tasas",
    "2365": "Retenciones y descuentos",
}

SUGERENCIAS_PUC = {
    "mercancia": "1435",
    "producto": "1435",
    "articulo": "1435",
    "bebida": "1435",
    "gaseosa": "1435",
    "cerveza": "1435",
    "cigarrillo": "1435",
    "pan": "1435",
    "leche": "1435",
    "arroz": "1435",
    "azucar": "1435",
    "aceite": "1435",
    "harina": "1435",
    "detergente": "1435",
    "jabon": "1435",
    "shampoo": "1435",
    "pasta": "1435",
    "galletas": "1435",
    "confite": "1435",
    "dulce": "1435",
    "papel": "1435",
    "bolsa": "1435",
    "caja": "1460",
    "botella": "1460",
    "envase": "1460",
    "mueble": "1516",
    "equipo": "1512",
}

def sugerir_cuenta(descripcion, categoria=""):
    texto = (descripcion + " " + categoria).lower().strip()
    for palabra, cuenta in SUGERENCIAS_PUC.items():
        if palabra in texto:
            nombre = PUC_TIENDA_BARRIO.get(cuenta, "Cuenta no encontrada")
            return {
                "cuenta": cuenta,
                "nombre": nombre,
                "confianza": "Alta"
            }
    return {
        "cuenta": "1435",
        "nombre": "Mercancías no fabricadas por la empresa",
        "confianza": "Alta (por defecto)"
    }


def buscar_cuenta(cuentas, termino):
    termino = termino.lower().strip()
    resultados = []
    for cuenta in cuentas:
        if termino in cuenta.codigo.lower() or termino in cuenta.nombre.lower():
            resultados.append(cuenta)
    return resultados
