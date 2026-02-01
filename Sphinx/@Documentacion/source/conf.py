# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# Añadir la ruta absoluta a la carpeta 'src' para que Sphinx pueda encontrar el código.
# La carpeta 'src' está en la raíz del proyecto, un nivel por encima de '@Documentacion\source'.
sys.path.insert(0, 'C:\\Users\\samue\\Documents\\dam2\\DI-VARIOS_\\Random\\Sphinx\\src')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Proyecto de Documentación Gemini'
copyright = '2026, Gemini CLI'
author = 'Gemini CLI'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Añadir extensiones útiles para la documentación.
extensions = [
    'sphinx.ext.autodoc',     # Para documentar el código fuente automáticamente.
    'sphinx.ext.napoleon',    # Para soportar docstrings de Google y NumPy.
    'sphinx.ext.viewcode',    # Para enlazar la documentación con el código fuente.
    'sphinx.ext.todo',        # Para usar la directiva '.. todo::'.
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

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoifnot` produce output, else they produce nothing.
todo_include_todos = True