from Progetto_1.MyList import MyList
import sys

def verificaLista(lista, name):
    print("La ", name, " contiene: ", lista)
    # test di append
    print("Inserimento di 5 alla fine della ", name)
    lista.append(5)
    print("La ", name, " contiene: ", lista)
    # test di extend
    print("Estensione di ", name, " con [0,4,3]")
    l = [0, 4, 3]
    lista.extend(l)
    print("La ", name, " contiene: ", lista)
    # test di count
    print("Conta le occorrenze di 5 nella ", name)
    count = lista.count(5)
    print("5 occorre ", count, " volte")
    # test di index e __len__
    print("Restituisci la posizione di 5 e poi di 7 nella ", name)
    try:
        index = lista.index(5)
        print("Posizione di 5: ", index)
    except Exception as e:
        print(e)
    try:
        index = lista.index(7)
        print("Posizione di 7: ", index)
    except Exception as e:
        print(e)
    try:
        print("Cerca 5 nelle ultime due posizioni di ", name)
        start = (lista.__len__()) - 2
        end = (lista.__len__()) - 1
        index = lista.index(5, start, end)
        print("Risultato: ", index)
    except Exception as e:
        print(e)
    # test di insert
    print("Inserimento di 12 in posizione 1 in ", name)
    lista.insert(1, 12)
    print("Inserimento di 9 nella posizione -2")
    lista.insert(-2, 9)
    print("La ", name, " contiene: ", lista)
    # test di remove
    print("Rimozione di 4 da ", name)
    lista.remove(4)
    print("La ", name, " contiene: ", lista)
    # rimuovi l'ultimo elemento della lista
    print("Rimuovi l'ultimo elemento di ", name)
    print("Elemento rimosso: ", lista.pop())
    print("La ", name, " contiene: ", lista)
    # prova __add__
    list3 = lista + lista
    print("Lista 1 + Lista 2 = ", list3)
    # prova copy
    list3 = lista.copy()
    print("Crea copia di Lista 1 in Lista 3: ", list3)
    list3.insert(0, 10)
    print("La Lista 3 contiene: ", list3)
    # prova __eq__
    print(name," è uguale a Lista 3? ", lista == list3)
    # prova __ne__
    print(name," è diversa da Lista 3? ", lista != list3)
    # prova __lt__
    print(name," è minore di Lista 3? ", lista < list3)
    # prova __le__
    print(name," è minore o uguale di Lista 3? ", lista <= list3)
    # prova __gt__
    print(name," è maggiore di Lista 3? ", lista > list3)
    # prova __ge__
    print(name," è maggiore o uguale a Lista 3? ", lista >= list3)
    #  prova clear
    list3.clear()
    print("Distruggi la Lista 3: ", list3)
    # prova reverse
    lista.reverse()
    print("Inverti gli elementi della copia di Lista 1: ", lista)
    # prova sort
    lista.sort()
    print("Lista 1 ordinata: ", lista)
    lista.suffix_iterative()


list1 = MyList()
list2 = MyList(list1)
verificaLista(list1, "Lista 1")
verificaLista(list2, "Lista 2")

