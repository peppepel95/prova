from Esercizi.TdP_collections.graphs.graph import Graph

def BellmanFord (G, s):
    d = {} #distance
    p = {} #predecessor

    # Passo 1: Inizializza
    for v in G.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')
        p[v] = None

    n = len(G)

    # Passo 2: Processa gli archi ripetutamente
    for i in range(1,n):
        for uv in G.edges():
            u, v = uv.endpoints()
            r = d[u] + uv.element()
            if r < d[v]:
                d[v] = r
                p[v] = u

    # Passo 3: controlla la presenza di cicli negativi
    for uv in G.edges():
        u, v = uv.endpoints()
        if d[v] > d[u] + uv.element():
            raise TypeError ("Il grafo contiene un ciclo di peso negativo")

    return d, p

def printShortestPath (d, p, i, j):

    stack = []
    curr_vertex = j

    while curr_vertex is not i:
        stack.append(str(curr_vertex.element()))
        prev_vertex = p[curr_vertex]
        stack.append(str(d[curr_vertex] - d[prev_vertex]))
        curr_vertex = prev_vertex
    stack.append(curr_vertex)

    for stringa in stack:
        print(stringa, end=" ")

