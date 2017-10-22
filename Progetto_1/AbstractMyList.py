from abc import ABCMeta, abstractmethod

class AbstractMyList(metaclass=ABCMeta):
    """classe astratta MyList"""

    @abstractmethod
    def append(self, x):
        """Aggiunge l'elemento x in coda alla lista"""

    @abstractmethod
    def extend(self, list):
        """Estende la lista appendendo gli elementi del parametro list"""

    @abstractmethod
    def insert(self, i, x):
        """Inserisce l'elemento x alla posizione i"""

    @abstractmethod
    def remove(self, x):
        """Rimuove la prima occorrenza dell'elemento x all'interno della lista, genera una eccezione in caso di assenza di x nella lista"""

    @abstractmethod
    def pop(self, i=None):
        """Se la i è specificata, rimuove l'elemento alla posizione i-esima e ritorna il valore associato a tale elemento,
        se i non è specificata, viene rimosso e ritornato l'ultimo elemento"""

    @abstractmethod
    def index(self, x, start = 0, end=None):
        """Ritorna l'indice della prima occorrenza dell'elemento x nella lista
        (compreso tra start ed end, con start ed end impostati di default rispettivamente a 0 e size - 1),
         genera una eccezione in caso di assenza di x nella lista"""

    @abstractmethod
    def count(self, x):
        """Ritorna il numero di occorrenze di x presenti nella lista"""

    @abstractmethod
    def sort(self, key=None, reverse=False):
        """Ordina gli elementi della lista in place (gli argonemnti possono essere utilizzati per ordinamenti personallizati)."""

    @abstractmethod
    def reverse(self):
        """Inverte gli elementi della lista in place."""

    @abstractmethod
    def clear(self):
        """rimuove gli elementi dalla lista"""

    @abstractmethod
    def copy(self):
        """Ritorna una deepCopy"""
