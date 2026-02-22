import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gestorInventario.miLibreria.conexionBD import ConexionBD
from gestorInventario.gui.dialogoFormulario import DialogoFormulario
from gestorInventario.utilidades import obtenerRutaBaseDatos


class VentanaPrincipal(Gtk.Window):
    """Ventana principal de la aplicación de gestión de inventario."""

    def __init__(self):
        super().__init__(title="Gestor de Inventario")
        self.set_default_size(800, 600)
        self.set_border_width(10)

        # Contenedor principal
        cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaVertical)

        # Etiqueta de título
        etiquetaTitulo = Gtk.Label()
        etiquetaTitulo.set_markup("<big><b>Gestor de Inventario</b></big>")
        cajaVertical.pack_start(etiquetaTitulo, False, True, 0)

        # Vista de árbol para mostrar los productos
        self.modeloLista = Gtk.ListStore(int, str, str, int, float)
        self.vistaArbol = Gtk.TreeView(model=self.modeloLista)

        # Columnas explícitas
        renderizadorTexto = Gtk.CellRendererText()

        columnaId = Gtk.TreeViewColumn("ID", renderizadorTexto, text=0)
        self.vistaArbol.append_column(columnaId)

        columnaNombre = Gtk.TreeViewColumn("Nombre", renderizadorTexto, text=1)
        self.vistaArbol.append_column(columnaNombre)

        columnaCantidad = Gtk.TreeViewColumn("Cantidad", renderizadorTexto, text=3)
        self.vistaArbol.append_column(columnaCantidad)

        columnaPrecio = Gtk.TreeViewColumn("Precio", renderizadorTexto, text=4)
        self.vistaArbol.append_column(columnaPrecio)

        seleccionActual = self.vistaArbol.get_selection()
        seleccionActual.connect("changed", self.alCambiarSeleccion)

        ventanaDesplazable = Gtk.ScrolledWindow()
        ventanaDesplazable.set_hexpand(True)
        ventanaDesplazable.set_vexpand(True)
        ventanaDesplazable.add(self.vistaArbol)
        cajaVertical.pack_start(ventanaDesplazable, True, True, 0)

        # Caja para los botones
        cajaBotones = Gtk.Box(spacing=6)
        cajaVertical.pack_start(cajaBotones, False, True, 0)

        self.botonAñadir = Gtk.Button(label="Añadir")
        self.botonAñadir.connect("clicked", self.alHacerClicAñadir)

        self.botonEditar = Gtk.Button(label="Editar")
        self.botonEditar.connect("clicked", self.alHacerClicEditar)

        self.botonEliminar = Gtk.Button(label="Eliminar")
        self.botonEliminar.connect("clicked", self.alHacerClicEliminar)

        cajaBotones.pack_start(self.botonAñadir, True, True, 0)
        cajaBotones.pack_start(self.botonEditar, True, True, 0)
        cajaBotones.pack_start(self.botonEliminar, True, True, 0)

        # Desactivar botones de edición/borrado inicialmente
        self.botonEditar.set_sensitive(False)
        self.botonEliminar.set_sensitive(False)

        self.cargarDatos()

    def cargarDatos(self):
        self.modeloLista.clear()
        conexionBaseDatos = None
        try:
            conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
            conexionBaseDatos.conectarBaseDatos()
            conexionBaseDatos.crearCursor()
            listaProductos = conexionBaseDatos.consultaSinParametros(
                "SELECT id, nombre, descripcion, cantidad, precio FROM productos")
            if listaProductos:
                for productoActual in listaProductos:
                    self.modeloLista.append(list(productoActual))
        except Exception as errorCarga:
            print(f"Error al cargar los datos: {errorCarga}")
        finally:
            if conexionBaseDatos:
                conexionBaseDatos.cerrarBaseDatos()

    def alHacerClicAñadir(self, componenteBoton):
        dialogoFormulario = DialogoFormulario(ventanaPadre=self)
        respuestaDialogo = dialogoFormulario.run()
        if respuestaDialogo == Gtk.ResponseType.OK and dialogoFormulario.validarDatos():
            datosFormulario = dialogoFormulario.obtenerDatos()
            conexionBaseDatos = None
            try:
                conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
                conexionBaseDatos.conectarBaseDatos()
                conexionBaseDatos.crearCursor()
                consultaSql = "INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)"
                parametrosConsulta = (datosFormulario["nombre"], datosFormulario["descripcion"],
                                      datosFormulario["cantidad"], datosFormulario["precio"])
                conexionBaseDatos.añadirRegistro(consultaSql, *parametrosConsulta)
                self.cargarDatos()
            except Exception as errorAñadir:
                print(f"Error al añadir el producto: {errorAñadir}")
            finally:
                if conexionBaseDatos:
                    conexionBaseDatos.cerrarBaseDatos()
        dialogoFormulario.destroy()

    def alHacerClicEditar(self, componenteBoton):
        modeloDatos, iteradorArbol = self.vistaArbol.get_selection().get_selected()
        if iteradorArbol is None:
            return

        productoSeleccionado = list(modeloDatos[iteradorArbol])

        dialogoFormulario = DialogoFormulario(ventanaPadre=self, productoSeleccionado=productoSeleccionado)
        respuestaDialogo = dialogoFormulario.run()

        if respuestaDialogo == Gtk.ResponseType.OK and dialogoFormulario.validarDatos():
            datosFormulario = dialogoFormulario.obtenerDatos()
            conexionBaseDatos = None
            try:
                conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
                conexionBaseDatos.conectarBaseDatos()
                conexionBaseDatos.crearCursor()
                consultaSql = "UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=? WHERE id=?"
                parametrosConsulta = (datosFormulario["nombre"], datosFormulario["descripcion"],
                                      datosFormulario["cantidad"], datosFormulario["precio"], datosFormulario["id"])
                conexionBaseDatos.actualizarRegistro(consultaSql, *parametrosConsulta)
                self.cargarDatos()
            except Exception as errorEditar:
                print(f"Error al actualizar el producto: {errorEditar}")
            finally:
                if conexionBaseDatos:
                    conexionBaseDatos.cerrarBaseDatos()

        dialogoFormulario.destroy()

    def alHacerClicEliminar(self, componenteBoton):
        modeloDatos, iteradorArbol = self.vistaArbol.get_selection().get_selected()
        if iteradorArbol is None:
            return

        identificadorProducto = modeloDatos[iteradorArbol][0]
        nombreProducto = modeloDatos[iteradorArbol][1]

        dialogoConfirmacion = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text=f"¿Confirma la eliminación del producto '{nombreProducto}' (ID: {identificadorProducto})?"
        )
        dialogoConfirmacion.format_secondary_text("Esta acción no se puede deshacer.")

        respuestaDialogo = dialogoConfirmacion.run()
        dialogoConfirmacion.destroy()

        if respuestaDialogo == Gtk.ResponseType.YES:
            conexionBaseDatos = None
            try:
                conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
                conexionBaseDatos.conectarBaseDatos()
                conexionBaseDatos.crearCursor()
                consultaSql = "DELETE FROM productos WHERE id=?"
                conexionBaseDatos.eliminarRegistro(consultaSql, identificadorProducto)
                self.cargarDatos()
            except Exception as errorEliminar:
                print(f"Error al eliminar el producto: {errorEliminar}")
            finally:
                if conexionBaseDatos:
                    conexionBaseDatos.cerrarBaseDatos()

    def alCambiarSeleccion(self, seleccionActual):
        """Activa o desactiva los botones 'Editar' y 'Eliminar' según si hay una fila seleccionada."""
        modeloDatos, iteradorArbol = seleccionActual.get_selected()
        estaSeleccionado = iteradorArbol is not None
        self.botonEditar.set_sensitive(estaSeleccionado)
        self.botonEliminar.set_sensitive(estaSeleccionado)