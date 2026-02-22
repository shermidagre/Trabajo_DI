import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from gestor_inventario.bd.conexionBD import ConexionBD
from gestor_inventario.gui.ventanaPrincipal import VentanaPrincipal
from gestor_inventario.configuracionBD import configurarBaseDatos
from gestor_inventario.utils import obtenerRutaBaseDatos


class App:
    """Clase principal de la aplicación que inicializa la base de datos, carga estilos y abre la ventana."""

    def __init__(self):
        # 1. Aseguramos que la base de datos existe
        configurarBaseDatos(obtenerRutaBaseDatos())

        # 2. Cargamos los estilos CSS
        self.cargarEstilos()

        # 3. Iniciamos la ventana principal
        self.ventanaPrincipal = VentanaPrincipal()
        self.ventanaPrincipal.connect("destroy", Gtk.main_quit)
        self.ventanaPrincipal.show_all()

    def cargarEstilos(self):
        """Carga el archivo estilos.css y lo aplica a toda la aplicación."""
        proveedorCss = Gtk.CssProvider()
        # Buscamos el archivo estilos.css dinámicamente en la carpeta 'gui'
        rutaCss = os.path.join(os.path.dirname(__file__), "gui", "styles.css")

        try:
            proveedorCss.load_from_path(rutaCss)
            pantalla = Gdk.Screen.get_default()
            contextoEstilo = Gtk.StyleContext()
            # Aplicamos el CSS a nivel global
            contextoEstilo.add_provider_for_screen(
                pantalla,
                proveedorCss,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
            print("Estilos CSS cargados correctamente.")
        except Exception as error:
            print(f"Advertencia: No se pudo cargar el archivo CSS. {error}")


def iniciar():
    """Punto de entrada para el comando de consola."""
    aplicacionGestor = App()
    Gtk.main()

if __name__ == "__main__":
    iniciar()