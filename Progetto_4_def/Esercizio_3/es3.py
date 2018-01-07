from Esercizi.TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Progetto_4.Utilities import read_graph_from_file
import random


def emergency_call(g, pos, src, k):
    d = {}                                              # d[v] is upper bound from s to v
    cloud = {}                                          # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()                   # vertex v will have key d[v]
    pqlocator = {}                                      # map from vertex to its pq locator
    volanti = {}                                        # dict ricavato da pos, (key:incrocio, value:lista di volanti)
    solution = []                                       # lista delle k volanti da allertare

    for volante in pos:
        incrocio = pos[volante]
        if volanti.__contains__(incrocio):
            volanti[incrocio].append(volante)
        else:
            volanti[incrocio] = [volante]

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')                         # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)                  # save locator for future updates

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key                                  # its correct d[u] value
        del pqlocator[u]                                # u is no longer in pq
        if volanti.__contains__(u):                     # se c'è una volante nell'incrocio
            for volante in volanti[u]:
                if k == 0:
                    return solution
                solution.append(volante)
                k -= 1
        for e in g.incident_edges(u):                   # outgoing edges (u,v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:                   # better path to v?
                    d[v] = d[u] + wgt                   # update the distance
                    pq.update(pqlocator[v], d[v], v)    # update the pq entry

    raise ValueError("non ci sono abbastanza volanti!")


"""*******************************************MAIN*******************************************"""


i = 1
start = None
G = read_graph_from_file("../Test_files/city_map.txt")

for j in range(0,3000):
    i = 1
    start = None
    pos = {}
    for v in G.vertices():
        r = random.randrange(0,2)
        if r:
            pos[i] = v
            i += 1
        r1 = random.randrange(1, 100)
        if r1 > 50 and start is None:
            start = v

    k = int(len(pos)/2)
    print(emergency_call(G, pos, start, k))
