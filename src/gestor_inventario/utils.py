import os

def obtenerRutaBaseDatos():
    """
    Retorna la ruta absoluta al archivo de la base de datos.
    Se guarda en la carpeta del usuario para evitar problemas de permisos.
    """
    directorioDatos = os.path.join(os.path.expanduser("~"), ".gestor_inventario")
    if not os.path.exists(directorioDatos):
        os.makedirs(directorioDatos)
    return os.path.join(directorioDatos, "inventario.db")