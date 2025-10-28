from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        cnx = get_connection()
        cursore = cnx.cursor()
        query = """SELECT * FROM automobile"""
        cursore.execute(query)
        lista_automobili = []
        for row in cursore:
            aTemp = Automobile(row[0], row[1], row[2], row[3], row[4], row[5])
            lista_automobili.append(aTemp)
        cursore.close()
        cnx.close()
        return lista_automobili





    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """

        cnx = get_connection()
        cursore = cnx.cursor()
        query = f"""SELECT * FROM automobile
                    WHERE modello = '{modello}' """
        cursore.execute(query)
        lista_auto_modelli = []
        for row in cursore:
            aTemp = Automobile(row[0], row[1], row[2], row[3], row[4], row[5])
            lista_auto_modelli.append(aTemp)
        cursore.close()
        cnx.close()
        return lista_auto_modelli

