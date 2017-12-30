from Esercizi.TdP_collections.graphs.graph import Graph
import cProfile
import random

class MyGraph(Graph):

    def greedy_vertex_cover1(self):
        vetex_degree = {}
        vetex_cover = []

        for vertex in self.vertices():
            vetex_degree[vertex] = self.degree(vertex)

        max_degree = 1

        while max_degree:
            max_degree = 0
            current_vertex = None

            for v in vetex_degree:
                if vetex_degree[v] > max_degree:
                    max_degree = vetex_degree[v]
                    current_vertex = v

            if current_vertex is None:
                return vetex_cover
            else:
                vetex_cover.append(current_vertex)

            for edge in self.incident_edges(current_vertex):
                v = edge.opposite(current_vertex)
                if vetex_degree.__contains__(v):
                    deg = vetex_degree[v]
                    deg -= 1
                    if deg > 0:
                        vetex_degree[v] = deg
                    else:
                        del vetex_degree[v]

            if vetex_degree.__contains__(current_vertex):
                del vetex_degree[current_vertex]

        return vetex_cover


    ''''Aggiorna la mappa vertex_degree se è la prima volta che si incontra il vertice u - O(1)'''
    def update_degree(self, u, vertex_degree):
        if not vertex_degree.__contains__(u):
            vertex_degree[u] = self.degree(u)

    '''Cerca il vertice che ha il grado più alto tra i vertici adiacenti a u, tenendo conto degli archi già coperti - O(deg(u))'''
    def find_max(self, u, vertex_degree):
        max_degree = vertex_degree[u]
        max_vertex = u
        for edge in self.incident_edges(u):
            v = edge.opposite(u)
            self.update_degree(v, vertex_degree)
            if vertex_degree[v] > max_degree:
                max_degree = vertex_degree[v]
                max_vertex = v
        return (max_vertex, max_degree)

    '''Restituisce la lista dei vertici che risolve il problema di vertex cover con metodologia gready. - O(m)?'''
    def greedy_vertex_cover2(self):
        vertex_degree = {}
        vertex_cover = []
        stack = []
        discovered = {}
        for e in self.edges():  # O(m)
            discovered[e] = False
        for vertex in self.vertices():  # O(1)
            current_vertex = vertex
            self.update_degree(current_vertex, vertex_degree)
            stack.append(current_vertex)
            break
        while (True):  # O(m) ?
            max_vertex, max_degree = self.find_max(current_vertex, vertex_degree)  # O(deg(current_vertex))
            if max_degree == 0:
                if len(stack) == 0:
                    return vertex_cover
                else:
                    current_vertex = stack.pop()
                    continue
            if current_vertex == max_vertex:
                vertex_cover.append(current_vertex)
                for edge in self.incident_edges(current_vertex):  # O(deg(current_vertex))
                    if not discovered[edge]:
                        discovered[edge] = True
                        u = edge.opposite(current_vertex)
                        vertex_degree[u] -= 1
                        vertex_degree[current_vertex] -= 1
            else:
                current_vertex = max_vertex
                stack.append(current_vertex)

    def greedy_vertex_cover3(self):

        # dict di edges in cui ad ogni edge è associato un valore che segna la sua validità(1) o invalidità(0)
        edges = {}
        for edge in self.edges():
            edges[edge] = 1

        soluzione = []

        for edge in edges:

            # l'edge è già stato preso
            if edges[edge] == 0:
                continue

            origin, destination = edge.endpoints()

            # calcolo il grado restante del primo vertice
            degree_origin = 0
            for elem in self.incident_edges(origin):
                if edges[elem] == 1:
                    degree_origin += 1

            # calcolo il grado restante del secondo vertice
            degree_destination = 0
            for elem in self.incident_edges(destination):
                if edges[elem] == 1:
                    degree_destination += 1

            if degree_origin > degree_destination:
                soluzione.append(origin)  # aggiungo il vertice alla soluzione

                # invalido tutti i suoi edge
                for elem in self.incident_edges(origin):
                    edges[elem] = 0

            else:
                soluzione.append(destination)  # aggiungo il vertice alla soluzione

                # invalido tutti i suoi edge
                for elem in self.incident_edges(destination):
                    edges[elem] = 0

        return soluzione


def generateGraph(n,m):
    G = MyGraph()
    l = []
    for i in range(n):
        l.append(G.insert_vertex(i))
    for j in range(m):
        n1 = 0
        n2 = 0
        cond = True
        while n1 == n2 or cond:
            n1 = random.randrange(1,n)
            n2 = random.randrange(1,n)
            try:
                G.insert_edge(l[n1],l[n2])
                cond = False
            except:
                cond = True
    return G

G2 = MyGraph()

a = G2.insert_vertex("a")
b = G2.insert_vertex("b")
c = G2.insert_vertex("c")
d = G2.insert_vertex("d")
e = G2.insert_vertex("e")
f = G2.insert_vertex("f")
g = G2.insert_vertex("g")
h = G2.insert_vertex("h")
i = G2.insert_vertex("i")
G2.insert_edge(a, b)
G2.insert_edge(b, c)
G2.insert_edge(a, c)
G2.insert_edge(c, d)
G2.insert_edge(d, e)
G2.insert_edge(e, f)
G2.insert_edge(f, g)
G2.insert_edge(g, d)
G2.insert_edge(c, h)
G2.insert_edge(b, h)
G2.insert_edge(h, i)

G3 = MyGraph()

a = G3.insert_vertex("a")
b = G3.insert_vertex("b")
c = G3.insert_vertex("c")
d = G3.insert_vertex("d")
e = G3.insert_vertex("e")
f = G3.insert_vertex("f")
g = G3.insert_vertex("g")
h = G3.insert_vertex("h")
i = G3.insert_vertex("i")
l = G3.insert_vertex("l")
m = G3.insert_vertex("m")
n = G3.insert_vertex("n")
o = G3.insert_vertex("o")
p = G3.insert_vertex("p")
q = G3.insert_vertex("q")
r = G3.insert_vertex("r")
s = G3.insert_vertex("s")

G3.insert_edge(a, b)
G3.insert_edge(c, a)
G3.insert_edge(d, b)
G3.insert_edge(f, b)
G3.insert_edge(f, g)
G3.insert_edge(c, e)
G3.insert_edge(h, g)
G3.insert_edge(h, l)
G3.insert_edge(i, h)
G3.insert_edge(i, m)
G3.insert_edge(n, m)
G3.insert_edge(n, o)
G3.insert_edge(o, p)
G3.insert_edge(r, q)
G3.insert_edge(s, q)
G3.insert_edge(q, p)
G3.insert_edge(r, i)

G = generateGraph(10000,10000000)

cProfile.run("G.greedy_vertex_cover1()")
cProfile.run("G.greedy_vertex_cover2()")
cProfile.run("G.greedy_vertex_cover3()")

vertex_cover = G.greedy_vertex_cover1()
print(len(vertex_cover))
print("***************1****************")

vertex_cover = G.greedy_vertex_cover2()
print(len(vertex_cover))
print("***************2****************")

vertex_cover = G.greedy_vertex_cover3()
print(len(vertex_cover))
print("***************3****************")