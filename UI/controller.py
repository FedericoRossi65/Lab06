import flet as ft

from UI.alert import AlertManager
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view
        self._alert = self._view.alert


    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler

    def mostro_automobili(self,e):
        auto = self._model.get_automobili() # prendo dal model la lista di automobili
        self._view.lista_auto.controls.clear() # ripulisco la lista

        for a in auto:
            self._view.lista_auto.controls.append(ft.Text(f'{a}')) # aggiorno la lista auto nella view con le auto prese dalla lista auto
        self._view.update() # aggiorno la pagina

    def mostra_modelli(self,e):

        self._view.lista_auto_ricerca.controls.clear() # ripulisco la lista

        modello = (self._view.input_modello_auto.value.strip())
        lista_auto = self._model.cerca_automobili_per_modello(modello)
        if not lista_auto: # controllo se l'auto è peresente nel catalago se non lo è scateno un alert
            self._alert.show_alert('⚠️ Auto non presente nel catalogo')
        else:
             # nota bene : alla funzione cercaaoutopermodello devo passare un il parametro modello
             for a in lista_auto:
                self._view.lista_auto_ricerca.controls.append(ft.Text(f'{a}'))
        self._view.update()




