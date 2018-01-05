from TdP_collections.graphs.graph import Graph
import cProfile
from .Utilities import generateGraph, knownGraphs

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


G = generateGraph(30, 80)

vertex_cover = None

cProfile.run("vertex_cover = G.min_vertex_cover()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)