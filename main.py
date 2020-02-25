import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

import eventos, conexion, variables
import funcionescli, funcioneshab, funcionesreser,funcionesvar

'''
el main contiene los elementos necesarios para lanzar la aplicación
así como la declaración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas

'''

class Empresa:
    def __init__(self):
        #iniciamos la libreria Gtk
        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')

        #cargamos los widgets con algún evente asociado o que son referenciados
        vprincipal = self.b.get_object('venPrincipal')
        self.vendialog = self.b.get_object('venDialog')
        variables.venacercade = self.b.get_object('venAcercade')
        variables.panel = self.b.get_object('Panel')
        variables.venprezos = self.b.get_object('venPrezos')
        variables.filechooserbackup = self.b.get_object('fileChooserbackup')
        menubar = self.b.get_object('menuBar').get_style_context()
        datagridfinfac = self.b.get_object('datagridfinfac').get_style_context()

        #declaracion de wigdets
        entdni = self.b.get_object('entDni')
        entapel = self.b.get_object('entApel')
        entnome = self.b.get_object('entNome')
        entdatacli = self.b.get_object('entDatacli')
        lblerrdni = self.b.get_object('lblErrdni')
        lblcodcli = self.b.get_object('lblCodcli')
        lblnumnoches = self.b.get_object('lblNumnoches')
        lbldirbackup = self.b.get_object('lblFolderbackup')
        lbldnires = self.b.get_object('lblDnires')
        lblapelres = self.b.get_object('lblApelres')
        lbldnifac = self.b.get_object('lbldnifac')
        lblapelfac = self.b.get_object('lblapelfac')
        lblcodrfac = self.b.get_object('lblcodrfac')
        lblnomefac = self.b.get_object('lblnomefac')
        lblhabfac = self.b.get_object('lblhabfac')
        lbltotalhab = self.b.get_object('lbltotalhab')
        lblnumnochesfac = self.b.get_object('lblnumnochesfac')
        lblpreciohabfac = self.b.get_object('lblpreciohabfac')
        lblfechafac = self.b.get_object('lblfechafac')
        lblhabser = self.b.get_object('lblHabser')
        lblsercodres = self.b.get_object('lblSercodres')
        variables.vencalendar = self.b.get_object('venCalendar')
        variables.vendialogsalir = self.b.get_object('vendialogSalir')
        variables.calendar = self.b.get_object('Calendar')
        variables.filacli = (entdni, entapel, entnome, entdatacli)
        variables.listclientes = self.b.get_object('listClientes')
        variables.treereservas = self.b.get_object('treeReservas')
        variables.listreservas = self.b.get_object('listReservas')
        variables.treeclientes = self.b.get_object('treeClientes')
        variables.treeservicios = self.b.get_object('treeServicios')
        variables.listservicios = self.b.get_object('listServ')
        variables.menslabel = (lblerrdni, lblcodcli, lblnumnoches, lbldirbackup, lbldnires, lblapelres)
        variables.mensfac = (lbldnifac, lblapelfac, lblcodrfac, lblnomefac,lblhabfac, lblnumnochesfac, lblpreciohabfac,
                             lbltotalhab, lblfechafac)
        variables.mensserv = (lblhabser, lblsercodres)

        #widgets habitaciones
        entnumhab = self.b.get_object('entNumhab')
        entprezohab = self.b.get_object('entPrezohab')
        rbtsimple = self.b.get_object('rbtSimple')
        rbtdoble = self.b.get_object('rbtDoble')
        rbtfamily = self.b.get_object('rbtFamily')
        variables.treehab = self.b.get_object('treeHab')
        variables.listhab = self.b.get_object('listHab')
        variables.filahab = (entnumhab, entprezohab)
        variables.filarbt = (rbtsimple, rbtdoble, rbtfamily)
        variables.listcmbhab = self.b.get_object('listcmbHab')
        variables.cmbhab = self.b.get_object('cmbNumres')
        variables.switch = self.b.get_object('switch')

        #widgtes reservas
        entdatain = self.b.get_object('entDatain')
        entdataout = self.b.get_object('entDataout')
        variables.filareserva = (entdni, entapel, entdatain, entdataout)
        lblsubtotal = self.b.get_object('lblSubtotal')
        lbliva = self.b.get_object('lblIva')
        lbltotal = self.b.get_object('lblTotal')
        variables.linfacfinal = (lblsubtotal, lbliva, lbltotal)

        #gestion prezos e servizos
        entprezopar = self.b.get_object('entPrezoPark')
        entprezopc =  self.b.get_object('entPrezoPC')
        entprezodes = self.b.get_object('entPrezoDes')
        entotrobasico = self.b.get_object('entOtrobasico')
        entprezootrobasico = self.b.get_object('entPrezoOtrobasico')
        variables.otrobasico = (entotrobasico, entprezootrobasico)
        variables.prezos = (entprezopar, entprezodes, entprezopc)
        rbtdes = self.b.get_object('rbtDes')
        rbtcom  = self.b.get_object('rbtCom')
        chkpark = self.b.get_object('chkPark')
        variables.filarbtser = ( rbtdes, rbtcom, chkpark )
        for i in range (0,32):
            registro = "lblf"+str(i)
            registro = self.b.get_object('lblf'+str(i))
            variables.linefactura.append(registro)

        #conectamos
        self.b.connect_signals(eventos.Eventos())

        #conexion estilos

        self.set_style()
        menubar.add_class('menuBar')
        datagridfinfac.add_class('datagridfinfac')
        '''
        for i in range(len(variables.menserror)):
            variables.menserror[i].add_class('label')
        '''
        s = Gdk.Screen.get_default()
        a = s.get_width()
        b = s.get_height()
        vprincipal.show_all()
        vprincipal.resize(a,b)
        vprincipal.maximize()
        conexion.Conexion().abrirbbdd()
        funcionesreser.listadores()
        funcioneshab.listadonumhab(self)
        funcionescli.listadocli(variables.listclientes)
        funcioneshab.listadohab(variables.listhab)
        funcionesvar.controlhab()


    def set_style(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('estilos.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__=='__main__':
    main = Empresa()
    Gtk.main()

