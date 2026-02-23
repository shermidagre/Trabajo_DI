# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# Añadir la ruta absoluta a la carpeta 'src' para que Sphinx pueda encontrar el código.
# La carpeta 'src' está en la raíz del proyecto, un nivel por encima de '@Documentacion\source'.
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Gestor de Inventario'
copyright = '2026, Samuel'
author = 'Samuel'
version = '4.0'
release = '4.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Añadir extensiones útiles para la documentación.
extensions = [
    'sphinx.ext.autodoc',     # Para documentar el código fuente automáticamente.
    'sphinx.ext.napoleon',    # Para soportar docstrings de Google y NumPy.
    'sphinx.ext.viewcode',    # Para enlazar la documentación con el código fuente.
    'sphinx.ext.todo',        # Para usar la directiva '.. todo::'.
    'furo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Language configuration --------------------------------------------------
language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#
html_theme = "furo"

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    # Puedes personalizar colores específicos aquí
    "light_css_variables": {
        "color-brand-primary": "#2980b9",
        "color-brand-content": "#2980b9",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3498db",
        "color-brand-content": "#3498db",
    },
}

html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoifnot` produce output, else they produce nothing.
todo_include_todos = True

autodoc_mock_imports = [
    "gi",
    "gi.repository",
    "gi.repository.Gtk",
    "gi.repository.Gdk",
    "gestor_inventario.bd",
    "PyGObject",
]
# Ocultar las advertencias de objetos simulados (mocked)
autodoc_warningiserror = False
suppress_warnings = ['autodoc.mocked_object']