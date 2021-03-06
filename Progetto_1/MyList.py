from Progetto_1.AbstractMyList import AbstractMyList
from Progetto_1.QuickSort import quicksort


class Node:
    def __init__(self, val, next=None, prev=None):
        self._data = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return self._data


class MyList(AbstractMyList):
    def __init__(self, *args):

        self._size = 0
        self._head = None
        self._tail = None

        if (args.__len__() != 0):
            try:
                some_object_iterator = iter(args[0])
                self.extend(args[0])
            except IndexError:
                print('the obj is not iterable')

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

        if isinstance(i, int):
            pass
        elif isinstance(i, slice):
            return self._getSlice(i)
        else:
            raise TypeError("Invalid argument type")

        if i < 0:
            i = self._size + i
        if i < 0 or i > self._size - 1:
            raise IndexError("Out of range")

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

        if isinstance(i, int):

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
        else:
            raise TypeError("Invalid argument type")

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
                self._size -= 1
                return val

            if i == self._size - 1:
                val = self._tail._data
                newTail = self._tail.prev
                del self._tail
                self._tail = newTail
                self._tail.next = None
                self._size -= 1
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

        self._size -= 1
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

        if isinstance(i, int):
            if i < 0:
                i = self._size + i
            if i < 0 or i > self._size - 1:
                raise Exception("Out of range")

            return i
        else:
            raise TypeError("Invalid argument type")

    def __len__(self):
        return self._size

    def reverse(self):
        head = self._head
        tail = self._tail

        while head != tail and head.next != tail:
            head._data, tail._data = tail._data, head._data
            head = head.next
            tail = tail.prev

        if head.next == tail:
            head._data, tail._data = tail._data, head._data

    def __str__(self):
        temp = self._head
        stringa = "<"

        while temp is not None:
            stringa += str(temp._data)
            temp = temp.next
            if (temp != None):
                stringa += ","

        stringa += ">"
        return stringa

    def copy(self):
        newCopy = MyList()
        newCopy.extend(self)
        return newCopy

    def extend(self, list):
        for nodo in iter(list):
            self.append(nodo)

    def insert(self, i, x):
        # controllo il valore di i

        i = self._inRange(i)

        newNode = Node(x)

        # se la lista è vuota
        if self._size == 0:
            self._head = newNode
            self._tail = newNode
            newNode.next = None
            newNode.prev = None

        # se è un inserimento in coda
        if i == self._size:
            self.append(x)

        # se è un inserimento in testa
        elif i == 0:
            newNode.next = self._head
            self._head = newNode
            newNode.prev = None

        # se non è né un inserimento in testa né in coda
        else:
            nodo = self._getNodeAtIndex(i)
            prevNode = nodo.prev
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = nodo
            nodo.prev = newNode
        self._size += 1

    def remove(self, x):
        pos = 0

        node = self._head

        while node != None:
            if node._data == x:
                # eliminazione in testa
                if pos == 0:
                    if self._size == 1:
                        self._head = None
                        self._tail = None
                    else:
                        self._head = self._head.next
                        self._head.prev = None

                # eliminazione in coda
                elif pos == self._size - 1:
                    if pos == 0:
                        self._tail = None
                        self._head = None
                    else:
                        self._tail = self._tail.prev
                        self._tail.next = None
                else:
                    prevNode = node.prev
                    nextNode = node.next
                    prevNode.next = node.next
                    nextNode.prev = prevNode

                del node
                self._size -= 1
                break

            pos += 1
            node = node.next
        else:
            raise Exception("Elemento non presente")

    def index(self, x, start=None, end=None):
        """Ritorna l'indice della prima occorrenza dell'elemento x nella lista
        (compreso tra start ed end, con start ed end impostati di default rispettivamente a 0 e size - 1),
         genera una eccezione in caso di assenza di x nella lista"""

        if start != None:
            start = self._inRange(start)
        if end != None:
            end = self._inRange(end)

        if start == None:
            start = 0
        if end == None:
            end = self._size - 1

        if start > end:
            raise Exception("start è maggiore di end")

        pos = 0
        nodo = self._getNodeAtIndex(start)
        lun = end - start

        while nodo != None and pos <= lun:
            if nodo._data == x:
                return pos + start
            else:
                pos += 1
            nodo = nodo.next

        raise Exception("Valore non trovato")

    def clear(self):
        """rimuove gli elementi dalla lista"""
        if self._head is not None:
            pointer = self._head
            while pointer.next != None:
                prev = pointer
                pointer = pointer.next
                del prev
            self._head = None
            self._tail = None

    def sort(self, key=None, reverse=False):
        """Ordina gli elementi della lista in place (gli argonemnti possono essere utilizzati per ordinamenti personallizati)."""
        quicksort(self, 0, len(self) - 1, key, reverse)

    def __add__(self, other):
        """a = a + b + .."""
        lista = MyList()

        for val in self:
            lista.append(val)

        for val in other:
            lista.append(val)

        return lista

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __contains__(self, item):
        return self.index(item) >= 0

    def __delitem__(self, key):
        self.pop(key)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            pass
        elif isinstance(key, slice):
            self._setSlice(key, value)
            return
        else:
            raise TypeError("Invalid argument type")

        self._getNodeAtIndex(key)._data = value

    def __del__(self):
        self.clear()

    def __eq__(self, other):
        if other == None:
            return False
        else:
            if self._head == None:
                if other._head == None:
                    return True
                else:
                    return False
            else:
                if other._head == None:
                    return False
                else:
                    pointer1 = self._head
                    pointer2 = other._head
                    equals = True
                    while pointer1 != None and pointer2 != None and equals:
                        equals = pointer1._data == pointer2._data
                        pointer1 = pointer1.next
                        pointer2 = pointer2.next
                    if pointer1 == None or pointer2 == None:
                        return False
                    else:
                        return equals

    def __le__(self, other):
        return (self < other or self == other)

    def __lt__(self, other):
        if self == None or other == None:
            raise Exception
        else:
            pointer1 = self._head
            pointer2 = other._head
            cond = False
            while pointer1 != None and pointer2 != None:
                if pointer1._data < pointer2._data:
                    return True
                elif pointer1._data == pointer2._data:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                else:
                    return False
            if pointer1 == None:
                return True
            else:
                return False

    def __ne__(self, other):
        return not (self.__eq__(other))

    def __gt__(self, other):
        return not (self < other or self == other)

    def __ge__(self, other):
        return not self < other

    def _getSlice(self, sl):

        if isinstance(sl, slice):
            start = self._inRange(sl.start)
            stop = self._inRange(sl.stop)
            step = sl.step

            if start is None:
                start = 0
            if stop is None:
                stop = len(self) - 1
            if step is None:
                step = 1

            nodo = self._getNodeAtIndex(start)
            lista = MyList()

            i = 0

            while nodo is not None and i <= stop - start:
                if i == 0:
                    lista.append(nodo._data)
                else:
                    if step == 1:
                        lista.append(nodo._data)
                    else:
                        for val in range(0, step - 1):
                            if nodo is None:
                                break
                            i += 1
                            nodo = nodo.next

                        if nodo is not None:
                            lista.append(nodo._data)

                i += 1
                if nodo is not None:
                    nodo = nodo.next

            return lista

        else:
            raise TypeError("Invalid argument type")

    def _setSlice(self, sl, seq):

        if isinstance(sl, slice) and type(seq) in [str, list, tuple]:

            start = self._inRange(sl.start)
            stop = self._inRange(sl.stop)
            step = sl.step

            if start is None:
                start = 0
            if stop is None:
                stop = len(self) - 1
            if step is None:
                step = 1

            node = self._getNodeAtIndex(start)
            while start <= stop and node is not None:
                node._data = seq[start]
                start += step
                for i in range(0, step - 1):
                    if node is not None:
                        nodo = nodo.next
                    else:
                        break

        else:
            raise TypeError("Invalid argument type")


def suffix_iterative(lista):
    if lista != None:
        copy = lista.copy()
        result = MyList()
        result.append(MyList(copy))
        for i in range(0, lista.__len__() - 1):
            copy.pop(0)
            result.append(MyList(copy))
        result.append(MyList())
        result.reverse()

        return result
    else:
        return MyList()


def suffix_ric(lista):
    if len(lista) == 0:
        return [lista]

    lista1 = lista.copy()
    lista1.pop(0)

    return suffix_ric(lista1) + [lista]
