import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Recordatorio: si renombras las carpetas a camelCase en tu sistema de archivos, los imports quedarán así:
from gestorInventario.miLibreria.conexionBD import ConexionBD
from gestorInventario.gui.ventanaPrincipal import VentanaPrincipal
from gestorInventario.configuracionBD import configurarBaseDatos
from gestorInventario.utils import obtenerRutaBaseDatos


class Aplicacion:
    """Clase principal de la aplicación que inicializa la base de datos y la ventana principal."""

    def __init__(self):
        # Aseguramos que la base de datos existe
        configurarBaseDatos(obtenerRutaBaseDatos())

        self.ventanaPrincipal = VentanaPrincipal()
        self.ventanaPrincipal.connect("destroy", Gtk.main_quit)
        self.ventanaPrincipal.show_all()


if __name__ == "__main__":
    aplicacionGestor = Aplicacion()
    Gtk.main()