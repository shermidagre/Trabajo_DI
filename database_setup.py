
import sqlite3

def setup_database(db_name="inventario.db"):
    """
    Crea y configura la base de datos inicial.

    Crea un fichero de base de datos SQLite y una tabla 'productos' si no existen.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Crear la tabla de productos si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
        """)
        
        conn.commit()
        print(f"Base de datos '{db_name}' y tabla 'productos' configuradas correctamente.")

    except sqlite3.Error as e:
        print(f"Error al configurar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
