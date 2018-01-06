from Progetto_4.TdP_collections.graphs.graph import Graph
from Progetto_4.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue


class MyGraph(Graph):
    def min_vertex_cover(self):
        """
        calcola un vertex cover di dimensione minima
        :return: solution_list lista dei vertici del vertex cover
        """
        current_status = {}
        vertex_list = [None] * self.vertex_count()
        solution = {}
        pq = HeapPriorityQueue()

        for v in self.vertices():  # O(n*log(n))
            solution[v] = 1
            pq.add(-self.degree(v), v)  # O(log(n))

        for edge in self.edges():  # O(m)
            current_status[edge] = 2

        for i in range(len(pq)):  # O(n*log(n))
            k, v = pq.remove_min()
            vertex_list[i] = (v, 0)

        self._backtrack_min_vertex_cover(vertex_list, current_status, solution, 0)

        solution_list = []

        for v in solution:
            if solution[v]:
                solution_list.append(v)

        return solution_list

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

    def _could_be_a_sol(self, current_status, vertex):  # dato lo stato corrente, e dato che non prendo quel vertice
        new_status = current_status.copy()

        for edge in self.incident_edges(vertex):
            new_status[edge] -= 1
            if not new_status[edge]:
                return False

        if self.is_directed():
            for edge in self.incident_edges(vertex, False):
                new_status[edge] -= 1
                if not new_status[edge]:
                    return False

        return new_status
