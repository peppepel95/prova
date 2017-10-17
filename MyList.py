from Progetto1.AbstractMyList import AbstractMyList


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

        if(args != None):
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

    def __len__(self):
        return self._size

    def reverse(self):
        head = self._head
        tail = self._tail

        while(head != tail and head.next != tail):
            head._data, tail._data = tail._data, head._data
            head = head.next
            tail = tail.prev

        if(head.next == tail):
            head._data, tail._data = tail._data, head._data

    def __str__(self):
        temp = self._head
        stringa = "<"

        while temp != None:
            stringa += str(temp._data)
            temp = temp.next
            if(temp != None):
                stringa += ","

        stringa += ">"
        return stringa

    def copy(self):
        newCopy = MyList()
        newCopy.extend(self)
        return newCopy


    #codice longo


    def extend(self, list):
        for nodo in iter(list):
            self.append(nodo)

    def insert(self, i, x):
        # controllo il valore di i

        if i < 0:
            i = self._size + i
        if i < 0 or i > self._size:
            raise Exception("Out of range")

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

        if start > end:
            raise Exception("start è maggiore di end")

        if start == None:
            start = 0
        if end == None:
            end = self._size - 1

        pos = 0
        for node in self:
            if node._data == x:
                return pos
            pos += 1


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

    def sort(key=None, reverse=False):
        """Ordina gli elementi della lista in place (gli argonemnti possono essere utilizzati per ordinamenti personallizati)."""

    def __add__(self, other):
        """a = a + b + .."""
        lista = MyList()

        for val in self:
            lista.append(val)

        for val in other:
            lista.append(val)

        return list

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __contains__(self, item):
        return self.index(item) >= 0

    def __delitem__(self, key):
        self.pop(key)

    def __setitem__(self, key, value):
        self.insert(key,value)

    def __del__(self):
        self.clear()







list1 = MyList()

list1.append(1)
list1.append(3)
list1.append(5)
list1.append(7)
list1.append(9)
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

print("lista in -2:", list1[-2])
print("pop di -2:", list1.pop(-2))
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

print("elementi con for in:")
for i in list1:
    print(i, end=" ")
print()

print("\n**************************************************************\n")

print("reverse lista")
list1.reverse()
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

print("copia lista")
l = list1.copy()
l.append(11)
print("append a copia di 11")

print("lista", list1, "dim:", list1.__len__())
print("copia", l, "dim:", list1.__len__())

print("\n**************************************************************\n")

list1.insert(1,8)
list1.insert(3,6)
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

list1.remove(6)
print("Rimuovo 6 dalla lista")
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

del list1[1]
print(list1, "dim:", list1.__len__())

list1[1] = 50
print(list1, "dim:", list1.__len__())

print("\n**************************************************************\n")

l = MyList(list1)
list1.append(5)
l.append(5)
print(l)
