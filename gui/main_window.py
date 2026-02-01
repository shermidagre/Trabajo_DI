
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

# Agregamos la ruta de la librería al path para poder importarla
sys.path.append('src')
from mi_libreria.conexionBD import ConexionBD
from gui.form_dialog import FormDialog


class MainWindow(Gtk.Window):
    """
    Ventana principal de la aplicación de gestión de inventario.
    Contiene el listado de productos y los botones de acción.
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
        
        # TreeView para mostrar los productos
        self.liststore = Gtk.ListStore(int, str, str, int, float)
        self.treeview = Gtk.TreeView(model=self.liststore)

        # Definimos y añadimos las columnas, mapeando a los índices correctos del ListStore
        # (id, nombre, descripcion, cantidad, precio)
        # column_titles = ["ID", "Nome", "Cantidade", "Prezo"]
        # for i, title in enumerate(column_titles):
        #    renderer = Gtk.CellRendererText()
        #    model_index = i if i < 2 else i + 1 # Esto saltaba 'descripcion'
        #    column = Gtk.TreeViewColumn(title, renderer, text=model_index)
        #    self.treeview.append_column(column)
        
        # Columnas explícitas para mayor claridad y control
        renderer_text = Gtk.CellRendererText()
        
        column_id = Gtk.TreeViewColumn("ID", renderer_text, text=0)
        self.treeview.append_column(column_id)

        column_nome = Gtk.TreeViewColumn("Nome", renderer_text, text=1)
        self.treeview.append_column(column_nome)

        column_cantidade = Gtk.TreeViewColumn("Cantidade", renderer_text, text=3)
        self.treeview.append_column(column_cantidade)

        column_prezo = Gtk.TreeViewColumn("Prezo", renderer_text, text=4)
        self.treeview.append_column(column_prezo)

        selection = self.treeview.get_selection()
        selection.connect("changed", self.on_selection_changed)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        scrolled_window.add(self.treeview)
        vbox.pack_start(scrolled_window, True, True, 0)

        # Caja para los botones
        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, False, True, 0)

        self.btn_add = Gtk.Button(label="Engadir")
        self.btn_add.connect("clicked", self.on_add_clicked)
        
        self.btn_edit = Gtk.Button(label="Editar")
        self.btn_edit.connect("clicked", self.on_edit_clicked)
        
        self.btn_delete = Gtk.Button(label="Eliminar")
        self.btn_delete.connect("clicked", self.on_delete_clicked)

        button_box.pack_start(self.btn_add, True, True, 0)
        button_box.pack_start(self.btn_edit, True, True, 0)
        button_box.pack_start(self.btn_delete, True, True, 0)

        # Desactivar botones de edición/borrado inicialmente
        self.btn_edit.set_sensitive(False)
        self.btn_delete.set_sensitive(False)

        self.load_data()

    def load_data(self):
        self.liststore.clear()
        db = None
        try:
            db = ConexionBD("inventario.db")
            db.conectaBD()
            db.creaCursor()
            productos = db.consultaSenParametros("SELECT id, nombre, descripcion, cantidad, precio FROM productos")
            if productos:
                for producto in productos:
                    self.liststore.append(list(producto))
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
        finally:
            if db:
                db.pechaBD()

    def on_add_clicked(self, widget):
        dialog = FormDialog(parent=self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK and dialog.validate_data():
            data = dialog.get_data()
            db = None
            try:
                db = ConexionBD("inventario.db")
                db.conectaBD()
                db.creaCursor()
                sql = "INSERT INTO productos (nombre, descripcion, cantidad, precio) VALUES (?, ?, ?, ?)"
                params = (data["nombre"], data["descripcion"], data["cantidad"], data["precio"])
                db.engadeRexistro(sql, *params)
                self.load_data()
            except Exception as e:
                print(f"Error al añadir el producto: {e}")
            finally:
                if db:
                    db.pechaBD()
        dialog.destroy()

    def on_edit_clicked(self, widget):
        model, tree_iter = self.treeview.get_selection().get_selected()
        if tree_iter is None:
            return

        selected_producto = list(model[tree_iter])
        
        dialog = FormDialog(parent=self, producto=selected_producto)
        response = dialog.run()

        if response == Gtk.ResponseType.OK and dialog.validate_data():
            data = dialog.get_data()
            db = None
            try:
                db = ConexionBD("inventario.db")
                db.conectaBD()
                db.creaCursor()
                sql = "UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=? WHERE id=?"
                params = (data["nombre"], data["descripcion"], data["cantidad"], data["precio"], data["id"])
                db.actualizaRexistro(sql, *params)
                self.load_data()
            except Exception as e:
                print(f"Error al actualizar el producto: {e}")
            finally:
                if db:
                    db.pechaBD()
        
        dialog.destroy()

    def on_delete_clicked(self, widget):
        model, tree_iter = self.treeview.get_selection().get_selected()
        if tree_iter is None:
            return

        producto_id = model[tree_iter][0] # El ID está en la primera columna del liststore
        producto_nombre = model[tree_iter][1]

        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text=f"¿Confirma a eliminación do produto '{producto_nombre}' (ID: {producto_id})?"
        )
        dialog.format_secondary_text("Esta acción non se pode desfacer.")
        
        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.YES:
            db = None
            try:
                db = ConexionBD("inventario.db")
                db.conectaBD()
                db.creaCursor()
                sql = "DELETE FROM productos WHERE id=?"
                db.borraRexistro(sql, producto_id)
                self.load_data()
            except Exception as e:
                print(f"Error al eliminar el producto: {e}")
            finally:
                if db:
                    db.pechaBD()

    def on_selection_changed(self, selection):
        """
        Activa o desactiva los botones 'Editar' y 'Eliminar' según si
        hay una fila seleccionada en el TreeView.
        """
        model, tree_iter = selection.get_selected()
        is_selected = tree_iter is not None
        self.btn_edit.set_sensitive(is_selected)
        self.btn_delete.set_sensitive(is_selected)