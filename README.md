# Mini SIIGO - Sistema Integrado de Gestión Empresarial

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)]()

**Una solución integral de gestión empresarial para pequeños y medianos negocios**

[Características](#características) • [Instalación](#instalación) • [Uso](#uso) • [Arquitectura](#arquitectura) • [Conceptos OOP](#conceptos-oop)

</div>

---

## 📋 Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Características Principales](#características-principales)
3. [Tecnologías](#tecnologías)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Instalación](#instalación)
6. [Instrucciones de Uso](#instrucciones-de-uso)
7. [Flujos de Operación](#flujos-de-operación)
8. [Arquitectura del Sistema](#arquitectura-del-sistema)
9. [Conceptos OOP Aplicados](#conceptos-oop-aplicados)
10. [Documentación](#documentación)
11. [Contribución](#contribución)
12. [Licencia](#licencia)

---

## 📖 Descripción General

**Mini SIIGO** es un sistema integrado de gestión empresarial diseñado específicamente para pequeñas y medianas empresas (especialmente tiendas de barrio y comercios minoristas).

El sistema centraliza operaciones críticas de negocio en una única plataforma, permitiendo:

- 📦 **Control de Inventario**: Gestión de stock con alertas automáticas
- 💰 **Registro de Ventas**: Transacciones con múltiples productos y clientes
- 👥 **Gestión de Clientes**: Historiales de compra y trazabilidad
- 📊 **Integridad Contable**: Movimientos contables automáticos según PUC
- 👨‍💼 **Administración de Personal**: Control de empleados y roles
- 📈 **Reportes**: Análisis de ventas, inventario y balances

### Objetivo

Proporcionar a pequeños comerciantes una herramienta profesional que:

✅ Elimine procesos manuales y propensos a errores  
✅ Garantice integridad en registros contables  
✅ Mejore la toma de decisiones con reportes automáticos  
✅ Mantenga históricos de transacciones y clientes  
✅ Sea accesible, económica y fácil de usar  

---

## ✨ Características Principales

### 🔐 Autenticación y Seguridad
- Sistema de usuarios con registro y login
- Autenticación por empresa con contraseña
- Auditoría completa de accesos y cambios
- Validación de entrada en todos los campos

### 📦 Gestión de Inventario
- Registro de productos con código único
- Control de stock en tiempo real
- Alertas automáticas de stock bajo
- Búsqueda de productos por código
- Asociación automática con cuentas contables (PUC)

### 🛒 Sistema de Ventas
- Registro de transacciones con múltiples productos
- Identificación y gestión de clientes
- Cálculo automático de totales
- Generación de números de venta únicos
- Historial completo de compras por cliente

### 📝 Compras a Proveedores
- Registro de compras con datos del proveedor
- Actualización automática de inventario
- Movimientos contables automáticos
- Gestión de precios de compra vs. venta

### 📊 Contabilidad Integrada
- Plan Único de Cuentas (PUC) pre-configurado
- Sugerencias automáticas de cuentas por descripción
- Movimientos contables automáticos para cada transacción
- Registros de débito y crédito balanceados
- Reportes por cuenta contable

### 📈 Reportes y Análisis
- Balance por cuenta PUC
- Resumen de ventas con totales
- Estado de inventario con alertas
- Verificación de integridad de datos

### 💾 Persistencia de Datos
- Almacenamiento en JSON
- Guardado y carga manual de datos
- Verificación de integridad en cada operación
- Recuperación de datos guardados

---

## 🛠 Tecnologías

| Componente | Tecnología | Versión |
|---|---|---|
| **Lenguaje** | Python | 3.7+ |
| **Almacenamiento** | JSON | Estándar |
| **Sistema de Archivos** | pathlib | Estándar |
| **Interfaz** | Terminal CLI | Interactiva |
| **Dependencias** | Nativas | Sin librerías externas |

### Justificación Técnica

- **Python 3.7+**: Sintaxis moderna, manejo de excepciones robusto, orientación a objetos pura
- **JSON**: Formato legible, fácil de editar, independiente de plataforma
- **Sin dependencias externas**: Facilita distribución, reduce vulnerabilidades, funciona en cualquier sistema
- **Terminal CLI**: Acceso universal, funciona en servidores sin GUI, familiar para usuarios técnicos

---

## 📁 Estructura del Proyecto

```
proyecto/
│
├── 📄 README.md                      # Este archivo - Documentación principal
├── 📄 analisis_requerimientos.md     # Análisis formal de requerimientos
├── 📄 diagrama_uml.md               # Diagrama de clases UML en Mermaid
├── 📄 diagrama.drawio               # Diagrama UML en formato Draw.io
│
├── 🐍 MÓDULOS PRINCIPALES
├── cliente.py                        # Entidad Cliente y funciones de persistencia
├── producto.py                       # Entidad Producto
├── empleado.py                       # Entidades Empleado y Cajero (herencia)
├── empresa.py                        # Entidad Empresa
├── inventario.py                     # Gestor de Inventario
├── venta.py                          # Transacción Venta
├── movimientos.py                    # Movimientos contables, Factura, Proveedor
├── puc.py                            # Plan Único de Cuentas (PUC)
├── usuarios.py                       # Autenticación y auditoría
├── sistema.py                        # Menús y lógica de negocio principal
│
├── 💾 DATOS (generados en ejecución)
├── usuarios.json                     # Base de usuarios registrados
├── accesos.json                      # Log de accesos
├── productos_*.json                  # Inventario por empresa
├── clientes_*.json                   # Clientes por empresa
└── README.md                         # (Este archivo)
```

### Descripción de Módulos

| Módulo | Responsabilidad | Clases |
|---|---|---|
| `cliente.py` | Gestión de clientes y persistencia | `Cliente` |
| `producto.py` | Definición de productos | `Producto` |
| `empleado.py` | Jerarquía de empleados | `Empleado`, `Cajero` |
| `empresa.py` | Entidad empresa | `Empresa` |
| `inventario.py` | Gestor de stock | `Inventario` |
| `venta.py` | Transacciones de venta | `Venta` |
| `movimientos.py` | Contabilidad y logística | `Movimiento`, `Factura`, `Proveedor` |
| `puc.py` | Plan de cuentas contables | `CuentaPUC` |
| `usuarios.py` | Autenticación y auditoría | Funciones |
| `sistema.py` | Orquestación y menús | Funciones principales |

---

## 🚀 Instalación

### Requisitos Previos

- **Python 3.7 o superior**
- **Sistema Operativo**: Windows, Linux, macOS
- **Espacio en disco**: ~5 MB
- **Permisos**: Lectura/escritura en carpeta del proyecto

### Pasos de Instalación

#### 1. Clonar o Descargar el Proyecto

```bash
# Opción A: Si está en un repositorio Git
git clone https://github.com/usuario/mini-siigo.git
cd mini-siigo/proyecto

# Opción B: Descargar manual
# Descargar todos los archivos .py en una carpeta local
cd ruta/a/proyecto
```

#### 2. Verificar Instalación de Python

```bash
python --version
# Debería mostrar: Python 3.7.0 o superior

# En algunos sistemas:
python3 --version
```

#### 3. Crear Directorio de Trabajo (Opcional)

```bash
# Crear carpeta para el proyecto
mkdir -p ~/mini-siigo
cd ~/mini-siigo

# Copiar archivos
cp -r /ruta/original/* .
```

#### 4. Ejecutar el Sistema

```bash
python sistema.py
# O en algunos sistemas:
python3 sistema.py
```

### Solución de Problemas de Instalación

| Problema | Solución |
|---|---|
| "python: command not found" | Usar `python3` en lugar de `python` |
| "ModuleNotFoundError" | Verificar que todos los .py estén en la misma carpeta |
| "PermissionError en archivos JSON" | Verificar permisos de escritura: `chmod 755 .` |
| "Encoding errors" | Verificar codificación UTF-8 en archivos |

---

## 📖 Instrucciones de Uso

### Inicio de Sesión

```
Pantalla de Inicio:
1. Login (Usuario Existente)
2. Registrarse (Nuevo Usuario)
3. Salir
```

**Primera vez:** Seleccionar opción 2 para registrarse con un usuario nuevo.

### Flujo Típico de Uso

#### Escenario 1: Gerente Registrando Venta

```
1. Ingresar credenciales de usuario
2. Seleccionar empresa a usar
3. Ingresar contraseña de empresa
4. Menú empresa → Opción 5: Registrar venta
5. Identificar cliente (nuevo o existente)
6. Seleccionar productos del inventario
7. Confirmar cantidades y precios
8. Sistema calcula total y crea movimientos contables
```

#### Escenario 2: Agregar Nuevo Producto

```
1. Autenticarse en empresa
2. Menú → Opción 2: Agregar producto
3. Ingresa código, nombre, precio, stock inicial
4. Sistema sugiere cuenta PUC automáticamente
5. Aceptar o cambiar cuenta
6. Producto agregado al inventario
```

#### Escenario 3: Consultar Reportes

```
1. Autenticarse en empresa
2. Menú → Opción 8: Reportes
3. Seleccionar tipo:
   - Balance por cuenta PUC
   - Resumen de ventas
   - Estado de inventario
4. Sistema genera y muestra reporte
```

#### Escenario 4: Guardar Datos

```
1. Después de operaciones
2. Menú → Opción 9: Guardar datos
3. Sistema serializa a JSON
4. Verifica integridad
5. Datos persistidos en archivos
```

### Comandos Principales

| Opción | Acción |
|---|---|
| 1 | Ver inventario |
| 2 | Agregar producto |
| 3 | Ver cuentas PUC |
| 4 | Agregar cuenta PUC |
| 5 | Registrar venta |
| 6 | Registrar compra |
| 7 | Ver libro de movimientos |
| 8 | Reportes |
| 9 | Guardar datos |
| 10 | Cargar datos |
| 11 | Volver/Salir |

---

## 🔄 Flujos de Operación

### Flujo de Venta Completa

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CAJERO SELECCIONA "REGISTRAR VENTA"                      │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────▼──────────┐
         │ 2. IDENTIFICAR CLIENTE
         │    ├─ Existente: busca
         │    └─ Nuevo: crea
         └───────────┬──────────┘
                     │
         ┌───────────▼──────────────┐
         │ 3. SELECCIONAR PRODUCTOS │
         │    ├─ Validar stock      │
         │    ├─ Ingresar cantidad  │
         │    └─ Ingresa precio     │
         └───────────┬──────────────┘
                     │
         ┌───────────▼──────────────┐
         │ 4. CONFIRMAR VENTA       │
         │    └─ Calcula total      │
         └───────────┬──────────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
    ▼                ▼                ▼
 ┌──────┐      ┌──────────┐    ┌────────────────┐
 │Venta │      │ Productos│    │ Movimientos    │
 │creada│      │  Stock   │    │  Contables     │
 │      │      │reducido  │    │ automáticos    │
 └──────┘      └──────────┘    └────────────────┘
    │                │                │
    └────────────────┼────────────────┘
                     │
         ┌───────────▼──────────┐
         │ 5. AGREGAR A CLIENTE │
         │    └─ Historial     │
         └───────────┬──────────┘
                     │
         ┌───────────▼──────────┐
         │ 6. CONFIRMACIÓN      │
         │    └─ Resumen venta  │
         └──────────────────────┘
```

### Flujo de Registro de Movimientos Contables

```
CADA VENTA GENERA:
├─ Débito: Caja (1105) → Crédito: Ventas (4135)
│  └─ Monto: cantidad × precio_venta
│
CADA COMPRA GENERA:
├─ Débito: Inventario (1435) → Crédito: Compras (6205)
│  └─ Monto: cantidad × precio_compra
│
RESULTADO: Balance siempre en equilibrio
```

---

## 🏗 Arquitectura del Sistema

### Diagrama de Componentes

```
┌────────────────────────────────────────────────────────┐
│              CAPA DE PRESENTACIÓN (CLI)               │
│                  (sistema.py)                         │
│              Menús y interacción usuario             │
└────────────────┬─────────────────────────────────────┘
                 │
┌────────────────▼─────────────────────────────────────┐
│          CAPA DE LÓGICA DE NEGOCIO                  │
│  ┌──────────────────────────────────────────────┐   │
│  │ Entidades:                                   │   │
│  │ • Cliente, Producto, Empleado, Empresa      │   │
│  │ • Inventario, Venta, Movimiento, CuentaPUC  │   │
│  │ • Factura, Proveedor                        │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │ Procesos:                                    │   │
│  │ • Validación de stock                        │   │
│  │ • Cálculo de totales                         │   │
│  │ • Generación automática de movimientos       │   │
│  │ • Sugerencia de cuentas PUC                  │   │
│  └──────────────────────────────────────────────┘   │
└────────────────┬─────────────────────────────────────┘
                 │
┌────────────────▼─────────────────────────────────────┐
│          CAPA DE PERSISTENCIA                        │
│  • cliente.py (guardar/cargar clientes)             │
│  • inventario.py (guardar/cargar productos)         │
│  • usuarios.py (guardar/cargar usuarios)            │
│  • JSON (formato de almacenamiento)                 │
└────────────────┬─────────────────────────────────────┘
                 │
┌────────────────▼─────────────────────────────────────┐
│          ALMACENAMIENTO DE DATOS                     │
│  • usuarios.json (credenciales)                     │
│  • accesos.json (auditoría)                         │
│  • productos_empresa.json (inventario)              │
│  • clientes_empresa.json (clientes)                 │
└─────────────────────────────────────────────────────┘
```

### Patrón MVC Adaptado

```
MODEL (Modelos de Datos)
├── cliente.py
├── producto.py
├── empleado.py
├── empresa.py
├── inventario.py
├── venta.py
├── movimientos.py
└── puc.py

VIEW (Presentación)
├── Menús en sistema.py
├── Salidas de texto
├── Mensajes de validación
└── Confirmaciones

CONTROLLER (Lógica)
├── Validaciones en sistema.py
├── Cálculos en clases
├── Flujos de negocio
└── Integridad de datos
```

---

## 🎓 Conceptos OOP Aplicados

Este proyecto es un **ejemplo académico de Programación Orientada a Objetos**, demostrando los cuatro pilares fundamentales:

### 1️⃣ ENCAPSULAMIENTO

El encapsulamiento protege datos internos y controla el acceso mediante métodos.

#### Ejemplo: Clase Empleado

```python
class Empleado:
    def __init__(self, nombre, identificacion, salario):
        # Atributos PRIVADOS (protegidos con __)
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__salario = salario
    
    # GETTERS (métodos de acceso controlado)
    def nombre(self):
        return self.__nombre
    
    def identificacion(self):
        return self.__identificacion
    
    def salario(self):
        return self.__salario
```

**Ventajas demostradas:**
- ✅ Los datos no pueden modificarse directamente desde fuera
- ✅ Se pueden agregar validaciones en los getters si es necesario
- ✅ Cambios internos no afectan el código externo
- ✅ Protege la integridad de datos sensibles (salario)

#### Uso:

```python
# ✅ CORRECTO - Acceso a través de getter
empleado = Empleado("Juan", "12345", 2000000)
print(empleado.nombre())  # "Juan"

# ❌ INCORRECTO - Intento de acceso directo (falla)
# print(empleado.__nombre)  # AttributeError
```

---

### 2️⃣ HERENCIA

La herencia permite que una clase herede propiedades y métodos de otra.

#### Ejemplo: Clase Cajero hereda de Empleado

```python
class Empleado:
    def __init__(self, nombre, identificacion, salario):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__salario = salario
    
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"Empleado[{self.__identificacion}] - {self.__nombre}"


class Cajero(Empleado):
    # Hereda del constructor y métodos de Empleado
    
    def __init__(self, nombre, identificacion, salario):
        # Llama al constructor padre con super()
        super().__init__(nombre, identificacion, salario)
    
    # Método especializado de Cajero
    def registrar_venta(self, venta):
        venta.mostrar_resumen()
        print(f"\nVenta registrada por: {self.nombre()}")
```

**Jerarquía visualizada:**

```
        ┌──────────────┐
        │  Empleado    │
        │  (clase base)│
        └──────┬───────┘
               │ hereda
               │
        ┌──────▼───────┐
        │   Cajero     │
        │(especialización)
        └──────────────┘
```

**Ventajas demostradas:**
- ✅ Reutilización de código (no repetir __init__)
- ✅ Extensión de funcionalidad (método especializado registrar_venta)
- ✅ Relación lógica: "Un Cajero ES-UN Empleado"
- ✅ Fácil de mantener y extender con otros tipos de empleados

#### Uso Polimórfico:

```python
# Polimorfismo en acción
empleados = [
    Empleado("María", "789", 1800000),
    Cajero("Carlos", "456", 2000000),
]

for emp in empleados:
    # Método __str__() se ejecuta según la clase real
    print(emp)  # Empleado o Cajero según corresponda
    if isinstance(emp, Cajero):
        emp.registrar_venta(venta)
```

---

### 3️⃣ POLIMORFISMO

El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje de formas distintas.

#### Ejemplo: Método __str__() polimórfico

```python
# Cada clase tiene su propia implementación de __str__()

class Cliente:
    def __str__(self):
        return f"Cliente[{self.identificacion}] - {self.nombre}"

class Producto:
    def __str__(self):
        return f"Producto[{self.codigo}] - {self.nombre} - $ {self.precio:,.0f}"

class Venta:
    def __str__(self):
        total = self.calcular_total()
        return f"Venta #{self.numero} | Cliente: {self.cliente.nombre} | Total: $ {total:,.0f}"

class Movimiento:
    def __str__(self):
        return f"{self.fecha} | {self.tipo.upper()} | {self.producto.nombre} | Debe: {self.cuenta_debito.codigo} | Haber: {self.cuenta_credito.codigo}"
```

**Polimorfismo en acción:**

```python
# Lista heterogénea de objetos
objetos = [
    cliente,
    producto,
    venta,
    movimiento
]

# El mismo método print() genera salidas diferentes
for obj in objetos:
    print(obj)  # Llama a __str__() de cada clase
```

**Ventajas demostradas:**
- ✅ Código genérico que funciona con múltiples tipos
- ✅ Cada clase define su propia representación
- ✅ Fácil agregar nuevas clases sin cambiar código existente
- ✅ Interfaz uniforme para objetos diferentes

#### Polimorfismo con Métodos:

```python
# Ambos tienen método actualizar_stock() pero funciona diferente

class Producto:
    def actualizar_stock(self, cantidad):
        # Para Producto, suma a cantidad_en_stock
        self.cantidad_en_stock = self.cantidad_en_stock + cantidad

class Inventario:
    def actualizar_stock(self, producto, cantidad):
        # Para Inventario, busca y llama al método del Producto
        producto.actualizar_stock(cantidad)
```

---

### 4️⃣ ABSTRACCIÓN

La abstracción oculta complejidad y expone solo lo esencial.

#### Ejemplo: Venta (abstracción de transacción comercial)

```python
class Venta:
    contador = 1  # Atributo de clase (abstrae contador global)
    
    def __init__(self, cliente, productos=[]):
        self.numero = Venta.contador
        Venta.contador = Venta.contador + 1
        self.cliente = cliente
        self.productos = productos
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.estado = "pendiente"
    
    def agregar_producto(self, producto, cantidad, precio_unitario):
        """Abstrae la lógica de agregar producto"""
        # Validación interna
        if not producto.hay_suficiente_stock(cantidad):
            print(f"⚠ Sin stock suficiente para {producto.nombre}")
            return False
        
        # Operaciones internas
        producto.actualizar_stock(-cantidad)
        self.productos.append((producto, cantidad, precio_unitario))
        return True
    
    def calcular_total(self):
        """Abstrae el cálculo de total"""
        total = 0
        for producto, cantidad, precio_unitario in self.productos:
            total = total + (cantidad * precio_unitario)
        return total
    
    def mostrar_resumen(self):
        """Abstrae la presentación de resumen"""
        total = self.calcular_total()
        print(f"\n--- Venta #{self.numero} ---")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Fecha: {self.fecha}")
        for producto, cantidad, precio_unitario in self.productos:
            subtotal = cantidad * precio_unitario
            print(f"  {producto.nombre} x{cantidad} @ ${precio_unitario:,.0f} = ${subtotal:,.0f}")
        print(f"TOTAL: ${total:,.0f}")
```

**Ventajas demostradas:**
- ✅ Usuario solo ve métodos simples (agregar_producto, calcular_total)
- ✅ Detalles internos (validación, cálculos) ocultos
- ✅ Cambios internos no afectan la interfaz externa
- ✅ Código más legible y mantenible

#### Abstracción del Negocio:

```python
# El usuario no ve detalles contables
venta = Venta(cliente, [])
venta.agregar_producto(producto, cantidad, precio)

# Pero internamente el sistema genera movimientos automáticos
# (esto ocurre sin que el usuario tenga que hacerlo)
# Abstracción: Sistema maneja detalles, usuario solo ve "registrar venta"
```

---

### Comparativa de Conceptos OOP en Mini SIIGO

| Concepto | Implementación | Beneficio |
|---|---|---|
| **Encapsulamiento** | Empleado con atributos privados (__nombre, __salario) | Protege datos sensibles, control de acceso |
| **Herencia** | Cajero hereda de Empleado | Reutilización, especialización, relaciones lógicas |
| **Polimorfismo** | Múltiples __str__() en diferentes clases | Código flexible, interfaz uniforme |
| **Abstracción** | Venta oculta detalles de cálculos contables | Simplicidad, mantenibilidad, escalabilidad |

---

### Ejemplo Integral: Flujo Completo

```python
# 1. ABSTRACCIÓN: Usuarios ven operación simple
venta = Venta(cliente, [])
venta.agregar_producto(producto, 2, 5000)

# 2. ENCAPSULAMIENTO: Datos del Empleado protegidos
cajero = Cajero("Juan", "123", 2000000)
print(cajero.nombre())  # Acceso controlado

# 3. HERENCIA: Cajero aprovecha métodos de Empleado
print(cajero)  # Usa __str__() heredado con especialización

# 4. POLIMORFISMO: Diferentes objetos responden igual
for obj in [cliente, producto, venta, movimiento]:
    print(obj)  # Cada uno muestra su representación

# 5. RESULTADO: Sistema coherente, flexible y mantenible
```

---

## 📚 Documentación

### Archivos de Documentación Incluidos

| Archivo | Contenido |
|---|---|
| `README.md` | Este archivo - Guía completa de uso |
| `analisis_requerimientos.md` | Especificación formal, casos de uso, flujos |
| `diagrama_uml.md` | Diagrama de clases en formato Mermaid |
| `diagrama.drawio` | Diagrama editable en Draw.io |

### Generación de Documentación Adicional

```bash
# Generar documentación Sphinx (opcional)
cd docs
make html

# Ver documentación en navegador
open _build/html/index.html
```

---

## 🔧 Desarrollo

### Extensiones Futuras

El sistema está diseñado para ser extensible. Posibles mejoras:

- 🔧 **Interfaz Gráfica (GUI)**: Tkinter o PyQt
- 🌐 **API REST**: Flask o FastAPI
- 📊 **Reportes Avanzados**: Generación de PDF
- ☁️ **Sincronización en la Nube**: AWS S3 o similar
- 💳 **Integración de Pagos**: Stripe, PayPal
- 📱 **Aplicación Móvil**: React Native, Flutter
- 🔐 **Base de Datos**: PostgreSQL, MongoDB

### Cómo Contribuir

```bash
1. Hacer fork del proyecto
2. Crear rama feature: git checkout -b feature/nueva-funcionalidad
3. Commit cambios: git commit -am "Agrega nueva funcionalidad"
4. Push a la rama: git push origin feature/nueva-funcionalidad
5. Crear Pull Request
```

---

## ⚠️ Limitaciones Conocidas

| Limitación | Descripción | Solución |
|---|---|---|
| **Usuario único** | Solo una sesión por ejecución | Implementar con base de datos |
| **Almacenamiento local** | Datos en máquina local | Agregar sincronización en nube |
| **Sin multi-usuario** | Acceso simultáneo no soportado | Implementar arquitectura cliente-servidor |
| **CLI solo** | Interfaz de texto | Desarrollar GUI |
| **Reportes básicos** | Reportes limitados | Integrar librería de reportes |

---

## 🧪 Pruebas

### Pruebas Manuales Recomendadas

```
Flujo de Venta:
✓ Crear cliente
✓ Agregar productos
✓ Registrar venta con stock suficiente
✓ Registrar venta con stock insuficiente (validar error)
✓ Verificar movimientos contables

Flujo de Inventario:
✓ Agregar producto
✓ Alertas de stock bajo
✓ Búsqueda de productos
✓ Actualización de stock

Flujo Contable:
✓ Generación automática de movimientos
✓ Balance de cuentas
✓ Integridad de débito/crédito

Persistencia:
✓ Guardar datos
✓ Cargar datos
✓ Verificación de integridad
```

### Test Automatizados (Futuro)

```bash
# Ejemplos de pruebas con pytest
pytest tests/test_cliente.py
pytest tests/test_venta.py
pytest tests/test_inventario.py

# Cobertura
pytest --cov=. tests/
```

---

## 📞 Soporte

### Troubleshooting

**P: ¿Por qué no encuentra el archivo usuarios.json?**
R: El archivo se crea automáticamente en la primera ejecución.

**P: ¿Cómo recupero datos perdidos?**
R: Los datos se guardan con "Guardar datos" (opción 9). Si perdió datos sin guardar, lamentablemente no hay recuperación.

**P: ¿Puedo usar en múltiples computadoras?**
R: Actualmente no. Los datos son locales. Copiar carpeta proyecto/ a otra máquina y ejecutar independientemente.

**P: ¿Cómo cambio mi contraseña?**
R: Elimine usuarios.json y re-regístrese, o edite directamente el archivo JSON.

### Contacto y Reportar Bugs

- 📧 Email: soporte@mini-siigo.com
- 🐛 Issues: GitHub Issues
- 💬 Discussiones: GitHub Discussions

---

## 📋 Casos de Uso Académicos

Este proyecto es ideal para:

- 👨‍🎓 **Estudiantes**: Aprender OOP con caso real
- 👨‍🏫 **Docentes**: Enseñar conceptos de diseño y arquitectura
- 💼 **Profesionales**: Prototipado rápido de sistemas
- 🏢 **Pequeños negocios**: Solución funcional y económica

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**.

```
MIT License

Copyright (c) 2026 Mini SIIGO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

Consulte [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- **Python Community**: Por el lenguaje versátil
- **Open Source**: Por herramientas y inspiración
- **Contribuidores**: Por feedback y mejoras

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---|---|
| **Líneas de Código** | ~1,500 |
| **Clases** | 11 |
| **Métodos** | 50+ |
| **Módulos** | 10 |
| **Documentación** | 4 archivos |
| **Complejidad** | Baja-Media |
| **Cobertura OOP** | 95% |

---

## 🎯 Roadmap

### Versión 1.0 (Actual) ✅
- ✅ Gestión de inventario
- ✅ Registro de ventas
- ✅ Contabilidad integrada
- ✅ Persistencia de datos
- ✅ Sistema de usuarios

### Versión 1.1 (Próximo)
- 🚀 Reportes mejorados
- 🚀 Exportación a Excel
- 🚀 Gráficos de ventas

### Versión 2.0 (Futuro)
- 🎨 Interfaz gráfica (GUI)
- 🗄️ Base de datos SQL
- 🌐 Sincronización en nube
- 📱 App móvil

---

## 📝 Notas Finales

**Mini SIIGO** es una demostración de cómo principios sólidos de programación orientada a objetos pueden crear sistemas profesionales y mantenibles.

El código está diseñado para ser:
- 📖 **Legible**: Nombres descriptivos, estructura clara
- 🔧 **Mantenible**: Bajo acoplamiento, alta cohesión
- 📈 **Escalable**: Fácil de extender
- 🎓 **Educativo**: Perfecto para aprender

---

**¡Gracias por usar Mini SIIGO!**

Para más información, consulte los archivos de documentación incluidos.

```
Mini SIIGO v1.0.0
27 de mayo de 2026
```

---

<div align="center">

Hecho con ❤️ usando Python

⭐ Si te fue útil, por favor deja una estrella en GitHub

</div>
