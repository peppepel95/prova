from Progetto_4.TdP_collections.graphs.graph import Graph
from Progetto_4.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue


class MyGraph(Graph):
    def _DFS(self, u, discovered, value):

        for e in self.incident_edges(u):
            v = e.opposite(u)
            if discovered[v][0] == 0:
                discovered[v][0] = value
                self._DFS(v, discovered, value)
        if self.degree(u) == 0:
            discovered[u][0] = value

    def _sconnect_graph(self):

        grafi = []
        disc_vert = {}
        index = 1

        for vertex in self.vertices():
            disc_vert[vertex] = [0, None]

        for vertex in disc_vert:
            if disc_vert[vertex][0] == 0:  # se è 0 non è stato visitato
                self._DFS(vertex, disc_vert, index)
                index += 1

        if index == 2:  # un unico grafo
            return [self, ]

        for i in range(index - 1):
            grafi.append(MyGraph(directed=self.is_directed()))

            for edge in self.edges():
                v1, v2 = edge.endpoints()
                if (disc_vert[v1][0] == i + 1) and (disc_vert[v2][0] == i + 1):
                    if disc_vert[v1][1] is None:
                        ver1 = grafi[i].insert_vertex(v1.element())
                        disc_vert[v1][1] = ver1
                    else:
                        ver1 = disc_vert[v1][1]
                    if disc_vert[v2][1] is None:
                        ver2 = grafi[i].insert_vertex(v2.element())
                        disc_vert[v2][1] = ver2
                    else:
                        ver2 = disc_vert[v2][1]
                    grafi[i].insert_edge(ver1, ver2)
        return grafi

    def min_vertex_cover(self):  # for disconnected graph
        grafi = self._sconnect_graph()
        sol = []

        for grafo in grafi:
            sol += grafo._min_vertex_cover()
        return sol

    def _min_vertex_cover(self):  # for connected graph
        """
        calcola un vertex cover di dimensione minima
        :return: solution_list lista dei vertici del vertex cover
        """
        current_status = {}
        vertex_list = [None] * self.vertex_count()
        solution = []
        pq = HeapPriorityQueue()
        current_solution = []
        sol = []
        for v in self.vertices():  # O(n*log(n))
            solution.append(v)
            pq.add(-self.degree(v), v)  # O(log(n))

        for edge in self.edges():  # O(m)
            current_status[edge] = 2

        for i in range(len(pq)):  # O(n*log(n))
            k, v = pq.remove_min()
            vertex_list[i] = v

        sol.append(solution)
        self._backtrack_min_vertex_cover(vertex_list, current_status, sol, current_solution, 0)

        return sol[0]

    def _backtrack_min_vertex_cover(self, vertex_list, current_status, s, current_solution, k):
        if k == len(vertex_list):

            sum = len(current_solution)

            current_sum = len(s[0])

            if sum < current_sum:
                s[0] = current_solution
        else:
            new_status = self._could_be_a_sol(current_status, vertex_list[k])
            if new_status:
                self._backtrack_min_vertex_cover(vertex_list, new_status, s, current_solution, k + 1)

            if len(current_solution) + 1 < len(s[0]):
                next2 = current_solution.copy()
                next2.append(vertex_list[k])

                self._backtrack_min_vertex_cover(vertex_list, current_status, s, next2, k + 1)

    def _is_a_solution(self, vertex_list):
        status = {}
        for edge in self.edges():
            status[edge] = 0

        for v in vertex_list:
            for edge in self.incident_edges(v):
                status[edge] += 1
            if self.is_directed():
                for edge in self.incident_edges(v, False):  # nel caso di grafo diretto
                    status[edge] += 1

        for edge in status:
            if not status[edge]:
                return False

        return True

    def _could_be_a_sol(self, current_status, vertex):  # dato lo stato corrente, e dato che non prendo quel vertice
        new_status = current_status.copy()

        for edge in self.incident_edges(vertex):
            new_status[edge] -= 1
            if not new_status[edge]:
                return False

        if self.is_directed():
            for edge in self.incident_edges(vertex, False):  # nel caso di grafo diretto
                new_status[edge] -= 1
                if not new_status[edge]:
                    return False

        return new_status

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
                        del vetex_degree[v]

            if vetex_degree.__contains__(current_vertex):
                del vetex_degree[current_vertex]

        return vetex_cover
