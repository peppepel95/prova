from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue

def newDFS(g, u, discovered, value):

    for e in g.incident_edges(u):
        v = e.opposite(u)
        if discovered[v] == 0:
            discovered[v] = value
            newDFS(g, v, discovered, value)


class MyGraph(Graph):

    def sconnectGraph(self):

        grafi = []
        disc_vert = {}
        index = 1

        for vertex in self.vertices():
            disc_vert[vertex] = 0

        for vertex in disc_vert:
            if disc_vert[vertex] == 0: # se è 0 non è stato visitato
                newDFS(self, vertex, disc_vert, index)
                index += 1

        for i in range(index):
            grafi.append(MyGraph(directed=self.is_directed()))
            for vertex in disc_vert:
                if disc_vert[vertex] == i+1:
                    grafi[i].insert_vertex(vertex.element())
            for edge in self.edges():
                v1, v2 = edge.endpoints()
                v1 = grafi[i].vertices()[v1]
                v2 = grafi[i].vertices()[v2]
                if (disc_vert[v1] == i + 1) and (disc_vert[v2] == i + 1):
                    grafi[i].insert_edge(v1, v2)
        return grafi

    def mvc(self):
        grafi = self.sconnectGraph()
        sol = {}
        for grafo in grafi:
            sol.update(grafo.min_vertex_cover())
        return sol

    def min_vertex_cover(self):
        current_status = {}
        vertex_list = [None]*self.vertex_count()
        solution = {}
        pq = HeapPriorityQueue()

        for v in self.vertices():
            solution[v] = 1

            pq.add(-self.degree(v), v)

            for edge in self.incident_edges(v):
                if edge in current_status:
                    current_status[edge] += 1
                else:
                    current_status[edge] = 1

        for i in range(len(pq)):
            k, v = pq.remove_min()
            vertex_list[i] = (v, 0)

        self._backtrack_min_vertex_cover(vertex_list,current_status,solution,0)
        return solution


    def _backtrack_min_vertex_cover(self, vertex_list, current_status, s, k):
        if k == len(s):
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

