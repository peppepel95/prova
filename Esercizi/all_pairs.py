from Esercizi.TdP_collections.graphs.graph import Graph
from copy import deepcopy


def floyd_warshall(g):
    n = g.vertex_count()
    d = {}
    p = {}

    for u in g.vertices():
        d[u] = {}
        p[u] = {}
        for v in g.vertices():
            if u == v:
                d[u][v] = 0
                p[u][v] = float('inf')
            else:
                edge = g.get_edge(u, v)
                if edge is None:
                    d[u][v] = float('inf')
                    p[u][v] = float('inf')
                else:
                    d[u][v] = int(edge.element())
                    p[u][v] = u

    for k in g.vertices():
        for i in g.vertices():
            for j in g.vertices():
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]

    return d, p

G = Graph()
a = G.insert_vertex("a")
b = G.insert_vertex("b")
c = G.insert_vertex("c")
d = G.insert_vertex("d")
e = G.insert_vertex("e")
f = G.insert_vertex("f")
g = G.insert_vertex("g")
h = G.insert_vertex("h")
i = G.insert_vertex("i")
G.insert_edge(a, b, 21)
G.insert_edge(b, c, 57)
G.insert_edge(a, c, 17)
G.insert_edge(c, d, 81)
G.insert_edge(d, e, 8)
G.insert_edge(e, f, 7)
G.insert_edge(f, g, 55)
G.insert_edge(g, d, 12)
G.insert_edge(c, h, 42)
G.insert_edge(b, h, 99)
G.insert_edge(h, i, 120)

d, p = floyd_warshall(G)
