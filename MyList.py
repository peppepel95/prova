from Progetto1.AbstractMyList import AbstractMyList


class Node:
    def __init__(self, val, next=None, prev=None):
        self._data = val
        self.next = next
        self.prev = prev


class MyList(AbstractMyList):
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def append(self, x):
        node = Node(x)

        if self._size == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._size += 1

    def __getitem__(self, i):

        if i < 0:
            i = self._size + i
        if i < 0 or i > self._size - 1:
            raise Exception("Out of range")

        if i < self._size / 2:

            temp = self._head
            j = 0

            while temp.next != None:
                if j == i:
                    break
                else:
                    j += 1
                    temp = temp.next

            return temp._data

        else:
            temp = self._tail
            j = self._size - 1

            while temp.prev != None:
                if j == i:
                    break
                else:
                    j -= 1
                    temp = temp.prev

            return temp._data

    def _getNodeAtIndex(self, i):

        i = self._inRange(i)

        if i < self._size / 2:

            temp = self._head
            j = 0

            while temp.next != None:
                if j == i:
                    break
                else:
                    j += 1
                    temp = temp.next

            return temp

        else:
            temp = self._tail
            j = self._size - 1

            while temp.prev != None:
                if j == i:
                    break
                else:
                    j -= 1
                    temp = temp.prev

            return temp

    def pop(self, i=None):

        if i is not None:
            nodo = self._getNodeAtIndex(i)
            if i < 0:
                i = self._size + i

            if i == 0:
                val = self._head._data
                newHead = self._head.next
                del self._head
                self._head = newHead
                return val

            if i == self._size - 1:
                val = self._tail._data
                newTail = self._tail.prev
                del self._tail
                self._tail = newTail
                self._tail.next = None
                return val

            temp1 = nodo.prev
            temp2 = nodo.next
            val = nodo._data
            temp1.next = temp2
            temp2.prev = temp1
            del nodo

        else:
            val = self._tail._data
            temp = self._tail.prev
            del self._tail
            self._tail = temp
            self._tail.next = None

        return val

    def count(self, x):
        temp = self._head
        j = 0
        count = 0

        while temp.next != None:
            j += 1
            if (temp._data == x):
                count += 1
            temp = temp.next

        return count

    def _inRange(self, i):
        if i < 0:
            i = self._size + i
        if i < 0 or i > self._size - 1:
            raise Exception("Out of range")

        return i

    def reverse(self):
        pass

    def extend(self, list):
        """Estende la lista appendendo gli elementi del parametro list"""

    def insert(self, i, x):
        """Inserisce l'elemento x alla posizione i"""

    def remove(self, x):
        """Rimuove la prima occorrenza dell'elemento x all'interno della lista, genera una eccezione in caso di assenza di x nella lista"""

    def index(self, x, start=0, end=None):
        """Ritorna l'indice della prima occorrenza dell'elemento x nella lista
        (compreso tra start ed end, con start ed end impostati di default rispettivamente a 0 e size - 1),
         genera una eccezione in caso di assenza di x nella lista"""

    def sort(cmp=None, key=None, reverse=False):
        """Ordina gli elementi della lista in place (gli argonemnti possono essere utilizzati per ordinamenti personallizati)."""

    def clear(self):
        """rimuove gli elementi dalla lista"""

    def copy(self):
        """Ritorna una deepCopy"""


list = MyList()

list.append(1)
list.append(3)
list.append(5)
list.append(7)
list.append(9)
print(list[-2])
print(list.pop(-2))