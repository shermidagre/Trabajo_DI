import gi
try:
    gi.require_version('Gtk', '3.0')
except ValueError:
    pass # Si ya está cargada otra versión, evitamos que el proceso muera