# Reorganización do Proxecto e Guía de Publicación

Este documento resume os cambios realizados para profesionalizar a estrutura do proxecto e os pasos necesarios para publicalo en PyPI.

## Cambios Realizados

1.  **Estrutura de Paquete Estándar**: Moveuse todo o código a `src/gestor_inventario/` para cumprir cos estándares de Python.
2.  **Eliminación de Hacks de Path**: Elimináronse os `sys.path.append('src')`. Agora o código utiliza importacións absolutas (ex: `from gestor_inventario.gui...`).
3.  **Persistencia de Datos**: A base de datos xa non se crea na carpeta de execución, senón en `~/.gestor_inventario/` para evitar problemas de permisos ao ser instalado como paquete.
4.  **Configuración de Empaquetado**: Creouse `pyproject.toml` con `hatchling` como motor de construción.
5.  **Punto de Entrada CLI**: Configurouse o comando `xestor-inventario` para que a aplicación poida executarse directamente desde a terminal tras a instalación.

---

## Guía para Publicar en PyPI desde Cero

Sigue estes pasos para xerar os ficheiros de distribución e subilos a PyPI.

### 1. Preparar o contorno
Asegúrate de ter instaladas as ferramentas necesarias:
```bash
py -m pip install --upgrade build twine
```

### 2. Limpar versións anteriores (opcional)
Se xa fixeches builds antes, borra as carpetas `dist/` e `build/` para evitar confusións.

### 3. Construír o paquete (Build)
Este comando xerará os ficheiros `.whl` (Wheel) e `.tar.gz` (Source Distribution) na carpeta `dist/`.
```bash
py -m build
```

### 4. Verificar o paquete
É recomendable verificar que a construción é correcta:
```bash
py -m twine check dist/*
```

### 5. Subir a PyPI (Push)
Para subir o paquete ao repositorio oficial, necesitarás unha conta en [PyPI](https://pypi.org/) e crear un API Token.

**Subida a TestPyPI (Recomendado para probar):**
```bash
py -m twine upload --repository testpypi dist/*
```

**Subida a PyPI (Produción):**
```bash
py -m twine upload dist/*
```

*Nota: Cando che pida o usuario, escribe `__token__`. No contrasinal, pega o teu API Token (incluíndo o prefixo `pypi-`).*

---

## Como probar a instalación localmente
Antes de subir a PyPI, podes probar se todo funciona instalando o teu propio cartafol:
```bash
pip install .
```
E logo executa:
```bash
xestor-inventario
```
