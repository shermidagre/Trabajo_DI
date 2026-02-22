import sqlite3


def configurarBaseDatos(nombreBaseDatos="inventario.db"):
    """
    Crea y configura la base de datos inicial con tablas relacionadas.
    """
    conexionBaseDatos = None
    try:
        conexionBaseDatos = sqlite3.connect(nombreBaseDatos)
        cursorBaseDatos = conexionBaseDatos.cursor()

        # 1. Crear tabla de categorías
        cursorBaseDatos.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
        """)

        # Insertar algunas categorías por defecto si está vacía
        cursorBaseDatos.execute("SELECT COUNT(*) FROM categorias")
        if cursorBaseDatos.fetchone()[0] == 0:
            cursorBaseDatos.executemany("INSERT INTO categorias (nombre) VALUES (?)",
                                        [("Electrónica",), ("Mobiliario",), ("Ofimática",)])

        # 2. Crear tabla de productos (ahora con relaciones y más campos)
        cursorBaseDatos.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria_id INTEGER,
            es_nuevo INTEGER,      -- 1 para Nuevo, 0 para Usado (RadioButton)
            en_stock INTEGER,      -- 1 para Sí, 0 para No (CheckButton)
            FOREIGN KEY(categoria_id) REFERENCES categorias(id)
        )
        """)

        conexionBaseDatos.commit()
        print(f"Base de datos configurada correctamente con relaciones.")

    except sqlite3.Error as errorBaseDatos:
        print(f"Error al configurar la base de datos: {errorBaseDatos}")
    finally:
        if conexionBaseDatos:
            conexionBaseDatos.close()


if __name__ == "__main__":
    configurarBaseDatos()