
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    """
    Ventana principal de la aplicación de gestión de inventario.
    """
    def __init__(self):
        """
        Constructor de la ventana principal.
        """
        super().__init__(title="Xestor de Inventario")
        self.set_default_size(800, 600)
        self.set_border_width(10)

        # Contenedor principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Etiqueta de título
        title_label = Gtk.Label()
        title_label.set_markup("<big><b>Xestor de Inventario</b></big>")
        vbox.pack_start(title_label, False, True, 0)
        
        # Por ahora, un placeholder para el TreeView
        placeholder_label = Gtk.Label(label="Aquí irá el Gtk.TreeView con los productos.")
        vbox.pack_start(placeholder_label, True, True, 0)

        # Caja para los botones
        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, False, True, 0)

        btn_add = Gtk.Button(label="Engadir")
        btn_edit = Gtk.Button(label="Editar")
        btn_delete = Gtk.Button(label="Eliminar")

        button_box.pack_start(btn_add, True, True, 0)
        button_box.pack_start(btn_edit, True, True, 0)
        button_box.pack_start(btn_delete, True, True, 0)
