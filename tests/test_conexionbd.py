
import unittest
import os
import sqlite3

# Importamos la clase ConexionBD desde la ruta relativa
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'mi_libreria')))
from conexionBD import ConexionBD

# Importamos la función setup_database para crear la tabla de productos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database_setup import setup_database


class TestConexionBD(unittest.TestCase):
    """
    Clase de pruebas para el módulo ConexionBD.
    """
    DB_NAME = "test_inventario.db"

    def setUp(self):
        """
        Configura la base de datos de prueba antes de cada test.
        """
        if os.path.exists(self.DB_NAME):
            os.remove(self.DB_NAME)
        setup_database(self.DB_NAME) # Usamos la función de setup para crear la tabla

    def tearDown(self):
        """
        Elimina la base de datos de prueba después de cada test.
        """
        if os.path.exists(self.DB_NAME):
            os.remove(self.DB_NAME)

    def test_connection_success(self):
        """
        Verifica que la conexión a la base de datos se realiza correctamente.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        self.assertIsNotNone(db.conexion)
        db.pechaBD()

    def test_cursor_creation(self):
        """
        Verifica que el cursor se crea correctamente después de la conexión.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        self.assertIsNotNone(db.cursor)
        db.pechaBD()

    def test_engadeRexistro(self):
        """
        Verifica que se puede añadir un registro correctamente.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        
        sql = "INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)"
        params = ("Producto Test", "Descripcion Test", 10, 9.99)
        db.engadeRexistro(sql, *params)
        
        productos = db.consultaSenParametros("SELECT * FROM productos")
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0][1], "Producto Test") # Nombre
        db.pechaBD()

    def test_consultaSenParametros(self):
        """
        Verifica que se pueden consultar registros sin parámetros.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "P1", "D1", 1, 1.0)
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "P2", "D2", 2, 2.0)
        
        productos = db.consultaSenParametros("SELECT * FROM productos")
        self.assertEqual(len(productos), 2)
        db.pechaBD()

    def test_consultaConParametros(self):
        """
        Verifica que se pueden consultar registros con parámetros.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "P1", "D1", 1, 1.0)
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "P2", "D2", 2, 2.0)
        
        productos = db.consultaConParametros("SELECT * FROM productos WHERE nombre = ?", "P1")
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0][1], "P1")
        db.pechaBD()

    def test_actualizaRexistro(self):
        """
        Verifica que se puede actualizar un registro existente.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "Old Name", "Old Desc", 5, 5.50)
        
        producto_id = db.consultaSenParametros("SELECT id FROM productos WHERE nombre = 'Old Name'")[0][0]
        
        db.actualizaRexistro("UPDATE productos SET nombre = ?, cantidad = ? WHERE id = ?", "New Name", 15, producto_id)
        
        updated_producto = db.consultaConParametros("SELECT * FROM productos WHERE id = ?", producto_id)[0]
        self.assertEqual(updated_producto[1], "New Name")
        self.assertEqual(updated_producto[3], 15)
        db.pechaBD()

    def test_borraRexistro(self):
        """
        Verifica que se puede borrar un registro correctamente.
        """
        db = ConexionBD(self.DB_NAME)
        db.conectaBD()
        db.creaCursor()
        
        db.engadeRexistro("INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)", "To Delete", "Desc", 10, 10.0)
        
        producto_id = db.consultaSenParametros("SELECT id FROM productos WHERE nombre = 'To Delete'")[0][0]
        
        db.borraRexistro("DELETE FROM productos WHERE id = ?", producto_id)
        
        productos = db.consultaSenParametros("SELECT * FROM productos")
        self.assertEqual(len(productos), 0)
        db.pechaBD()

    def test_pechaBD_handles_none_connection(self):
        """
        Verifica que pechaBD no falla si la conexión no se ha establecido.
        """
        db = ConexionBD(self.DB_NAME)
        # No conectaBD ni creaCursor
        db.pechaBD() # No debería lanzar error
        self.assertIsNone(db.conexion)
        self.assertIsNone(db.cursor)

if __name__ == '__main__':
    unittest.main()
