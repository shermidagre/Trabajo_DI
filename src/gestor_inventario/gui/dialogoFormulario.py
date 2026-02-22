import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class DialogoFormulario(Gtk.Dialog):
    """Diálogo para añadir o editar un producto."""

    def __init__(self, ventanaPadre, productoSeleccionado=None):
        """Constructor del diálogo."""
        esModoEdicion = productoSeleccionado is not None
        tituloDialogo = "Editar Producto" if esModoEdicion else "Añadir Nuevo Producto"

        super().__init__(title=tituloDialogo, transient_for=ventanaPadre, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE, Gtk.ResponseType.OK
        )

        self.set_default_size(400, 250)
        self.set_border_width(10)

        cuadriculaContenedor = Gtk.Grid(column_spacing=10, row_spacing=10, margin=10)
        areaContenido = self.get_content_area()
        areaContenido.add(cuadriculaContenedor)

        # Campos del formulario
        etiquetaNombre = Gtk.Label(label="Nombre:", xalign=0)
        self.entradaNombre = Gtk.Entry()

        etiquetaDescripcion = Gtk.Label(label="Descripción:", xalign=0)
        self.entradaDescripcion = Gtk.Entry()

        etiquetaCantidad = Gtk.Label(label="Cantidad:", xalign=0)
        ajusteCantidad = Gtk.Adjustment(lower=0, upper=10000, step_increment=1)
        self.selectorCantidad = Gtk.SpinButton(adjustment=ajusteCantidad, digits=0)

        etiquetaPrecio = Gtk.Label(label="Precio:", xalign=0)
        ajustePrecio = Gtk.Adjustment(lower=0.0, upper=100000.0, step_increment=0.01)
        self.selectorPrecio = Gtk.SpinButton(adjustment=ajustePrecio, digits=2)

        # Añadir componentes a la cuadrícula
        cuadriculaContenedor.attach(etiquetaNombre, 0, 0, 1, 1)
        cuadriculaContenedor.attach(self.entradaNombre, 1, 0, 1, 1)
        cuadriculaContenedor.attach(etiquetaDescripcion, 0, 1, 1, 1)
        cuadriculaContenedor.attach(self.entradaDescripcion, 1, 1, 1, 1)
        cuadriculaContenedor.attach(etiquetaCantidad, 0, 2, 1, 1)
        cuadriculaContenedor.attach(self.selectorCantidad, 1, 2, 1, 1)
        cuadriculaContenedor.attach(etiquetaPrecio, 0, 3, 1, 1)
        cuadriculaContenedor.attach(self.selectorPrecio, 1, 3, 1, 1)

        # Si estamos en modo edición, rellenamos los campos
        if esModoEdicion:
            self.identificadorProducto = productoSeleccionado[0]
            self.entradaNombre.set_text(productoSeleccionado[1])
            self.entradaDescripcion.set_text(productoSeleccionado[2])
            self.selectorCantidad.set_value(productoSeleccionado[3])
            self.selectorPrecio.set_value(productoSeleccionado[4])
        else:
            self.identificadorProducto = None

        self.show_all()

    def obtenerDatos(self):
        """Recupera los datos introducidos en el formulario."""
        return {
            "id": self.identificadorProducto,
            "nombre": self.entradaNombre.get_text(),
            "descripcion": self.entradaDescripcion.get_text(),
            "cantidad": self.selectorCantidad.get_value_as_int(),
            "precio": self.selectorPrecio.get_value()
        }

    def validarDatos(self):
        """Valida los datos del formulario."""
        datosFormulario = self.obtenerDatos()
        if not datosFormulario["nombre"].strip():
            self.mostrarMensajeError("El campo 'Nombre' no puede estar vacío.")
            return False
        return True

    def mostrarMensajeError(self, mensajeError):
        """Muestra un diálogo de error."""
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