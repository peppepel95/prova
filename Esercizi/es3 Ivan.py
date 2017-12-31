from Esercizi.TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from Esercizi.TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from Esercizi.TdP_collections.graphs.graph import Graph

def emergency_call(g, pos, src, k):
  d = {}                                        # d[v] is upper bound from s to v
  cloud = {}                                    # map reachable v to its d[v] value
  pq = AdaptableHeapPriorityQueue()             # vertex v will have key d[v]
  pqlocator = {}                                # map from vertex to its pq locator
  volanti = {}
  solution = []

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
      d[v] = float('inf')                       # syntax for positive infinity
    pqlocator[v] = pq.add(d[v], v)              # save locator for future updates

  while not pq.is_empty():
    key, u = pq.remove_min()
    cloud[u] = key                              # its correct d[u] value
    del pqlocator[u]                            # u is no longer in pq
    if volanti.__contains__(u):          # se c'è una volante nell'incrocio
        for volante in volanti[u]:
            if k == 0:
                return solution
            solution.append(volante)
            k -= 1
    for e in g.incident_edges(u):               # outgoing edges (u,v)
      v = e.opposite(u)
      if v not in cloud:
        # perform relaxation step on edge (u,v)
        wgt = e.element()
        if d[u] + wgt < d[v]:                   # better path to v?
          d[v] = d[u] + wgt                     # update the distance
          pq.update(pqlocator[v], d[v], v)      # update the pq entry    

  raise ValueError("non ci sono abbastanza volanti!")  

G = Graph()
pos = {}

a = G.insert_vertex("a")
b = G.insert_vertex("b")
c = G.insert_vertex("c")
d = G.insert_vertex("d")
e = G.insert_vertex("e")
f = G.insert_vertex("f")
g = G.insert_vertex("g")
G.insert_edge(a,b,300)
G.insert_edge(a,c,1290)
G.insert_edge(b,c,800)
G.insert_edge(c,d,70)
G.insert_edge(d,e,140)
G.insert_edge(e,f,900)
G.insert_edge(c,f,500)
G.insert_edge(c,g,250)

pos[1] = a
pos[2] = f
pos[3] = g


print(emergency_call(G, pos, c, 2))