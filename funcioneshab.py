"""
Aquí vendrán todas las funciones que afectan a la ¡gestión de los
habitaciones
Limpiarentry vaciará el contenido de los entry

"""

import conexion, sqlite3, variables

def insertarhab(fila):
    try:
        conexion.cur.execute('insert into habitacion(numero,tipo,prezo,libre) values(?,?,?,?)', fila)
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listarhab():
    try:
        conexion.cur.execute('select * from habitacion')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentry(fila):
    for i in range(len(fila)):
        fila[i].set_text('')

def listadohab(listhab):
    try:
        variables.listado = listarhab()
        variables.listhab.clear()
        for registro in variables.listado:
            listhab.append(registro)
    except:
        print("error en cargar treeview de hab")

def bajahab(numhab):
    try:
        conexion.cur.execute('delete from habitacion where numero = ?', (numhab,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifhab(registro, numhab):
    try:
        conexion.cur.execute('update habitacion set tipo = ?, prezo = ?, libre = ? where numero = ?',
                             (registro[1], registro[0], registro[2], numhab))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadonumhab(self):
    try:
        conexion.cur.execute('select numero from habitacion')
        listado = conexion.cur.fetchall()
        variables.listcmbhab.clear()
        for row in listado:
            variables.listcmbhab.append(row)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadonumhabres():
    try:
        conexion.cur.execute('select numero from habitacion')
        lista = conexion.cur.fetchall()
        return lista
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def cambiaestadohab(libre, numhabres):
    try:
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (libre[0], numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
       print(e)
       conexion.conex.rollback()

def cargarprecio(numhab):
    try:
        conexion.cur.execute('select prezo from habitacion where numero = ?', (numhab,))
        prezo = conexion.cur.fetchone()
        return prezo

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifhabres(numhabres):
    try:
        libre = 'SI'
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (libre, numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
       print(e)
       conexion.conex.rollback()