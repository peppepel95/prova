""""
0/1 Knapsak: problema dello zaino
definiamo:
P = Peso dello zaino
p = Vettore che contiene i pesi degli elementi xi
v = Vettore che contiene i valori degli elementi xi
"""""

def Knapsak_0_1 (p, v, P):
    if len(v) != len(p):
        raise ValueError("input errato")
    n_items = len(v)

    M = [[0] * (P+1) for k in range(n_items)] #matrice con P+1 colonne e n_items righe
    C = [[False] * (P+1) for k in range(n_items)]

    for i in range(0,n_items):                                          # ad ogni passo calcoliamo la soluzione M[i][peso]
                                                                        # ovvero il problema dello zaino considernado solo "i" elementi
        for peso in range(1,P+1):                                       # e uno zaino con peso pari a "peso"

            if peso < p[i]:
                M[i][peso] = M[i-1][peso]                               # se l'elemento è troppo pesante non possiamo metterlo
            else:
                if M[i-1][peso] > (M[i-1][peso - p[i]] + v[i]):         # entra, ma se non conviene metterlo non lo mettiamo
                    M[i][peso] = M[i-1][peso]
                else:                                                   # entra e conviene metterlo
                    M[i][peso] = M[i - 1][peso - p[i]] + v[i]
                    C[i][peso] = True

    M_temp = []
    C_temp = []
    for i in range(n_items-1,0,-1):
        M_temp.append(M[i])
        C_temp.append(C[i])
    return M_temp, C_temp

def getItems(p, C):
    n_items = len(p)
    k = 0
    b = len(C[0]) - 1
    item = []
    while k < (n_items - 1) and b > 0: # 0 -> 8
        if C[k][b] == True:
            item.append(n_items - k)
            b -= p[n_items - k - 1]
        k += 1

    return item

def printMatriceK01(M):
    for i in range(len(M)):
        print("[", end="")
        for j in range(len(M[i])):
            if j == len(M[i]) - 1:
                print("{:3} ".format(M[i][j]), end="")
            else:
                print("{:3} {}".format(M[i][j], ","), end="")
        print("]\n")
    print()

def printKnapsakResult(tup):
    M = tup[0]
    C = tup[1]
    printMatriceK01(M)
    printMatriceK01(C)

    items = getItems(p, C)

    print("Optimum: ", M[0][-1])
    for item in items:
        print("{:7} {:7} {:7}".format("item " + str(item), "Cost " + str(v[item - 1]), "Volume " + str(p[item - 1])))





"""*******************************************************Main*******************************************************"""

p = [3, 5, 7, 4, 3, 9, 2, 11, 5]
v = [2, 3, 3, 4, 4, 5, 7, 8, 8]

printKnapsakResult(Knapsak_0_1(p, v, 15))