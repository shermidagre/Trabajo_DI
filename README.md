
---

# 📦 Gestor de Inventario

Un sistema de gestión de inventario de escritorio, limpio y eficiente, desarrollado en **Python** utilizando **GTK3** para la interfaz gráfica y **SQLite** para el almacenamiento local de datos.

## ✨ Características

* **Gestión de Productos (CRUD):** Añade, edita, elimina y visualiza productos fácilmente.
* **Gestión de Categorías:** Organiza tu inventario creando categorías personalizadas.
* **Base de datos local:** Almacenamiento seguro en SQLite aislado en la carpeta de usuario (`~/.gestor_inventario/`).
* **Interfaz moderna:** Estilos personalizados mediante CSS (tematización completa de GtkTreeView, botones y formularios).
* **Validación de datos:** Formularios a prueba de errores.

## 📚 Documentación

Puedes consultar la documentación detallada de la API, clases y métodos, generada con **Sphinx**, en el siguiente enlace:

👉 **[gestor-inventario-samuel.readthedocs.io](https://www.google.com/search?q=https://gestor-inventario-samuel.readthedocs.io/es/latest/)**

## 🛠️ Requisitos Previos

* **Python** 3.8 o superior.
* Librerías de **GTK3** instaladas en tu sistema:
* *Linux:* Instaladas por defecto en la mayoría de distribuciones (como Debian/Ubuntu).
* *Windows:* Requiere un entorno como MSYS2 o WSL.



## 🚀 Instalación

La aplicación está publicada, por lo que puedes instalarla fácilmente a través de `pip`:

```bash
pip install .

```

## Uso

Una vez instalado, puedes ejecutar la aplicación con el comando:

```bash
xestor-inventario

```

## 🧪 Tests

Para ejecutar las pruebas unitarias de validación y conexión a base de datos:

```bash
python -m unittest discover tests/

```

## 📊 Arquitectura del Sistema

### 1. Diagrama de Clases

Este diagrama muestra cómo se relacionan las piezas principales del código, incluyendo la lógica de la aplicación, la interfaz y la persistencia.

```mermaid
classDiagram
    class App {
        +VentanaPrincipal ventanaPrincipal
        +__init__()
        +cargarEstilos()
    }

    class VentanaPrincipal {
        +GtkTreeView vistaArbol
        +__init__()
        +cargarDatos()
        +alHacerClicAnadir(widget)
        +alHacerClicEditar(widget)
        +alHacerClicEliminar(widget)
        +alHacerClicCategorias(widget)
    }

    class DialogoFormulario {
        +int identificadorProducto
        +__init__(ventanaPadre, productoSeleccionado)
        +cargarCategorias()
        +obtenerDatos()
        +validarDatos()
    }

    class VentanaCategorias {
        +GtkTreeView vistaArbol
        +__init__(ventanaPadre)
        +cargarDatos()
        +alHacerClicAnadir(widget)
    }

    class ConexionBD {
        +String rutaBaseDatos
        +Connection conexionActiva
        +Cursor cursorActivo
        +__init__(rutaBaseDatos)
        +conectarBaseDatos()
        +crearCursor()
        +consultaSenParametros(sql)
        +engadeRexistro(sql, args)
        +actualizaRexistro(sql, args)
        +eliminarRegistro(sql, args)
        +cerrarBaseDatos()
    }

    %% Relaciones
    App "1" *-- "1" VentanaPrincipal : Inicializa
    VentanaPrincipal "1" ..> "*" DialogoFormulario : Abre
    VentanaPrincipal "1" ..> "1" VentanaCategorias : Abre
    VentanaPrincipal ..> ConexionBD : Usa
    DialogoFormulario ..> ConexionBD : Usa
    VentanaCategorias ..> ConexionBD : Usa

```

### 2. Diagrama de Secuencia

Proceso de añadir un nuevo producto al inventario:

```mermaid
sequenceDiagram
    actor Usuario
    participant VP as VentanaPrincipal
    participant DF as DialogoFormulario
    participant BD as ConexionBD
    participant SQLite as Base de Datos Local

    Usuario->>VP: Clic en botón "Añadir"
    VP->>DF: __init__(parent=VP, producto=None)
    activate DF
    DF->>BD: conectarBaseDatos()
    BD->>SQLite: SELECT * FROM categorias
    SQLite-->>BD: Retorna categorías
    BD-->>DF: Diccionario de categorías
    DF-->>VP: Muestra ventana modal (Formulario)
    
    Usuario->>DF: Rellena datos y clic en "Guardar"
    DF->>DF: validarDatos()
    alt Datos Inválidos
        DF-->>Usuario: Muestra MensajeDialog (Error)
    else Datos Válidos
        DF->>DF: obtenerDatos()
        DF->>BD: conectarBaseDatos()
        DF->>BD: engadeRexistro(INSERT INTO productos...)
        activate BD
        BD->>SQLite: Ejecuta Query
        SQLite-->>BD: OK
        BD-->>DF: Operación exitosa
        deactivate BD
        DF-->>VP: Retorna ResponseType.OK
        deactivate DF
        
        VP->>BD: conectarBaseDatos()
        VP->>BD: consultaSenParametros(SELECT * FROM productos...)
        BD->>SQLite: Ejecuta Query
        SQLite-->>BD: Retorna filas actualizadas
        BD-->>VP: Datos de productos
        VP->>VP: Actualiza GtkListStore (TreeView)
        VP-->>Usuario: Muestra tabla actualizada
    end

```

---

**Desarrollado por:** Samuel
