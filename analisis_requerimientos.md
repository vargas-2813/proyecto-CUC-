# Análisis de Requerimientos - Sistema Mini SIIGO

**Fecha de Elaboración:** 27 de mayo de 2026  
**Versión:** 1.0  
**Estado:** Documento Base

---

## Tabla de Contenidos

1. [Descripción del Problema](#descripción-del-problema)
2. [Alcance del Proyecto](#alcance-del-proyecto)
3. [Requerimientos Funcionales](#requerimientos-funcionales)
4. [Requerimientos No Funcionales](#requerimientos-no-funcionales)
5. [Actores del Sistema](#actores-del-sistema)
6. [Casos de Uso Principales](#casos-de-uso-principales)
7. [Modelo del Dominio](#modelo-del-dominio)
8. [Flujos de Negocio](#flujos-de-negocio)

---

## Descripción del Problema

### Contexto

Las pequeñas y medianas empresas (especialmente tiendas de barrio) requieren una solución integrada de gestión administrativa que les permita controlar:

- **Inventario de productos**: Seguimiento del stock disponible
- **Ventas**: Registro de transacciones comerciales
- **Clientes**: Información y historial de compras
- **Proveedores**: Gestión de suministros
- **Contabilidad**: Registro de movimientos contables según el Plan Único de Cuentas (PUC)
- **Personal**: Control de empleados y sus funciones

### Problema Específico

Actualmente, muchas tiendas gestionan estas operaciones de forma manual o con herramientas desintegradas, lo que genera:

- **Ineficiencia operativa**: Procesos lentos y propensos a errores
- **Falta de trazabilidad**: No hay registro integral de transacciones
- **Inconsistencia de datos**: Múltiples fuentes de información
- **Incumplimiento contable**: Dificultad en registros contables formales
- **Pérdida de información**: Riesgo de datos sin respaldo

### Solución Propuesta

Desarrollar un **Sistema Integrado de Gestión Empresarial (Mini SIIGO)** que centralice todas las operaciones comerciales y contables en una única plataforma.

---

## Alcance del Proyecto

### Incluido

✅ Gestión de empresas con autenticación  
✅ Control de inventario con alertas de stock bajo  
✅ Registro de ventas y facturación  
✅ Gestión de clientes y historial de compras  
✅ Administración de proveedores  
✅ Control de empleados y roles específicos (Cajero)  
✅ Integración contable con Plan Único de Cuentas (PUC)  
✅ Registro de movimientos contables (débito/crédito)  
✅ Reportes básicos (ventas, inventario, balances)  
✅ Persistencia de datos (guardar/cargar JSON)  
✅ Sistema de usuarios con autenticación  
✅ Auditoría de accesos

### No Incluido

❌ Interfaz gráfica avanzada (GUI)  
❌ Multi-usuario simultáneo  
❌ Sincronización en la nube  
❌ Integración con sistemas de pago online  
❌ Reportes financieros avanzados (balances, flujos de caja)  
❌ Gestión de impuestos  
❌ Módulo de compras automatizado  
❌ API REST para terceros

---

## Requerimientos Funcionales

### RF1: Autenticación y Gestión de Usuarios

| Identificador | RF1 |
|---|---|
| **Nombre** | Autenticación de Usuarios |
| **Descripción** | El sistema debe permitir registrar nuevos usuarios y autenticar usuarios existentes |
| **Actores** | Usuario No Autenticado |
| **Precondiciones** | Sistema iniciado |
| **Flujo Principal** | 1. Usuario ingresa username y password<br>2. Sistema valida credenciales<br>3. Si es válido, registra acceso y permite entrada<br>4. Si es inválido, muestra error |
| **Postcondiciones** | Usuario autenticado o rechazado |
| **Criterios de Aceptación** | - Username único<br>- Contraseña no visible en pantalla<br>- Registro de accesos en log<br>- Validación obligatoria |

### RF2: Gestión de Empresas

| Identificador | RF2 |
|---|---|
| **Nombre** | Crear y Acceder a Empresas |
| **Descripción** | El sistema debe permitir registrar múltiples empresas y acceder según autenticación |
| **Actores** | Usuario Autenticado |
| **Precondiciones** | Usuario autenticado |
| **Flujo Principal** | 1. Usuario selecciona opción "Registrar empresa"<br>2. Ingresa NIT, nombre y contraseña<br>3. Sistema valida y almacena<br>4. Usuario puede seleccionar empresa y autenticarse |
| **Postcondiciones** | Empresa registrada o seleccionada |
| **Criterios de Aceptación** | - NIT único<br>- Campos requeridos validados<br>- Contraseña por empresa |

### RF3: Gestión de Inventario

| Identificador | RF3 |
|---|---|
| **Nombre** | Administrar Productos en Inventario |
| **Descripción** | El sistema debe permitir agregar, buscar y visualizar productos con control de stock |
| **Actores** | Gerente, Vendedor |
| **Precondiciones** | Usuario autenticado en empresa |
| **Flujo Principal** | 1. Usuario selecciona "Agregar producto"<br>2. Ingresa código, nombre, precio, stock inicial, stock mínimo<br>3. Sistema sugiere cuenta PUC automáticamente<br>4. Producto se agrega al inventario<br>5. Sistema alerta si stock cae bajo mínimo |
| **Postcondiciones** | Producto agregado y disponible |
| **Criterios de Aceptación** | - Código único<br>- Precios positivos<br>- Stock mínimo validado<br>- Alertas de stock bajo<br>- Búsqueda por código disponible |

### RF4: Registro de Ventas

| Identificador | RF4 |
|---|---|
| **Nombre** | Registrar Venta Completa |
| **Descripción** | El sistema debe registrar ventas con productos, cliente y generar movimientos contables automáticos |
| **Actores** | Cajero, Vendedor |
| **Precondiciones** | Usuario autenticado, Inventario no vacío, Cliente registrado o nuevo |
| **Flujo Principal** | 1. Usuario selecciona "Registrar venta"<br>2. Identifica o crea cliente<br>3. Selecciona múltiples productos y cantidades<br>4. Valida stock disponible<br>5. Genera venta con número único<br>6. Crea movimientos contables automáticos<br>7. Reduce stock de productos<br>8. Registra en historial del cliente |
| **Postcondiciones** | Venta registrada, Stock actualizado, Movimientos contables creados |
| **Criterios de Aceptación** | - Validación de stock obligatoria<br>- Número de venta único<br>- Movimientos contables automáticos<br>- Historial de cliente actualizado<br>- Fecha y hora registrada |

### RF5: Gestión de Clientes

| Identificador | RF5 |
|---|---|
| **Nombre** | Administrar Clientes y Historial |
| **Descripción** | El sistema debe mantener registro de clientes con historial de compras |
| **Actores** | Cajero, Vendedor, Gerente |
| **Precondiciones** | Usuario autenticado en empresa |
| **Flujo Principal** | 1. Sistema registra cliente en primera compra<br>2. Identifica cliente por nombre en ventas posteriores<br>3. Permite visualizar historial de compras<br>4. Guarda datos en persistencia |
| **Postcondiciones** | Cliente registrado con historial actualizado |
| **Criterios de Aceptación** | - Identificación única por documento<br>- Historial completo disponible<br>- Datos persistentes |

### RF6: Registro de Compras

| Identificador | RF6 |
|---|---|
| **Nombre** | Registrar Compra a Proveedor |
| **Descripción** | El sistema debe registrar compras que aumentan inventario y crean movimientos contables |
| **Actores** | Gerente, Encargado de Compras |
| **Precondiciones** | Usuario autenticado, Inventario con productos |
| **Flujo Principal** | 1. Usuario selecciona "Registrar compra"<br>2. Ingresa datos del proveedor<br>3. Selecciona productos a comprar y cantidades<br>4. Ingresa precio de compra unitario<br>5. Actualiza stock de productos<br>6. Crea movimientos contables de compra<br>7. Calcula total de compra |
| **Postcondiciones** | Compra registrada, Stock aumentado, Movimientos generados |
| **Criterios de Aceptación** | - Proveedor registrable<br>- Stock actualizado correctamente<br>- Movimientos contables creados (inventario/compras)<br>- Total calculado automáticamente |

### RF7: Gestión de Cuentas PUC

| Identificador | RF7 |
|---|---|
| **Nombre** | Administrar Plan Único de Cuentas |
| **Descripción** | El sistema debe permitir ver, agregar y sugerir cuentas contables |
| **Actores** | Contador, Gerente |
| **Precondiciones** | Usuario autenticado en empresa |
| **Flujo Principal** | 1. Sistema proporciona sugerencias automáticas de PUC por descripción<br>2. Usuario puede aceptar sugerencia o seleccionar manual<br>3. Nuevas cuentas se pueden agregar<br>4. Se mantiene catálogo de cuentas estándar (1435, 1105, 4135, etc.) |
| **Postcondiciones** | Cuenta PUC asignada o agregada |
| **Criterios de Aceptación** | - Sugerencias automáticas funcionales<br>- Validación de código único<br>- Búsqueda de cuentas disponible |

### RF8: Registro de Movimientos Contables

| Identificador | RF8 |
|---|---|
| **Nombre** | Registrar Movimientos Contables Automáticos |
| **Descripción** | El sistema debe registrar automáticamente movimientos de débito/crédito en cada transacción |
| **Actores** | Sistema (automático), Contador (consulta) |
| **Precondiciones** | Venta o Compra registrada |
| **Flujo Principal** | 1. En cada venta: Débito Caja, Crédito Ventas<br>2. En cada compra: Débito Inventario, Crédito Compras<br>3. Cada movimiento registra fecha, cantidad, valor unitario<br>4. Todos los movimientos son consultables |
| **Postcondiciones** | Movimientos contables creados y persistentes |
| **Criterios de Aceptación** | - Movimientos creados automáticamente<br>- Débito y crédito balanceados<br>- Registro de fecha/hora<br>- Descripción de transacción |

### RF9: Reportes y Consultas

| Identificador | RF9 |
|---|---|
| **Nombre** | Generar Reportes Básicos |
| **Descripción** | El sistema debe proporcionar reportes de ventas, inventario y balances contables |
| **Actores** | Gerente, Contador |
| **Precondiciones** | Usuario autenticado, Datos registrados |
| **Flujo Principal** | 1. Usuario selecciona tipo de reporte<br>2. Sistema procesa datos<br>3. Muestra:<br>&nbsp;&nbsp;&nbsp;&nbsp;- Balance por cuenta PUC<br>&nbsp;&nbsp;&nbsp;&nbsp;- Resumen de ventas<br>&nbsp;&nbsp;&nbsp;&nbsp;- Estado de inventario |
| **Postcondiciones** | Reporte mostrado en pantalla |
| **Criterios de Aceptación** | - Cálculos correctos<br>- Datos actualizados<br>- Formato claro |

### RF10: Persistencia de Datos

| Identificador | RF10 |
|---|---|
| **Nombre** | Guardar y Cargar Datos |
| **Descripción** | El sistema debe guardar datos en archivos JSON y permitir cargarlos posteriormente |
| **Actores** | Sistema (automático), Usuario (manual) |
| **Precondiciones** | Datos registrados en sesión |
| **Flujo Principal** | 1. Usuario selecciona "Guardar datos"<br>2. Sistema serializa a JSON<br>3. Verifica integridad<br>4. Guarda en archivos<br>5. Usuario puede cargar datos guardados |
| **Postcondiciones** | Datos guardados persistentemente, Verificación completada |
| **Criterios de Aceptación** | - Formatos JSON válidos<br>- Verificación de integridad<br>- Recuperación exitosa<br>- Confirmaciones de operación |

---

## Requerimientos No Funcionales

### RNF1: Rendimiento

| Requisito | Especificación |
|---|---|
| **Tiempo de Respuesta** | < 2 segundos para operaciones de lectura |
| **Búsquedas** | Búsqueda de productos en < 500ms (hasta 1000 artículos) |
| **Escalabilidad** | Soportar mínimo 10,000 transacciones por empresa |

### RNF2: Confiabilidad

| Requisito | Especificación |
|---|---|
| **Disponibilidad** | 99% durante horarios de operación |
| **Integridad de Datos** | Verificación en cada guardado |
| **Respaldo** | Archivos JSON con redundancia |
| **Recuperación** | Recuperación de errores sin perder datos en sesión |

### RNF3: Seguridad

| Requisito | Especificación |
|---|---|
| **Autenticación** | Username/Password requerido |
| **Autorización** | Roles: Gerente, Vendedor, Cajero, Contador |
| **Auditoría** | Registro de todos los accesos y cambios |
| **Protección de Datos** | Archivos JSON en carpeta local protegida |
| **Validación** | Validación de entrada en todos los campos |

### RNF4: Usabilidad

| Requisito | Especificación |
|---|---|
| **Interfaz** | Menús intuitivos basados en texto |
| **Navegación** | Estructura clara de opciones |
| **Mensajes** | Retroalimentación clara al usuario |
| **Idioma** | Español |

### RNF5: Mantenibilidad

| Requisito | Especificación |
|---|---|
| **Lenguaje** | Python 3.7+ |
| **Código** | Estructura modular con clases bien definidas |
| **Documentación** | Docstrings y comentarios |
| **Versionamiento** | Control de versiones Git |

### RNF6: Compatibilidad

| Requisito | Especificación |
|---|---|
| **Sistemas Operativos** | Windows, Linux, macOS |
| **Python** | 3.7 o superior |
| **Dependencias** | Mínimas (librería estándar) |

### RNF7: Sostenibilidad

| Requisito | Especificación |
|---|---|
| **Costos** | Solución de bajo costo |
| **Mantenimiento** | Fácil de actualizar |
| **Extensibilidad** | Diseño para agregar módulos futuros |

---

## Actores del Sistema

### 1. Usuario No Autenticado
- **Descripción**: Persona que accede al sistema por primera vez
- **Responsabilidades**: 
  - Registrarse como nuevo usuario
  - Proporcionar credenciales válidas
- **Objetivos**:
  - Acceder al sistema
  - Crear cuenta de usuario

### 2. Usuario Autenticado
- **Descripción**: Persona registrada en el sistema
- **Responsabilidades**:
  - Seleccionar empresa a utilizar
  - Autenticarse en empresa específica
- **Objetivos**:
  - Acceder a funciones según rol
  - Registrar transacciones

### 3. Gerente/Administrador
- **Descripción**: Responsable de la gestión empresarial
- **Responsabilidades**:
  - Crear y configurar empresas
  - Supervisar operaciones
  - Acceder a reportes
  - Gestionar inventario
  - Registrar compras
- **Objetivos**:
  - Tomar decisiones informadas
  - Mantener operación eficiente
  - Cumplir con registros contables

### 4. Cajero
- **Descripción**: Empleado encargado de cobros
- **Responsabilidades**:
  - Registrar ventas
  - Manejar transacciones de clientes
  - Consultar inventario
- **Objetivos**:
  - Procesar ventas rápidamente
  - Mantener exactitud en cobros
  - Registrar clientes

### 5. Vendedor
- **Descripción**: Empleado de ventas
- **Responsabilidades**:
  - Consultar disponibilidad de productos
  - Registrar ventas
  - Mantener relación con clientes
  - Ver historial de compras
- **Objetivos**:
  - Vender productos
  - Fidelizar clientes
  - Cumplir metas

### 6. Contador/Contabilista
- **Descripción**: Profesional de contabilidad
- **Responsabilidades**:
  - Revisar movimientos contables
  - Consultar balances por cuenta
  - Sugerir asignaciones de cuentas PUC
  - Validar integridad contable
- **Objetivos**:
  - Mantener registros contables correctos
  - Cumplir normatividad
  - Proporcionar información financiera

### 7. Sistema (Automático)
- **Descripción**: Procesos automatizados
- **Responsabilidades**:
  - Generar números únicos (ventas, facturas)
  - Crear movimientos contables automáticos
  - Actualizar stock
  - Validar datos
  - Sugerir cuentas PUC
- **Objetivos**:
  - Asegurar consistencia
  - Reducir errores manuales
  - Registrar auditoría

---

## Casos de Uso Principales

### Caso de Uso 1: Registrar Nueva Venta

```
Título: Registrar Nueva Venta
Actor Primario: Cajero
Precondiciones:
- Usuario autenticado en empresa
- Inventario con productos disponibles

Flujo Principal:
1. Cajero selecciona "Registrar venta"
2. Ingresa o identifica cliente
3. Para cada producto:
   a. Selecciona producto del inventario
   b. Ingresa cantidad
   c. Confirma precio de venta
4. Sistema valida stock
5. Sistema calcula total
6. Usuario confirma venta
7. Sistema crea:
   - Objeto Venta con número único
   - Movimientos contables (Caja/Ventas)
   - Actualiza Cliente con historial
   - Reduce stock de productos

Postcondiciones:
- Venta registrada en sistema
- Stock actualizado
- Movimientos contables creados
- Historial de cliente actualizado
- Usuario recibe confirmación

Flujos Alternativos:
- Si stock insuficiente: Mostrar error y permitir seleccionar otro producto
- Si cliente nuevo: Capturar datos y crear nuevo Cliente
- Si usuario cancela: Descartar venta sin cambios
```

### Caso de Uso 2: Consultar Reporte de Ventas

```
Título: Consultar Reporte de Ventas
Actor Primario: Gerente
Precondiciones:
- Usuario autenticado
- Ventas registradas en sistema

Flujo Principal:
1. Usuario selecciona "Reportes" → "Resumen de ventas"
2. Sistema recupera todas las ventas de la empresa
3. Para cada venta:
   a. Suma el total
   b. Muestra detalles (fecha, cliente, productos, total)
4. Sistema muestra total general de ventas
5. Usuario visualiza información en pantalla

Postcondiciones:
- Reporte mostrado
- Datos actualizados reflejados
- Usuario tiene visibilidad financiera
```

### Caso de Uso 3: Agregar Nuevo Producto

```
Título: Agregar Nuevo Producto al Inventario
Actor Primario: Gerente
Precondiciones:
- Usuario autenticado en empresa

Flujo Principal:
1. Usuario selecciona "Agregar producto"
2. Ingresa:
   - Código único del producto
   - Nombre del producto
   - Precio unitario
   - Cantidad inicial en stock
   - Stock mínimo recomendado
3. Sistema sugiere automáticamente cuenta PUC basada en nombre
4. Usuario puede aceptar o cambiar la cuenta sugerida
5. Sistema valida datos:
   - Código único
   - Precios positivos
   - Stock mínimo válido
6. Producto se agrega al Inventario
7. Sistema confirma agregación

Postcondiciones:
- Producto registrado en inventario
- Cuenta PUC asociada
- Stock inicial registrado
- Disponible para ventas

Flujos Alternativos:
- Si código duplicado: Mostrar error, permitir intentar de nuevo
- Si precio negativo: Mostrar validación, rechazar entrada
- Si usuario rechaza cuenta sugerida: Mostrar lista para seleccionar
```

### Caso de Uso 4: Registrar Compra a Proveedor

```
Título: Registrar Compra a Proveedor
Actor Primario: Gerente
Precondiciones:
- Usuario autenticado en empresa
- Inventario con productos

Flujo Principal:
1. Usuario selecciona "Registrar compra"
2. Ingresa datos del proveedor:
   - Nombre
   - NIT
3. Para cada producto a comprar:
   a. Selecciona producto del inventario
   b. Ingresa cantidad a comprar
   c. Ingresa precio de compra unitario
4. Sistema calcula subtotal (cantidad × precio)
5. Usuario confirma compra
6. Sistema:
   - Actualiza stock de cada producto
   - Crea movimientos contables (Inventario/Compras)
   - Calcula total de compra
   - Registra proveedor

Postcondiciones:
- Compra registrada
- Stock aumentado
- Movimientos contables creados
- Proveedor registrado en sistema

Flujos Alternativos:
- Usuario cancela: Sin cambios en datos
- Precio diferente al del producto: Registra nuevo precio de compra
```

### Caso de Uso 5: Autenticarse en el Sistema

```
Título: Autenticarse en el Sistema
Actor Primario: Usuario No Autenticado
Precondiciones:
- Sistema iniciado
- Usuario existente en archivo usuarios.json

Flujo Principal:
1. Sistema muestra menú de autenticación
2. Usuario selecciona:
   a. "Login" - si es usuario existente
   b. "Registrarse" - si es nuevo usuario
3. Si Login:
   - Ingresa username
   - Ingresa password
   - Sistema valida credenciales
   - Si válido: Registra acceso, muestra menú principal
   - Si inválido: Muestra error, permite reintentar
4. Si Registro:
   - Ingresa username nuevo
   - Ingresa password
   - Sistema guarda credenciales
   - Usuario autenticado automáticamente

Postcondiciones:
- Usuario autenticado o rechazado
- Acceso registrado en auditoría
- Sesión iniciada
```

---

## Modelo del Dominio

### Entidades Principales

#### Cliente
Representa un comprador del sistema.

```
Propiedades:
- identificacion (String): Documento de identidad único
- nombre (String): Nombre completo
- telefono (String): Contacto
- historial_compras (List[Venta]): Todas sus transacciones

Comportamientos:
- agregar_compra(venta): Registra una compra en su historial
- mostrar_historial(): Visualiza todas sus compras
```

**Relaciones:**
- Tiene múltiples Ventas (1:*)
- Puede estar asociado a una Factura (1:1)

---

#### Producto
Artículo del inventario.

```
Propiedades:
- codigo (String): Identificador único
- nombre (String): Descripción del producto
- precio (float): Precio unitario de venta
- cantidad_en_stock (int): Unidades disponibles
- stock_minimo (int): Punto de reorden

Comportamientos:
- mostrar_info(): Muestra detalles
- actualizar_stock(cantidad): Aumenta/disminuye stock
- hay_suficiente_stock(cantidad): Valida disponibilidad
```

**Relaciones:**
- Pertenece a Inventario (1:1)
- Puede estar en múltiples Ventas (*)
- Puede estar en múltiples Compras (*)
- Es registrado en Movimientos (*:1)

---

#### Inventario
Gestor del stock de productos.

```
Propiedades:
- productos (List[Producto]): Catálogo de artículos

Comportamientos:
- agregar_producto(producto): Añade al catálogo
- buscar_producto(codigo): Localiza por código
- mostrar_inventario(): Lista todos con alertas de stock
```

**Relaciones:**
- Contiene múltiples Productos (1:*)

---

#### Venta
Transacción comercial de venta.

```
Propiedades:
- numero (int): Identificador único (contador estático)
- cliente (Cliente): Quién compra
- productos (List[Tuple]): Lista de (Producto, cantidad, precio)
- fecha (String): Timestamp de la venta
- estado (String): "pendiente" (extensible a "pagada", "cancelada")

Comportamientos:
- agregar_producto(producto, cantidad, precio): Añade artículo
- calcular_total(): Suma de todos los artículos
- mostrar_resumen(): Muestra detalles de la venta
```

**Relaciones:**
- Asociada a un Cliente (1:1)
- Contiene múltiples Productos (*)
- Genera múltiples Movimientos contables (1:*)
- Parte del historial del Cliente

---

#### Empleado
Personal de la empresa.

```
Propiedades:
- __nombre (String): Privado, acceso mediante getter
- __identificacion (String): Privado
- __salario (float): Privado

Comportamientos:
- nombre(): Getter de nombre
- identificacion(): Getter de identificación
- salario(): Getter de salario
```

**Relaciones:**
- Base para Cajero (herencia)

---

#### Cajero
Especialización de Empleado.

```
Hereda de: Empleado

Comportamientos Adicionales:
- registrar_venta(venta): Valida y registra venta
```

**Relaciones:**
- Hereda de Empleado
- Crea Ventas

---

#### CuentaPUC
Representa una cuenta contable del Plan Único de Cuentas.

```
Propiedades:
- codigo (String): Código de cuenta (ej: "1435")
- nombre (String): Descripción (ej: "Mercancías")

Comportamientos:
- __str__(): Representación textual
```

**Relaciones:**
- Utilizada en Movimientos como débito (1:*)
- Utilizada en Movimientos como crédito (1:*)

---

#### Movimiento
Registro contable de un asiento.

```
Propiedades:
- fecha (String): Timestamp
- tipo (String): "venta" o "compra"
- producto (Producto): Artículo involucrado
- cantidad (int): Unidades
- valor_unitario (float): Precio unitario
- cuenta_debito (CuentaPUC): Cuenta que recibe
- cuenta_credito (CuentaPUC): Cuenta que entrega
- descripcion (String): Detalle (ej: "Venta factura #5")

Comportamientos:
- __str__(): Muestra resumen del movimiento
```

**Relaciones:**
- Generado automáticamente por cada Venta o Compra
- Referencias a un Producto
- Referencias a dos CuentasPUC (débito/crédito)

---

#### Factura
Documento formal de venta.

```
Propiedades:
- numero (int): Identificador único (contador estático)
- cliente (Cliente): Comprador
- productos_vendidos (List[Tuple]): Items facturados
- total (float): Suma total
- fecha (String): Fecha de emisión

Comportamientos:
- __str__(): Resumen de factura
```

**Relaciones:**
- Asociada a un Cliente (1:1)
- Detalla múltiples Productos (1:*)

---

#### Proveedor
Entidad externa que suministra productos.

```
Propiedades:
- nombre (String): Nombre del proveedor
- nit (String): NIT único

Comportamientos:
- __str__(): Representación textual
```

**Relaciones:**
- Provee múltiples Productos (1:*)

---

#### Empresa
Organización gestionada en el sistema.

```
Propiedades:
- id_empresa (String): Identificador único
- nombre (String): Nombre comercial
- password (String): Autenticación por empresa

Comportamientos:
- __str__(): Representación textual
```

**Relaciones:**
- Contiene múltiples Inventarios
- Contiene múltiples Empleados
- Registra múltiples Ventas
- Mantiene múltiples Clientes

---

### Diagrama de Relaciones Conceptual

```
┌─────────────┐
│  Empresa    │
└─────┬───────┘
      │
      ├─ contiene ──→ ┌────────────┐
      │               │ Inventario │
      │               └────┬───────┘
      │                    │
      │                    ├─ contiene* ──→ ┌─────────────┐
      │                    │                 │  Producto   │
      │                    │                 └─────┬───────┘
      │                    │                       │
      ├─ maneja* ──→ ┌───────────┐                │
      │               │ Empleado  │                │
      │               └───────┬───┘                │
      │                       │                   │
      │                       └─ especializa ──→ ┌─────────┐
      │                                          │ Cajero  │
      │                                          └───┬─────┘
      │                                              │
      │                                       registra*
      │                                              │
      ├─ tiene* ──→ ┌────────────┐                 │
      │             │  Cliente   │◄────────────────┘
      │             └──────┬─────┘
      │                    │
      │                    ├─ tiene* ──→ ┌──────────┐
      │                    │             │  Venta   │
      │                    │             └─────┬────┘
      │                    │                   │
      │                    │            genera*│
      │                    │                   │
      └─ registra* ────→ ┌─────────┐          │
                        │Movimiento◄──────────┘
                        └────┬────┘
                             │
                          usa│(débito)
                             │usa(crédito)
                             │
                             └──→ ┌──────────────┐
                                  │ CuentaPUC    │
                                  └──────────────┘

Multiplicidades:
* = 1 a muchos
  = 1 a 1
```

---

## Flujos de Negocio

### Flujo 1: Venta Completa

```
1. CAJERO INICIA VENTA
   └─ Selecciona "Registrar venta"
   
2. IDENTIFICACIÓN DE CLIENTE
   ├─ ¿Cliente existente?
   │  ├─ Sí: Busca por nombre → Cliente existe
   │  └─ No: Crea nuevo Cliente (identificación, nombre, teléfono)
   
3. SELECCIÓN DE PRODUCTOS
   └─ Repite hasta finalizar:
      ├─ Lista productos disponibles
      ├─ Selecciona producto
      ├─ Valida stock disponible
      │  ├─ Si hay: Ingresa cantidad
      │  └─ Si no: Mensaje de error, reintenta
      └─ Ingresa precio de venta
   
4. CONFIRMACIÓN DE VENTA
   ├─ Sistema calcula TOTAL
   ├─ Usuario confirma
   
5. CREACIÓN DE OBJETOS Y REGISTROS
   ├─ Crea Venta con número único
   ├─ Reduce stock de cada Producto
   ├─ Agrega Venta al historial de Cliente
   
6. MOVIMIENTOS CONTABLES AUTOMÁTICOS
   ├─ Para cada Producto vendido:
   │  └─ Crea Movimiento:
   │     ├─ Cuenta débito: Caja (1105)
   │     ├─ Cuenta crédito: Ventas (4135)
   │     ├─ Cantidad y valor
   │     └─ Descripción: "Venta factura #X"
   
7. CONFIRMACIÓN AL USUARIO
   └─ Muestra resumen de venta
```

### Flujo 2: Compra a Proveedor

```
1. GERENTE INICIA COMPRA
   └─ Selecciona "Registrar compra"
   
2. DATOS DEL PROVEEDOR
   ├─ Ingresa nombre del proveedor
   └─ Ingresa NIT
   
3. SELECCIÓN DE ARTÍCULOS
   └─ Repite hasta finalizar:
      ├─ Lista productos disponibles
      ├─ Selecciona producto
      ├─ Ingresa cantidad a comprar
      └─ Ingresa precio de compra unitario
   
4. CONFIRMACIÓN DE COMPRA
   ├─ Sistema calcula TOTAL
   └─ Usuario confirma
   
5. ACTUALIZACIÓN DE INVENTARIO
   ├─ Para cada Producto:
   │  └─ Aumenta cantidad_en_stock
   │     
6. MOVIMIENTOS CONTABLES AUTOMÁTICOS
   ├─ Para cada Producto comprado:
   │  └─ Crea Movimiento:
   │     ├─ Cuenta débito: Inventario (1435)
   │     ├─ Cuenta crédito: Compras (6205)
   │     ├─ Cantidad y valor
   │     └─ Descripción: "Compra a [Proveedor]"
   
7. CONFIRMACIÓN
   └─ Muestra confirmación de compra
```

### Flujo 3: Consulta de Reportes

```
1. USUARIO SOLICITA REPORTE
   └─ Selecciona opción de reportes
   
2. SELECCIONA TIPO DE REPORTE
   ├─ Balance por cuenta PUC
   ├─ Resumen de ventas
   └─ Estado de inventario
   
3. PARA BALANCE POR CUENTA:
   ├─ Recorre todos los Movimientos
   ├─ Suma débitos (Cuenta débito)
   ├─ Resta créditos (Cuenta crédito)
   ├─ Calcula saldo por cuenta
   └─ Muestra resultados
   
4. PARA RESUMEN DE VENTAS:
   ├─ Recorre todas las Ventas
   ├─ Suma totales
   ├─ Muestra:
   │  ├─ Número de venta
   │  ├─ Cliente
   │  ├─ Productos
   │  ├─ Total individual
   │  └─ TOTAL GENERAL
   
5. PARA ESTADO DE INVENTARIO:
   ├─ Muestra todos los Productos
   ├─ Indica alertas de stock bajo
   └─ Muestra cantidades actuales
```

---

## Matriz de Trazabilidad

| Requerimiento Funcional | Caso de Uso | Clases Involucradas |
|---|---|---|
| RF1: Autenticación | CU5 | Usuario, Sistema |
| RF2: Gestión de Empresas | CU5 | Empresa, Usuario |
| RF3: Gestión de Inventario | CU3 | Inventario, Producto |
| RF4: Registro de Ventas | CU1 | Venta, Cliente, Producto, Movimiento |
| RF5: Gestión de Clientes | CU1 | Cliente, Venta |
| RF6: Registro de Compras | CU4 | Proveedor, Producto, Movimiento |
| RF7: Gestión de Cuentas PUC | CU1, CU3, CU4 | CuentaPUC |
| RF8: Movimientos Contables | CU1, CU4 | Movimiento, CuentaPUC |
| RF9: Reportes | CU2 | Venta, Movimiento, Inventario |
| RF10: Persistencia | Todas | Sistema |

---

## Restricciones del Negocio

1. **Validación de Stock**: No se puede vender cantidad mayor al stock disponible
2. **Unicidad**: Códigos de producto y usuario deben ser únicos
3. **Integridad Contable**: Cada movimiento debe tener débito y crédito
4. **Autenticación Obligatoria**: Acceso solo con credenciales válidas
5. **Auditabilidad**: Todo cambio debe ser registrable
6. **Persistencia**: Los datos deben ser recuperables

---

## Supuestos

1. Los usuarios ingresarán datos válidos (con validación del sistema)
2. Las transacciones se realizan en moneda local (pesos)
3. Las empresas operan durante horarios de negocio convencional
4. El sistema se ejecuta en una máquina local
5. Un usuario por sesión
6. Precios y cantidades siempre positivos

---

## Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Pérdida de datos | Media | Alto | Respaldos periódicos, validación en guardado |
| Acceso no autorizado | Baja | Alto | Autenticación, auditoría |
| Errores de cálculo | Baja | Medio | Validaciones automáticas |
| Inconsistencia contable | Baja | Alto | Generación automática de movimientos |

---

## Conclusiones

El Sistema Mini SIIGO proporciona una solución integral para pequeñas empresas que requieren:

✅ Control de inventario eficiente  
✅ Registro de transacciones exacto  
✅ Integridad contable automática  
✅ Trazabilidad completa de operaciones  
✅ Fácil acceso a información vital  

La arquitectura modular permite futuras expansiones y mejoras sin afectar funcionalidades existentes.

---

**Documento Generado:** 27 de mayo de 2026  
**Versión:** 1.0  
**Estado:** Aprobado para desarrollo
