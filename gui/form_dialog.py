
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FormDialog(Gtk.Dialog):
    """
    Diálogo para añadir o editar un producto.
    """
    def __init__(self, parent, producto=None):
        """
        Constructor del diálogo.

        :param parent: La ventana padre.
        :param producto: Un objeto (lista o tupla) con los datos del producto
                         si se está en modo edición. Formato:
                         (id, nombre, descripcion, cantidad, precio)
        """
        is_edit_mode = producto is not None
        title = "Editar Produto" if is_edit_mode else "Engadir Novo Produto"

        super().__init__(title=title, transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE, Gtk.ResponseType.OK
        )

        self.set_default_size(400, 250)
        self.set_border_width(10)

        grid = Gtk.Grid(column_spacing=10, row_spacing=10, margin=10)
        content_area = self.get_content_area()
        content_area.add(grid)

        # Campos del formulario
        lbl_nombre = Gtk.Label(label="Nome:", xalign=0)
        self.txt_nombre = Gtk.Entry()

        lbl_desc = Gtk.Label(label="Descrición:", xalign=0)
        self.txt_desc = Gtk.Entry()

        lbl_cantidad = Gtk.Label(label="Cantidade:", xalign=0)
        adj_cantidad = Gtk.Adjustment(lower=0, upper=10000, step_increment=1)
        self.spin_cantidad = Gtk.SpinButton(adjustment=adj_cantidad, digits=0)

        lbl_precio = Gtk.Label(label="Prezo:", xalign=0)
        adj_precio = Gtk.Adjustment(lower=0.0, upper=100000.0, step_increment=0.01)
        self.spin_precio = Gtk.SpinButton(adjustment=adj_precio, digits=2)

        # Añadir widgets al grid
        grid.attach(lbl_nombre, 0, 0, 1, 1)
        grid.attach(self.txt_nombre, 1, 0, 1, 1)
        grid.attach(lbl_desc, 0, 1, 1, 1)
        grid.attach(self.txt_desc, 1, 1, 1, 1)
        grid.attach(lbl_cantidad, 0, 2, 1, 1)
        grid.attach(self.spin_cantidad, 1, 2, 1, 1)
        grid.attach(lbl_precio, 0, 3, 1, 1)
        grid.attach(self.spin_precio, 1, 3, 1, 1)

        # Si estamos en modo edición, rellenamos los campos
        if is_edit_mode:
            self.producto_id = producto[0]
            self.txt_nombre.set_text(producto[1])
            self.txt_desc.set_text(producto[2])
            self.spin_cantidad.set_value(producto[3])
            self.spin_precio.set_value(producto[4])
        else:
            self.producto_id = None

        self.show_all()

    def get_data(self):
        """
        Recupera los datos introducidos en el formulario.

        :return: Un diccionario con los datos del producto.
        """
        return {
            "id": self.producto_id,
            "nombre": self.txt_nombre.get_text(),
            "descripcion": self.txt_desc.get_text(),
            "cantidad": self.spin_cantidad.get_value_as_int(),
            "precio": self.spin_precio.get_value()
        }

    def validate_data(self):
        """
        Valida los datos del formulario. Por ahora, solo comprueba que
        el nombre no esté vacío.

        :return: True si los datos son válidos, False en caso contrario.
        """
        data = self.get_data()
        if not data["nombre"].strip():
            self.show_error_message("O campo 'Nome' non pode estar baleiro.")
            return False
        return True

    def show_error_message(self, message):
        """
        Muestra un diálogo de error.

        :param message: El mensaje de error a mostrar.
        """
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CANCEL,
            text="Erro de validación"
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()
