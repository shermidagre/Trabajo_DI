import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gestor_inventario.bd.conexionBD import ConexionBD
from gestor_inventario.utils import obtenerRutaBaseDatos


class DialogoFormulario(Gtk.Dialog):

    def __init__(self, ventanaPadre, productoSeleccionado=None):
        esModoEdicion = productoSeleccionado is not None
        tituloDialogo = "Editar Producto" if esModoEdicion else "Añadir Nuevo Producto"

        super().__init__(title=tituloDialogo, transient_for=ventanaPadre, flags=0)

        # 1. Añadimos los botones al diálogo
        self.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        # 2. ¡AQUÍ APLICAMOS EL CSS! Recuperamos los botones y les damos la clase
        botonGuardar = self.get_widget_for_response(Gtk.ResponseType.OK)
        botonGuardar.get_style_context().add_class("boton-exito")

        botonCancelar = self.get_widget_for_response(Gtk.ResponseType.CANCEL)
        botonCancelar.get_style_context().add_class("boton-peligro")

        self.set_default_size(450, 400)
        self.set_border_width(10)

        cuadricula = Gtk.Grid(column_spacing=10, row_spacing=10, margin=10)
        self.get_content_area().add(cuadricula)

        # 1. Gtk.Entry (Nombre)
        cuadricula.attach(Gtk.Label(label="Nombre:", xalign=0), 0, 0, 1, 1)
        self.entradaNombre = Gtk.Entry()
        cuadricula.attach(self.entradaNombre, 1, 0, 1, 1)

        # 2. Gtk.ComboBoxText (Categoría)
        cuadricula.attach(Gtk.Label(label="Categoría:", xalign=0), 0, 1, 1, 1)
        self.comboCategoria = Gtk.ComboBoxText()
        self.diccionarioCategorias = self.cargarCategorias()
        for idCat, nombreCat in self.diccionarioCategorias.items():
            self.comboCategoria.append(str(idCat), nombreCat)
        self.comboCategoria.set_active(0)
        cuadricula.attach(self.comboCategoria, 1, 1, 1, 1)

        # 3. Gtk.TextView (Descripción multilínea)
        cuadricula.attach(Gtk.Label(label="Descripción:", xalign=0, yalign=0), 0, 2, 1, 1)
        self.bufferDescripcion = Gtk.TextBuffer()
        self.vistaTextoDescripcion = Gtk.TextView(buffer=self.bufferDescripcion)
        self.vistaTextoDescripcion.set_size_request(-1, 80)  # Altura fija
        marcoTexto = Gtk.Frame()
        marcoTexto.add(self.vistaTextoDescripcion)
        cuadricula.attach(marcoTexto, 1, 2, 1, 1)

        # SpinButtons (Cantidad y Precio)
        cuadricula.attach(Gtk.Label(label="Cantidad:", xalign=0), 0, 3, 1, 1)
        self.selectorCantidad = Gtk.SpinButton(adjustment=Gtk.Adjustment(0, 0, 10000, 1), digits=0)
        cuadricula.attach(self.selectorCantidad, 1, 3, 1, 1)

        cuadricula.attach(Gtk.Label(label="Precio:", xalign=0), 0, 4, 1, 1)
        self.selectorPrecio = Gtk.SpinButton(adjustment=Gtk.Adjustment(0.0, 0.0, 100000.0, 0.01), digits=2)
        cuadricula.attach(self.selectorPrecio, 1, 4, 1, 1)

        # 4. Gtk.RadioButton (Estado del producto)
        cuadricula.attach(Gtk.Label(label="Estado:", xalign=0), 0, 5, 1, 1)
        cajaEstado = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.radioNuevo = Gtk.RadioButton.new_with_label_from_widget(None, "Nuevo")
        self.radioUsado = Gtk.RadioButton.new_with_label_from_widget(self.radioNuevo, "Usado")
        cajaEstado.pack_start(self.radioNuevo, False, False, 0)
        cajaEstado.pack_start(self.radioUsado, False, False, 0)
        cuadricula.attach(cajaEstado, 1, 5, 1, 1)

        # 5. Gtk.CheckButton (Disponibilidad)
        self.checkStock = Gtk.CheckButton(label="Disponible en Stock")
        self.checkStock.set_active(True)
        cuadricula.attach(self.checkStock, 1, 6, 1, 1)

        # Si estamos en edición, rellenar datos
        if esModoEdicion:
            self.identificadorProducto = productoSeleccionado[0]
            self.entradaNombre.set_text(productoSeleccionado[1])
            self.bufferDescripcion.set_text(productoSeleccionado[2])
            self.selectorCantidad.set_value(productoSeleccionado[3])
            self.selectorPrecio.set_value(productoSeleccionado[4])
            self.comboCategoria.set_active_id(str(productoSeleccionado[5]))

            if productoSeleccionado[6] == 1:
                self.radioNuevo.set_active(True)
            else:
                self.radioUsado.set_active(True)

            self.checkStock.set_active(bool(productoSeleccionado[7]))
        else:
            self.identificadorProducto = None

        self.show_all()

    def cargarCategorias(self):
        """Retorna un diccionario {id: nombre} con las categorías de la BD."""
        diccionario = {}
        baseDatos = ConexionBD(obtenerRutaBaseDatos())
        baseDatos.conectarBaseDatos()
        baseDatos.crearCursor()
        filas = baseDatos.consultaSinParametros("SELECT id, nombre FROM categorias")
        if filas:
            for fila in filas:
                diccionario[fila[0]] = fila[1]
        baseDatos.cerrarBaseDatos()
        return diccionario

    def obtenerDatos(self):
        inicio, fin = self.bufferDescripcion.get_bounds()
        return {
            "id": self.identificadorProducto,
            "nombre": self.entradaNombre.get_text(),
            "descripcion": self.bufferDescripcion.get_text(inicio, fin, False),
            "cantidad": self.selectorCantidad.get_value_as_int(),
            "precio": self.selectorPrecio.get_value(),
            "categoria_id": int(self.comboCategoria.get_active_id()) if self.comboCategoria.get_active_id() else 1,
            "es_nuevo": 1 if self.radioNuevo.get_active() else 0,
            "en_stock": 1 if self.checkStock.get_active() else 0
        }

    def validarDatos(self):
        if not self.entradaNombre.get_text().strip():
            self.mostrarMensajeError("El campo 'Nombre' no puede estar vacío.")
            return False
        return True

    def mostrarMensajeError(self, mensajeError):
        """Muestra un diálogo de error si falla la validación."""
        dialogoError = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CANCEL,
            text="Error de validación"
        )
        dialogoError.format_secondary_text(mensajeError)
        dialogoError.run()
        dialogoError.destroy()