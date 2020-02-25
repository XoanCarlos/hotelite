import conexion
import sqlite3
import variables
from datetime import datetime

def limpiarentry(fila):

    for i in range(len(fila)):
        fila[i].set_text('')
    for i in range(len(variables.menslabel)):
        variables.menslabel[i].set_text('')
    variables.cmbhab.set_active(-1)
    for i in range(len(variables.mensfac)):
        variables.mensfac[i].set_text('')

def calculardias():
    diain = variables.filareserva[2].get_text()
    date_in = datetime.strptime(diain, '%d/%m/%Y').date()
    diaout = variables.filareserva[3].get_text()
    date_out = datetime.strptime(diaout, '%d/%m/%Y').date()
    noches = (date_out-date_in).days
    if noches <= 0:
        variables.menslabel[2].set_text('Check-Out debe ser posterior')
        variables.reserva = 0
    else:
        variables.reserva = 1
        variables.menslabel[2].set_text(str(noches))

def insertares(fila):
    try:
        conexion.cur.execute('insert into  reservas(dni, numhab, checkin, checkout, noches) values(?,?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadores():
    try:
        variables.listado = listares()
        variables.listreservas.clear()
        for registro in variables.listado:
            variables.listreservas.append(registro)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listares():
    try:
        conexion.cur.execute('select codreser, dni, numhab, checkin, checkout, noches from reservas order by codreser desc')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarapelcli(dni):
    try:
        conexion.cur.execute('select apel from clientes where dni = ?', (dni,))
        apel = conexion.cur.fetchone()
        conexion.conex.commit()
        return apel
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarnome(dni):
    try:
        conexion.cur.execute('select nome from clientes where dni = ?', (dni,))
        nome = conexion.cur.fetchone()
        conexion.conex.commit()
        return nome
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajareserva(cod):
    try:
        print(cod)
        conexion.cur.execute('delete from reservas where codreser = ?', (cod,))
        conexion.conex.commit()
        if variables.switch.get_active():
            libre = 'SI'
        else:
            libre = 'NO'
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def versilibre(numhab):
    try:
        conexion.cur.execute('select libre from habitacion where numero = ?', (numhab,))
        lista= conexion.cur.fetchone()
        conexion.conex.commit()
        if lista[0] == 'SI':
            return True
        else:
            return False
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifreserva(registro, codr):
    try:
        conexion.cur.execute('update reservas set dni = ?, numhab = ?, checkin = ?, checkout = ?, noches = ? where codreser = ?',
                             (registro[0], registro[1], registro[2], registro[3], registro[4], codr))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadoservicios(variable):
    try:
        conexion.cur.execute('select tipo, prezo from servicios where codres=?', (variable,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()