import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gestor_inventario.bd.conexionBD import ConexionBD
from gestor_inventario.gui.dialogoFormulario import DialogoFormulario
from gestor_inventario.gui.ventanaCategorias import VentanaCategorias
from gestor_inventario.utils import obtenerRutaBaseDatos


class VentanaPrincipal(Gtk.Window):
    """Ventana principal de la aplicación de gestión de inventario."""

    def __init__(self):
        super().__init__(title="Gestor de Inventario")
        self.set_default_size(850, 600)
        self.set_border_width(10)

        # Contenedor principal
        cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaVertical)

        # Cabecera con título y botón de categorías
        cajaCabecera = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        etiquetaTitulo = Gtk.Label()
        etiquetaTitulo.set_markup("<big><b>Gestor de Inventario</b></big>")
        cajaCabecera.pack_start(etiquetaTitulo, False, False, 0)

        # Nuevo botón para la tercera ventana (Requisito del proyecto)
        self.botonCategorias = Gtk.Button(label="Gestionar Categorías")
        self.botonCategorias.connect("clicked", self.alHacerClicCategorias)
        cajaCabecera.pack_end(self.botonCategorias, False, False, 0)

        cajaVertical.pack_start(cajaCabecera, False, True, 0)

        # Vista de árbol (TreeView) para mostrar los productos
        # Estructura: id, nombre, descripcion, cantidad, precio, categoria_id, es_nuevo, en_stock
        self.modeloLista = Gtk.ListStore(int, str, str, int, float, int, int, int)
        self.vistaArbol = Gtk.TreeView(model=self.modeloLista)

        renderizadorTexto = Gtk.CellRendererText()
        renderizadorToggle = Gtk.CellRendererToggle()  # Para mostrar el stock visualmente

        # Añadimos solo las columnas más importantes a la vista (aunque el modelo guarda todo)
        self.vistaArbol.append_column(Gtk.TreeViewColumn("ID", renderizadorTexto, text=0))
        self.vistaArbol.append_column(Gtk.TreeViewColumn("Nombre", renderizadorTexto, text=1))
        self.vistaArbol.append_column(Gtk.TreeViewColumn("Cantidad", renderizadorTexto, text=3))
        self.vistaArbol.append_column(Gtk.TreeViewColumn("Precio (€)", renderizadorTexto, text=4))

        # Columna visual para el CheckButton (en_stock)
        columnaStock = Gtk.TreeViewColumn("En Stock", renderizadorToggle, active=7)
        self.vistaArbol.append_column(columnaStock)

        seleccionActual = self.vistaArbol.get_selection()
        seleccionActual.connect("changed", self.alCambiarSeleccion)

        ventanaDesplazable = Gtk.ScrolledWindow()
        ventanaDesplazable.set_hexpand(True)
        ventanaDesplazable.set_vexpand(True)
        ventanaDesplazable.add(self.vistaArbol)
        cajaVertical.pack_start(ventanaDesplazable, True, True, 0)

        # Caja para los botones de operaciones CRUD
        cajaBotones = Gtk.Box(spacing=6)
        cajaVertical.pack_start(cajaBotones, False, True, 0)

        self.botonAñadir = Gtk.Button(label="Añadir Producto")
        self.botonAñadir.get_style_context().add_class("boton-exito")
        self.botonAñadir.connect("clicked", self.alHacerClicAñadir)

        self.botonEditar = Gtk.Button(label="Editar Producto")
        self.botonEditar.connect("clicked", self.alHacerClicEditar)

        self.botonEliminar = Gtk.Button(label="Eliminar Producto")
        self.botonEliminar.get_style_context().add_class("boton-peligro")
        self.botonEliminar.connect("clicked", self.alHacerClicEliminar)

        cajaBotones.pack_start(self.botonAñadir, True, True, 0)
        cajaBotones.pack_start(self.botonEditar, True, True, 0)
        cajaBotones.pack_start(self.botonEliminar, True, True, 0)

        # Desactivar botones de edición/borrado inicialmente
        self.botonEditar.set_sensitive(False)
        self.botonEliminar.set_sensitive(False)

        self.cargarDatos()

    def cargarDatos(self):
        """Lee los registros de la base de datos y los carga en el TreeView."""
        self.modeloLista.clear()
        conexionBaseDatos = None
        try:
            conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
            conexionBaseDatos.conectarBaseDatos()
            conexionBaseDatos.crearCursor()
            # Ahora pedimos las 8 columnas para rellenar todo el modelo
            consultaSql = """
                SELECT id, nombre, descripcion, cantidad, precio, 
                       categoria_id, es_nuevo, en_stock 
                FROM productos
            """
            listaProductos = conexionBaseDatos.consultaSinParametros(consultaSql)
            if listaProductos:
                for productoActual in listaProductos:
                    self.modeloLista.append(list(productoActual))
        except Exception as errorCarga:
            print(f"Error al cargar los datos: {errorCarga}")
        finally:
            if conexionBaseDatos:
                conexionBaseDatos.cerrarBaseDatos()

    def alHacerClicCategorias(self, componenteBoton):
        """Abre la tercera ventana obligatoria para gestionar categorías."""
        ventanaCat = VentanaCategorias(ventanaPadre=self)
        # No hace falta procesar la respuesta, la ventana se gestiona sola.

    def alHacerClicAñadir(self, componenteBoton):
        """Abre el diálogo para añadir un nuevo producto con todas las opciones."""
        dialogoFormulario = DialogoFormulario(ventanaPadre=self)
        respuestaDialogo = dialogoFormulario.run()

        if respuestaDialogo == Gtk.ResponseType.OK and dialogoFormulario.validarDatos():
            datosFormulario = dialogoFormulario.obtenerDatos()
            conexionBaseDatos = None
            try:
                conexionBaseDatos = ConexionBD(obtenerRutaBaseDatos())
                conexionBaseDatos.conectarBaseDatos()
                conexionBaseDatos.crearCursor()
                consultaSql = """
                    INSERT INTO productos 
                    (nombre, descripcion, cantidad, precio, categoria_id, es_nuevo, en_stock) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                parametrosConsulta = (
                    datosFormulario["nombre"], datosFormulario["descripcion"],
                    datosFormulario["cantidad"], datosFormulario["precio"],
                    datosFormulario["categoria_id"], datosFormulario["es_nuevo"],
                    datosFormulario["en_stock"]
                )
                conexionBaseDatos.añadirRegistro(consultaSql, *parametrosConsulta)
                self.cargarDatos()
            except Exception as errorAñadir:
                print(f"Error al añadir el producto: {errorAñadir}")
            finally:
                if conexionBaseDatos:
                    conexionBaseDatos.cerrarBaseDatos()
        dialogoFormulario.destroy()

    def alHacerClicEditar(self, componenteBoton):
        """Abre el diálogo con los datos pre-cargados para editarlos."""
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
                consultaSql = """
                    UPDATE productos 
                    SET nombre=?, descripcion=?, cantidad=?, precio=?, 
                        categoria_id=?, es_nuevo=?, en_stock=? 
                    WHERE id=?
                """
                parametrosConsulta = (
                    datosFormulario["nombre"], datosFormulario["descripcion"],
                    datosFormulario["cantidad"], datosFormulario["precio"],
                    datosFormulario["categoria_id"], datosFormulario["es_nuevo"],
                    datosFormulario["en_stock"], datosFormulario["id"]
                )
                conexionBaseDatos.actualizarRegistro(consultaSql, *parametrosConsulta)
                self.cargarDatos()
            except Exception as errorEditar:
                print(f"Error al actualizar el producto: {errorEditar}")
            finally:
                if conexionBaseDatos:
                    conexionBaseDatos.cerrarBaseDatos()

        dialogoFormulario.destroy()

    def alHacerClicEliminar(self, componenteBoton):
        """Pide confirmación y elimina un registro de la base de datos."""
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