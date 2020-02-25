import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import eventos, variables, conexion


class EventosGenerales(eventos.Eventos):
    def __init__(self):
        variables.b.connect_signals(EventosGenerales)

    def on_acercade_activate(self, widget):
        try:
            variables.venacercade.show()
        except:
            print('error abrira acerca de')

    def on_btnCerrarabout_clicked(self, widget):
        try:
            variables.venacercade.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venacercade.hide()
        except:
            print('error abrir calendario')

    def on_menuBarsalir_activate(self, widget):
        try:
            self.salir()
        except:
            print('salir en menubar')

    def salir(self):
        try:
            conexion.Conexion.cerrarbbdd(self)
            # funcionesvar.cerrartimer()
            Gtk.main_quit()
        except:
            print('error función salir')

    def on_venPrincipal_destroy(self, widget):
        self.salir()

    def on_btnSalirtool_clicked(self, widget):
        variables.vendialogsalir.show()

    def on_btnCancelarsalir_clicked(self, widget):
        variables.vendialogsalir.connect('delete-event', lambda w, e: w.hide() or True)
        variables.vendialogsalir.hide()

    def on_btnAceptarsalir_clicked(self, widget):
        self.salir()