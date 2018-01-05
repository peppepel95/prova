from Progetto_4.TdP_collections.graphs.graph import Graph


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
    def update_degree (self, u, vertex_degree):
        if not vertex_degree.__contains__(u):
            vertex_degree[u] = self.degree(u)

    '''Cerca il vertice che ha il grado più alto tra i vertici adiacenti a u, tenendo conto degli archi già coperti - O(deg(u))'''
    def find_max(self,u,vertex_degree):
        max_degree = vertex_degree[u]
        max_vertex = u
        for edge in self.incident_edges(u):
            v = edge.opposite(u)
            self.update_degree(v, vertex_degree)
            if vertex_degree[v] > max_degree:
                max_degree = vertex_degree[v]
                max_vertex = v
        return (max_vertex,max_degree)

    '''Restituisce la lista dei vertici che risolve il problema di vertex cover con metodologia gready. - O(m)?'''
    def greedy_vertex_cover2(self):
        vertex_degree = {}
        vertex_cover = []
        stack = []
        discovered = {}
        for e in self.edges(): #O(m)
            discovered[e] = False
        for vertex in self.vertices():#O(1)
            current_vertex = vertex
            self.update_degree(current_vertex,vertex_degree)
            stack.append(current_vertex)
            break
        while(True): #O(m) ?
            max_vertex, max_degree = self.find_max(current_vertex,vertex_degree) #O(deg(current_vertex))
            if max_degree == 0:
                if len(stack) == 0:
                    if len(vertex_degree) == self.vertex_count():
                        return vertex_cover
                    else:
                        for vertex in self.vertices():
                            if vertex not in vertex_degree.keys():
                                current_vertex = vertex
                                self.update_degree(current_vertex,vertex_degree)
                                stack.append(current_vertex)
                                break
                        continue
                else:
                    current_vertex = stack.pop()
                    continue
            if current_vertex == max_vertex:
                vertex_cover.append(current_vertex)
                for edge in self.incident_edges(current_vertex): #O(deg(current_vertex))
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


"""
G = generateGraph(50,100)

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
"""