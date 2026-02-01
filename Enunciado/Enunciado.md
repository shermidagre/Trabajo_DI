Este é un modelo de ficheiro **README.md** profesional e estruturado para o teu proxecto. Está deseñado para ser claro, fácil de ler e para cumprir con tódolos puntos que require o enunciado do exercicio.

---

# 📦 Xestor de Inventario con Python e GTK3

Este proxecto consiste nunha aplicación de escritorio desenvolvida en **Python** utilizando a libraría **GTK3**. A aplicación permite a xestión completa de información (CRUD) sobre unha temática específica, garantindo unha interface intuitiva, validación de datos e persistencia nunha base de datos.

## 🚀 Características principais

* **Interface Gráfica Avanzada:** Construída en GTK3 para contornos Linux (Ubuntu).
* **Operacións CRUD Completas:** Crear, Ler, Actualizar e Borrar rexistros.
* **Control de Erros:** Validación de entradas e diálogos de confirmación para accións críticas.
* **Vista de Datos:** Uso de `Gtk.TreeView` para visualizar e seleccionar información de forma eficiente.
* **Documentación Automatizada:** Uso de **Sphinx** para xerar documentación técnica a partir de *docstrings*.

---

## 🛠️ Requisitos do Sistema

Para executar esta aplicación, necesitas ter instalado:

* **Python 3.x**
* **PyGObject (GTK3)**
* **SQLite3** (ou o motor de BD correspondente)
* **Sphinx** (para xerar a documentación)

### Instalación de dependencias en Ubuntu:

```bash
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install sphinx sphinx-rtd-theme

```

---

## 📁 Estrutura do Proxecto

O proxecto organízase da seguinte forma para manter unha arquitectura limpa:

* `main.py`: Punto de entrada da aplicación.
* `conexionBD.py`: Módulo encargado da lóxica de conexión e consultas á base de datos.
* `gui/`: Carpeta que contén as clases das distintas fiestras e formularios.
* `docs/`: Documentación xerada por Sphinx.
* `tests/`: Deseño e execución de probas de software.

---

## 🖥️ Compoñentes da Interface

A aplicación conta con tres formularios principais que utilizan diversos widgets de GTK:

1. **Fiestra Principal:** Listado de rexistros mediante `Gtk.TreeView`.
2. **Formulario de Alta/Edición:** Uso de `Gtk.Entry`, `Gtk.ComboBox`, `Gtk.CheckButton` e `Gtk.RadioButton`.
3. **Panel de Configuración/Detalles:** Unha terceira vista para xestión secundaria (ex: categorías ou estatísticas) utilizando `Gtk.TextView`.

---

## 📖 Documentación

O código está amplamente documentado seguindo os estándares de Python. Para xerar a páxina web coa documentación técnica, executa:

```bash
cd docs
make html

```

Isto creará unha carpeta `_build/html` onde poderás abrir o ficheiro `index.html` no teu navegador.

---

## 🧪 Probas de Software

Deseñáronse probas para asegurar o correcto funcionamento de:

* Conexión exitosa co módulo `conexionBD.py`.
* Inserción de datos con campos baleiros (validación de erros).
* Diálogos de confirmación ao eliminar un rexistro.
* Comprobación de que os botóns se activan/desactivan correctamente segundo o contexto.

---
