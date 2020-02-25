import os, threading, locale
from datetime import datetime
import time
import conexion, zipfile
import sqlite3
import variables, funcioneshab

def backup():
    try:
        conexion.Conexion().cerrarbbdd()
        backup = 'backup.zip'
        #destino = '/home/pruebas/copias/'
        copia = zipfile.ZipFile(backup, 'w')
        copia.write('empresa.sqlite', compress_type = zipfile.ZIP_DEFLATED)
        copia.close()
        neobackup = str(datetime.now()) + str(backup)
        os.rename(backup, neobackup)
        conexion.Conexion().abrirbbdd()
        return neobackup
    except:
        print('error backup')

def controlhab():
    variables.t = threading.Timer(0.5, controlhab)
    variables.t.daemon = True
    variables.t.start()
    fechahoy = time.strftime('%H:%M:%S')
    fechacontrol = '20:08:00'
    if str(fechacontrol) == str(fechahoy):
        actualizarhab()

def cerrartimer():
    variables.t.join(0)

'''
def controlhab():
    try:
        time_of_day = time.strftime("%H:%M:%S")
        target_time = '19:57:00'
        print(time_of_day)
        print(target_time)
        while True:
            while str(time_of_day) != str(target_time):
                time.sleep(.1)
            actualizarhab()
            while time_of_day == target_time:
                print('hola')
                time.sleep(.1)
    except:
        print('error control habitacion')

'''
def actualizarhab():
    print('hola actualizasdor de habitaciones')


def mostrarprezos():
    try:
        conexion.cur.execute('select prezopark, prezodes, prezopc from prezos')
        prezos = conexion.cur.fetchone()
        conexion.conex.commit()
        return prezos
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def actualizarprezos(registro):
    try:
        conexion.cur.execute('update prezos set prezopark = ?, prezodes= ?, prezopc = ?', (registro[0], registro[1], registro[2],))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def grabarserbasicos():
    try:
        print('Hola')
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def preciosbasicos():
    try:
        conexion.cur.execute('select * from prezos')
        listadoprezos = conexion.cur.fetchone()
        conexion.conex.commit()
        return listadoprezos

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def vertipohab(snumhab):
    try:
        conexion.cur.execute('select tipo from habitacion where numero = ?', (snumhab,))
        tipo = conexion.cur.fetchone()
        conexion.conex.commit()
        return tipo

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def altaserv(servicio):
    try:
        conexion.cur.execute('insert into servicios(codres, tipo, prezo) values(?,?,?)', servicio)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadoservicios(codr):
    try:
        conexion.cur.execute('select codser, tipo, prezo from servicios where codres = ?', (codr,))
        listaser = conexion.cur.fetchall()
        conexion.conex.commit()
        return listaser
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listaservicios(listserv):
    try:
        listado = listadoservicios(variables.codr)
        variables.listservicios.clear()
        for registro in listado:
            listserv.append(registro)
    except:
        print('error carga treeservicios')

def altaotrobasico(registro, codr):
    try:
        conexion.cur.execute('insert into servicios(codres, tipo, prezo) values (?,?,?)', (codr, registro[0], registro[1]))
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentservicios(fila):
    for i in range(len(fila)):
        fila[i].set_text('')

def cargalinefactura(grid):
    try:
        conexion.cur.execute('select tipo, prezo from servicios where codres =? ', (variables.codr,))
        listado = conexion.cur.fetchall()
        j = 0
        k = 3
        for i,valor in enumerate(listado):
            if  j % 4 == 0:
                grid[j].set_text(str(valor[0]))
                j += 4
                grid[k].set_text(str(valor[1]))
                k = j + 3
    except:
        print('cargar lineas factura')


def limpiarlinfact(fila):
    for i in range(len(fila)):
        fila[i].set_text('')

def bajaserv(codser):
    try:
        conexion.cur.execute('delete from servicios where codser = ?', (codser,))
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def sumafactura(codres, noches, numhab):
    try:

        subtotal = 0.00
        iva = 0.00
        total = 0.00
        prezo = funcioneshab.cargarprecio(numhab)
        alojamiento = float(prezo[0])*float(noches)
        conexion.cur.execute('select prezo from servicios where codres=?', (codres,))
        listado = conexion.cur.fetchall()
        for i in range(len(listado)):
            subtotal = subtotal + (float(listado[i][0]))
        subtotal = round(subtotal,2)
        iva = subtotal*0.21 + alojamiento*0.1
        iva = round(iva, 2)
        subtotal = subtotal + alojamiento
        total = subtotal + iva
        total = round(total, 2)
        variables.linfacfinal[0].set_text(str(subtotal)+' €')
        variables.linfacfinal[1].set_text(str(iva) + ' €')
        variables.linfacfinal[2].set_text(str(total) + ' €')
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()