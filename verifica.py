from Progetto1.MyList import MyList


def verificaLista(list, name):
    print("La ", name, " contiene: ", list)
    # test di append
    print("Inserimento di 5 alla fine della ", name)
    list.append(5)
    print("La ", name, " contiene: ", list)
    # test di extend
    print("Estensione di ", name, " con [0,4,3]")
    l = [0, 4, 3]
    list.extend(l)
    print("La ", name, " contiene: ", list)
    # test di count
    print("Conta le occorrenze di 5 nella ", name)
    count = list.count(5)
    print("5 occorre ", count, " volte")
    # test di index e __len__
    print("Restituisci la posizione di 5 e poi di 7 nella ", name)
    index = list.index(5)
    print("Posizione di 5: ", index)
    index = list.index(7)
    print("Posizione di 7: ", index)
    print("Cerca 5 nelle ultime due posizioni di ", name)
    start = (list.__len__()) - 2
    end = (list.__len__()) - 1
    index = list.index(5, start, end)
    print("Risultato: ", index)
    # test di insert
    print("Inserimento di 12 in posizione 1 in ", name)
    list.insert(1, 12)
    print("Inserimento di 9 nella posizione -2")
    list.insert(-2, 9)
    print("La ", name, " contiene: ", list)
    # test di remove
    print("Rimozione di 4 da ", name)
    list.remove(4)
    print("La ", name, " contiene: ", list)
    # rimuovi l'ultimo elemento della lista
    print("Rimuovi l'ultimo elemento di ", name)
    print("Elemento rimosso: ", list.pop())
    print("La ", name, " contiene: ", list)


list1 = MyList()
list2 = MyList(list1)
verificaLista(list1, "Lista 1")
verificaLista(list2, "Lista 2")
# prova __add__
list3 = list1 + list2
print("Lista 1 + Lista 2 = ", list3)
# prova copy
list3 = list1.copy()
print("Crea copia di Lista 1 in Lista 3: ", list3)
list3.insert(0, 10)
print("La Lista 3 contiene: ", list3)
# prova __eq__
print("Lista 1 è uguale a Lista 3? ", list1 == list3)
# prova __ne__
print("Lista 1 è diversa da Lista 3? ", list1 != list3)
# prova __lt__
print("Lista 1 è minore di Lista 3? ", list1 < list3)
# prova __le__
print("Lista 1 è minore o uguale di Lista 3? ", list1 <= list3)
# prova __gt__
print("Lista 1 è maggiore di Lista 3? ", list1 > list3)
# prova __ge__
print("Lista 1 è maggiore o uguale a Lista 3? ", list1 >= list3)
#  prova clear
list3.clear()
print("Distruggi la Lista 3: ", list3)
# prova reverse
list1.reverse()
print("Inverti gli elementi della copia di Lista 1: ", list1)
# prova sort
list1.sort()
print("Lista 1 ordinata: ", list1)
list1.suffix_iterative()
