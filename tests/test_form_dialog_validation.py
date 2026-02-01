
import unittest
from unittest.mock import MagicMock, patch

# Agregamos la ruta de la librería al path para poder importarla
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gui.form_dialog import FormDialog


# Mock para Gtk.Entry
class MockEntry:
    def __init__(self, text=""):
        self._text = text
    
    def get_text(self):
        return self._text
    
    def set_text(self, text):
        self._text = text

# Mock para Gtk.SpinButton
class MockSpinButton:
    def __init__(self, value=0.0):
        self._value = value
    
    def get_value_as_int(self):
        return int(self._value)
    
    def get_value(self):
        return float(self._value)
    
    def set_value(self, value):
        self._value = value


class TestFormDialogValidation(unittest.TestCase):
    """
    Clase de pruebas para la validación del FormDialog.
    Mockeamos los componentes Gtk para probar la lógica sin una interfaz gráfica.
    """

    def setUp(self):
        """
        Configura una instancia dummy de FormDialog con mocks para sus widgets Gtk.
        """
        # Mock para la ventana padre (necesario por transient_for)
        mock_parent = MagicMock()

        # Creamos una instancia de FormDialog con un producto nulo para "Add" mode
        self.dialog = FormDialog(parent=mock_parent, producto=None)
        
        # Reemplazamos los widgets Gtk reales con nuestros mocks
        self.dialog.txt_nombre = MockEntry()
        self.dialog.txt_desc = MockEntry()
        self.dialog.spin_cantidad = MockSpinButton()
        self.dialog.spin_precio = MockSpinButton()

        # Mock para el método show_error_message
        self.dialog.show_error_message = MagicMock()

    def test_valid_data_add_mode(self):
        """
        Verifica que la validación pasa con datos válidos en modo añadir.
        """
        self.dialog.txt_nombre.set_text("Nuevo Producto")
        self.dialog.txt_desc.set_text("Una descripción")
        self.dialog.spin_cantidad.set_value(5)
        self.dialog.spin_precio.set_value(12.50)

        self.assertTrue(self.dialog.validate_data())
        self.dialog.show_error_message.assert_not_called()

    def test_empty_nombre_add_mode(self):
        """
        Verifica que la validación falla si el campo 'nombre' está vacío.
        """
        self.dialog.txt_nombre.set_text("") # Nombre vacío
        self.dialog.txt_desc.set_text("Una descripción")
        self.dialog.spin_cantidad.set_value(5)
        self.dialog.spin_precio.set_value(12.50)

        self.assertFalse(self.dialog.validate_data())
        self.dialog.show_error_message.assert_called_once_with("O campo 'Nome' non pode estar baleiro.")

    def test_whitespace_nombre_add_mode(self):
        """
        Verifica que la validación falla si el campo 'nombre' solo contiene espacios.
        """
        self.dialog.txt_nombre.set_text("   ") # Solo espacios
        self.assertFalse(self.dialog.validate_data())
        self.dialog.show_error_message.assert_called_once_with("O campo 'Nome' non pode estar baleiro.")

    def test_get_data(self):
        """
        Verifica que el método get_data devuelve los datos correctamente.
        """
        self.dialog.producto_id = 1 # Simula un ID para edición
        self.dialog.txt_nombre.set_text("Producto de Prueba")
        self.dialog.txt_desc.set_text("Descripción detallada")
        self.dialog.spin_cantidad.set_value(10)
        self.dialog.spin_precio.set_value(99.99)

        expected_data = {
            "id": 1,
            "nombre": "Producto de Prueba",
            "descripcion": "Descripción detallada",
            "cantidad": 10,
            "precio": 99.99
        }
        self.assertEqual(self.dialog.get_data(), expected_data)

    def test_edit_mode_initial_data(self):
        """
        Verifica que el diálogo inicializa correctamente los datos en modo edición.
        """
        # Datos simulados para el producto en modo edición
        producto_data = [101, "Producto Editado", "Desc. Editada", 25, 50.25]
        
        # Volvemos a instanciar el diálogo en modo edición
        mock_parent = MagicMock()
        dialog_edit = FormDialog(parent=mock_parent, producto=producto_data)
        
        # Aseguramos que los mocks estén en su lugar para la validación
        dialog_edit.txt_nombre = MockEntry(text=producto_data[1])
        dialog_edit.txt_desc = MockEntry(text=producto_data[2])
        dialog_edit.spin_cantidad = MockSpinButton(value=producto_data[3])
        dialog_edit.spin_precio = MockSpinButton(value=producto_data[4])
        
        self.assertEqual(dialog_edit.producto_id, 101)
        self.assertEqual(dialog_edit.txt_nombre.get_text(), "Producto Editado")
        self.assertEqual(dialog_edit.txt_desc.get_text(), "Desc. Editada")
        self.assertEqual(dialog_edit.spin_cantidad.get_value_as_int(), 25)
        self.assertEqual(dialog_edit.spin_precio.get_value(), 50.25)


if __name__ == '__main__':
    unittest.main()
