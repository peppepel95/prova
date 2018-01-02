from Esercizi.TdP_collections.graphs.graph import Graph

class MyGraph(Graph):

    def min_vertex_cover(self):
        current_status = {}
        vertex_list = [None]*self.vertex_count()
        solution = {}
        i = 0

        for v in self.vertices():
            solution[v] = 1

            vertex_list[i] = (v, 0)
            i += 1

            for edge in self.incident_edges(v):
                if edge in current_status:
                    current_status[edge] += 1
                else:
                    current_status[edge] = 1

        self._backtrack_min_vertex_cover(vertex_list,current_status,solution,0)
        return solution


    def _backtrack_min_vertex_cover(self, vertex_list, current_status, s, k):
        if k == len(s):
            if self._is_a_solution(vertex_list):

                sum = 0
                for v, val in vertex_list:
                    sum += val

                current_sum = 0
                for v in s:
                    current_sum += s[v]

                if sum < current_sum:
                    for v, val in vertex_list:
                        s[v] = val
        else:
            new_status = self._could_be_a_sol(current_status, vertex_list[k][0])
            if new_status:
                next1 = vertex_list.copy()
                next1[k] = (next1[k][0], 0)
                self._backtrack_min_vertex_cover(next1, new_status, s, k + 1)

            next2 = vertex_list.copy()
            next2[k] = (next2[k][0], 1)
            self._backtrack_min_vertex_cover(next2, current_status, s, k + 1)

    def _is_a_solution(self, vertex_list):
        status = {}
        for edge in self.edges():
            status[edge] = 0

        for v, val in vertex_list:
            if val:
                for edge in self.incident_edges(v):
                    status[edge] += 1

        for edge in status:
            if not status[edge]:
                return False

        return True

    def _could_be_a_sol(self, current_status, vertex): # dato lo stato corrente, e dato che non prendo quel vertice
        new_status = current_status.copy()

        for edge in self.incident_edges(vertex):
            new_status[edge] -= 1
            if not new_status[edge]:
                return False

        return new_status

















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

G5 = MyGraph()

a = G5.insert_vertex("a")
b = G5.insert_vertex("b")
c = G5.insert_vertex("c")
d = G5.insert_vertex("d")
e = G5.insert_vertex("e")
f = G5.insert_vertex("f")
g = G5.insert_vertex("g")
h = G5.insert_vertex("h")
i = G5.insert_vertex("i")
l = G5.insert_vertex("l")
m = G5.insert_vertex("m")
n = G5.insert_vertex("n")

G5.insert_edge(a, b)
G5.insert_edge(b, c)
G5.insert_edge(d, b)
G5.insert_edge(d, c)
G5.insert_edge(a, m)
G5.insert_edge(a, l)
G5.insert_edge(c, e)
G5.insert_edge(d, f)
G5.insert_edge(i, e)
G5.insert_edge(l, i)
G5.insert_edge(n, i)
G5.insert_edge(m, n)
G5.insert_edge(m, l)
G5.insert_edge(n, h)
G5.insert_edge(h, f)
G5.insert_edge(h, g)
G5.insert_edge(g, f)
G5.insert_edge(e, g)


vertex_cover = G5.min_vertex_cover()

for v in vertex_cover:
    if vertex_cover[v]:
        print(v)