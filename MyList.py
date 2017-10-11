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
        if i < 0:
            i = self._size + i
        if i < 0 or i > self._size - 1:
            raise Exception("Out of range")
        return i

    def extend(self, list):
        for nodo in list:
            self.append(nodo)

    def insert(self, i, x):
        # controllo il valore di i

        if i == self._size:
            self.append(x)
            return

        i = self._inRange(i)

        newNode = Node(x)

        # se la lista è vuota
        if self._size == 0:
            self._head = newNode
            self._tail = newNode
            newNode.next = None
            newNode.prev = None

        # se è un inserimento in coda


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
        for node in self:
            if node == x:

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
                        self._tail.prev = None
                else:
                    prevNode = node.prev
                    nextNode = node.next
                    prevNode.next = node.next
                    nextNode.prev = prevNode
                del node
                self._size -= 1
                break
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

        pos = start
        node = self._getNodeAtIndex(start)
        if node is not None:
            while pos < end and node.next is not None:
                if node._data == x:
                    return pos
                pos += 1
                node = node.next
            raise Exception("Elemento non presente nella lista")
        raise Exception("Lista vuota")

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
            self._size = 0

    def __str__(self):
        if len(self) == 0:
            return "<>" \
                   ""
        stringa = "<"
        for elem in self:
            stringa += str(elem) + ","
        stringa = stringa[0:(len(stringa) - 1)] + ">"

        return stringa

    def __len__(self):
        return self._size

    def copy(self):
        newCopy = MyList()
        newCopy.extend(self)
        return newCopy

list = MyList()

list.append(1)
list.append(3)
list.append(5)
list.append(7)
list.append(9)
print(list)
print("-----------------------")
list1=list.copy()
list1.clear()
print(list1)
