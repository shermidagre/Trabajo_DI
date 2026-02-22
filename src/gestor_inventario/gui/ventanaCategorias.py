import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gestor_inventario.bd.conexionBD import ConexionBD
from gestor_inventario.utils import obtenerRutaBaseDatos


class VentanaCategorias(Gtk.Window):
    """Ventana secundaria para gestionar las categorías (Cumple requisito de 3ª ventana)."""

    def __init__(self, ventanaPadre):
        super().__init__(title="Gestión de Categorías", transient_for=ventanaPadre)
        self.set_default_size(300, 400)
        self.set_border_width(10)
        self.set_modal(True)

        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        # Formulario rápido para añadir categoría
        cajaFormulario = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.entradaNuevaCategoria = Gtk.Entry(placeholder_text="Nueva categoría...")
        botonAñadir = Gtk.Button(label="Añadir")
        botonAñadir.get_style_context().add_class("boton-exito")
        botonAñadir.connect("clicked", self.alHacerClicAñadir)
        
        cajaFormulario.pack_start(self.entradaNuevaCategoria, True, True, 0)
        cajaFormulario.pack_start(botonAñadir, False, False, 0)
        cajaPrincipal.pack_start(cajaFormulario, False, False, 0)

        # Lista de categorías
        self.modeloCategorias = Gtk.ListStore(int, str)
        self.vistaArbol = Gtk.TreeView(model=self.modeloCategorias)

        renderizador = Gtk.CellRendererText()
        columnaNombre = Gtk.TreeViewColumn("Nombre de Categoría", renderizador, text=1)
        self.vistaArbol.append_column(columnaNombre)

        ventanaDesplazable = Gtk.ScrolledWindow()
        ventanaDesplazable.add(self.vistaArbol)
        cajaPrincipal.pack_start(ventanaDesplazable, True, True, 0)

        self.cargarDatos()
        self.show_all()

    def cargarDatos(self):
        self.modeloCategorias.clear()
        baseDatos = ConexionBD(obtenerRutaBaseDatos())
        baseDatos.conectarBaseDatos()
        baseDatos.crearCursor()
        categorias = baseDatos.consultaSinParametros("SELECT id, nombre FROM categorias")
        if categorias:
            for cat in categorias:
                self.modeloCategorias.append(list(cat))
        baseDatos.cerrarBaseDatos()

    def alHacerClicAñadir(self, widget):
        nombre = self.entradaNuevaCategoria.get_text().strip()
        if nombre:
            baseDatos = ConexionBD(obtenerRutaBaseDatos())
            baseDatos.conectarBaseDatos()
            baseDatos.crearCursor()
            baseDatos.añadirRegistro("INSERT INTO categorias (nombre) VALUES (?)", nombre)
            baseDatos.cerrarBaseDatos()
            self.entradaNuevaCategoria.set_text("")
            self.cargarDatos()