import conexion, sqlite3, variables
import funcioneshab

def cargargridfactura(datosfactura):

    variables.mensfac[5].set_text(str(datosfactura[1]))
    precio = funcioneshab.cargarprecio(str(datosfactura[3]))
    variables.mensfac[6].set_text(str(precio[0]))
    totalhab = float(precio[0])*float(datosfactura[1])
    variables.mensfac[7].set_text(str(totalhab))
    variables.mensfac[8].set_text(str(datosfactura[4]))




