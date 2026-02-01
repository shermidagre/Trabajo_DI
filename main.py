
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

# Agregamos la ruta de la librería al path para poder importarla
sys.path.append('src')
from mi_libreria.conexionBD import ConexionBD
from gui.main_window import MainWindow

class App:
    """
    Clase principal de la aplicación que inicializa la base de datos y la ventana principal.
    """
    def __init__(self):
        # Aquí podrías inicializar la conexión a la BD, por ejemplo
        # self.db = ConexionBD("inventario.db")
        
        self.win = MainWindow()
        self.win.connect("destroy", Gtk.main_quit)
        self.win.show_all()

if __name__ == "__main__":
    app = App()
    Gtk.main()
