from Esercizi.TdP_collections.graphs.graph import Graph

class MyGraph(Graph):

    def greedy_vertex_cover(self):
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
                        vetex_degree[v] = 0
                vetex_degree[current_vertex] = 0

        return vetex_cover



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

vertex_cover = G2.greedy_vertex_cover()

for vertex in vertex_cover:
    print(vertex)

