import sqlite3


def configurarBaseDatos(nombreBaseDatos="inventario.db"):
    """
    Crea y configura la base de datos inicial.
    Crea un fichero de base de datos SQLite y una tabla 'productos' si no existen.
    """
    conexionBaseDatos = None
    try:
        conexionBaseDatos = sqlite3.connect(nombreBaseDatos)
        cursorBaseDatos = conexionBaseDatos.cursor()

        # Crear la tabla de productos si no existe
        cursorBaseDatos.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
        """)

        conexionBaseDatos.commit()
        print(f"Base de datos '{nombreBaseDatos}' y tabla 'productos' configuradas correctamente.")

    except sqlite3.Error as errorBaseDatos:
        print(f"Error al configurar la base de datos: {errorBaseDatos}")
    finally:
        if conexionBaseDatos:
            conexionBaseDatos.close()


if __name__ == "__main__":
    configurarBaseDatos()