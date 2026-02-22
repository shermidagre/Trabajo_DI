import sqlite3 as dbapi

class ConexionBD:
    """Clase para realizar la conexión a una base de datos SQlite."""

    def __init__(self, rutaBaseDatos):
        """
        Crea las propiedades necesarias para el acceso a una base de datos y las inicializa.
        """
        self.rutaBaseDatos = rutaBaseDatos
        self.conexionActiva = None
        self.cursorActivo = None

    def conectarBaseDatos(self):
        """Método que crea la conexión de la base de datos."""
        try:
            if self.conexionActiva is None:
                if self.rutaBaseDatos is None:
                    print("La ruta de la base de datos es: None")
                else:
                    self.conexionActiva = dbapi.connect(self.rutaBaseDatos)
            else:
                print("Base de datos conectada: " + str(self.conexionActiva))

        except dbapi.StandardError as errorConexion:
            print("Error al hacer la conexión a la base de datos " + self.rutaBaseDatos + ": " + str(errorConexion))
        else:
            print("Conexión de base de datos realizada")

    def crearCursor(self):
        """Método que crea el cursor de la base de datos."""
        try:
            if self.conexionActiva is None:
                print("Creando el cursor: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    self.cursorActivo = self.conexionActiva.cursor()
                else:
                    print("El cursor ya está inicializado: " + str(self.cursorActivo))

        except dbapi.Error as errorCursor:
            print(errorCursor)
        else:
            print("Cursor preparado")

    def consultaSinParametros(self, consultaSql):
        """Retorna una lista con los registros de una consulta realizada sin pasarle parámetros."""
        listaResultados = list()
        try:
            if self.conexionActiva is None:
                print("Creando consulta: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    print("Creando consulta: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursorActivo.execute(consultaSql)
                    for filaRegistro in self.cursorActivo.fetchall():
                        listaResultados.append(filaRegistro)

        except dbapi.DatabaseError as errorConsulta:
            print("Error haciendo la consulta: " + str(errorConsulta))
            return None
        else:
            print("Consulta ejecutada")
            return listaResultados

    def consultaConParametros(self, consultaSql, *parametrosConsulta):
        """Retorna una lista con los registros de una consulta realizada pasándole los parámetros."""
        listaResultados = list()
        try:
            if self.conexionActiva is None:
                print("Creando consulta: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    print("Creando consulta: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursorActivo.execute(consultaSql, parametrosConsulta)
                    for filaRegistro in self.cursorActivo.fetchall():
                        listaResultados.append(filaRegistro)

        except dbapi.DatabaseError as errorConsulta:
            print("Error haciendo la consulta: " + str(errorConsulta))
            return None
        else:
            print("Consulta ejecutada")
            return listaResultados

    def añadirRegistro(self, insertarSql, *parametrosInsercion):
        try:
            if self.conexionActiva is None:
                print("Realizando inserción: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    print("Realizando inserción: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursorActivo.execute(insertarSql, parametrosInsercion)
                    self.conexionActiva.commit()

        except dbapi.DatabaseError as errorInsercion:
            print("Error haciendo la inserción: " + str(errorInsercion))
        else:
            print("Inserción ejecutada")

    def actualizarRegistro(self, actualizarSql, *parametrosActualizacion):
        try:
            if self.conexionActiva is None:
                print("Realizando actualización: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    print("Realizando actualización: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursorActivo.execute(actualizarSql, parametrosActualizacion)
                    self.conexionActiva.commit()

        except dbapi.DatabaseError as errorActualizacion:
            print("Error haciendo la actualización: " + str(errorActualizacion))
        else:
            print("Actualización ejecutada")

    def eliminarRegistro(self, eliminarSql, *parametrosEliminacion):
        try:
            if self.conexionActiva is None:
                print("Realizando borrado: Es necesario realizar la conexión a la base de datos previamente")
            else:
                if self.cursorActivo is None:
                    print("Realizando borrado: Es necesario realizar la creación del cursor previamente")
                else:
                    self.cursorActivo.execute(eliminarSql, parametrosEliminacion)
                    self.conexionActiva.commit()

        except dbapi.DatabaseError as errorBorrado:
            print("Error haciendo el borrado: " + str(errorBorrado))
        else:
            print("Borrado de registro ejecutado")

    def cerrarBaseDatos(self):
        """Cierra el cursor y la conexión de la base de datos si esta existe."""
        if self.cursorActivo is not None:
            self.cursorActivo.close()
        if self.conexionActiva is not None:
            self.conexionActiva.close()