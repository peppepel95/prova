from TdP_collections.graphs.graph import Graph

class MyGraph(Graph):

    def greedy_vertex_cover(self):

        #dict di edges in cui ad ogni edge è associato un valore che segna la sua validità(1) o invalidità(0)
        edges = {}
        for edge in self.edges():
            edges[edge] = 1

        soluzione = []

        for edge in edges:

            #l'edge è già stato preso
            if edges[edge] == 0:
                continue

            origin, destination = edge.endpoints()

            #calcolo il grado restante del primo vertice
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
                soluzione.append(origin) #aggiungo il vertice alla soluzione

                #invalido tutti i suoi edge
                for elem in self.incident_edges(origin):
                    edges[elem] = 0

            else:
                soluzione.append(destination) #aggiungo il vertice alla soluzione

                # invalido tutti i suoi edge
                for elem in self.incident_edges(destination):
                    edges[elem] = 0

        return soluzione



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
G3.insert_edge(i, c)
G3.insert_edge(i, h)
G3.insert_edge(i, m)
G3.insert_edge(n, m)
G3.insert_edge(n, o)
G3.insert_edge(o, p)
G3.insert_edge(r, q)
G3.insert_edge(s, q)
G3.insert_edge(q, p)
G3.insert_edge(r, i)


vertex_cover = G3.greedy_vertex_cover()

for vertex in vertex_cover:
    print(vertex, end=" ")
