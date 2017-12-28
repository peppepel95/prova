from Esercizi.TdP_collections.graphs.graph import Graph
from Esercizi.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree

class Node:
    def __init__(self):
        self._left = None
        self._right = None
        self._parent = None

def MakeTreeDict(discovered,nodeList,treeDict):
    for i in range(1, len(nodeList) + 1):
        v = nodeList[-i]
        e = discovered[v]
        if e is not None:
            u = e.opposite(v)
            if treeDict[u]._left is None:
                treeDict[u]._left = v
            else:
                treeDict[u]._right = v
            treeDict[v]._parent = u

def DFS(g, u, discovered):
  for e in g.incident_edges(u):    # for every outgoing edge from u
    v = e.opposite(u)
    if v not in discovered:        # v is an unvisited vertex
      discovered[v] = e            # e is the tree edge that discovered v
      DFS(g, v, discovered)        # recursively explore from v

def construct_path(u, v, discovered):
  path = []                        # empty path by default
  if v in discovered:
    # we build list from v to u and then reverse it at the end
    path.append(v)
    walk = v
    while walk is not u:
      e = discovered[walk]         # find edge leading to walk
      parent = e.opposite(walk)
      path.append(parent)
      walk = parent
    path.reverse()                 # reorient path from u to v
  return path

def DFS_complete(g):
  forest = {}
  for u in g.vertices():
    if u not in forest:
      forest[u] = None             # u will be the root of a tree
      DFS(g, u, forest)
  return forest

G = Graph()
a = G.insert_vertex("a")
b = G.insert_vertex("b")
c = G.insert_vertex("c")
d = G.insert_vertex("d")
e = G.insert_vertex("e")
f = G.insert_vertex("f")
g = G.insert_vertex("g")
G.insert_edge(a,b)
G.insert_edge(a,c)
G.insert_edge(b,c)
G.insert_edge(c,d)
G.insert_edge(d,e)
G.insert_edge(e,f)
G.insert_edge(c,f)
G.insert_edge(c,g)

discovered = {}
discovered[a] = None
lista = []
DFS(G,a,discovered)

tree = {}
for node in discovered:
    lista.append(node)
    tree[node] = Node()

MakeTreeDict(discovered,lista,tree)

for el in tree:
    tree[el] = (tree[el], False)

for i in range(1,len(lista)+1):
    v = lista[-i]
    node, bridge_old = tree[v]
    bridge = True

    if (node._left is not None and tree[node._left][1]):
        print("edge: (", v.element(), ",", node._left.element(), ") è un bridge")
    if (node._right is not None and tree[node._right][1]):
        print("edge: (", v.element(), ",", node._right.element(), ") è un bridge")
    if (node._left is not None and not tree[node._left][1]) or (node._right is not None and not tree[node._right][1]):
        bridge = False
    else:
        if node._left is not None:
            ed1 = discovered[node._left]
        else:
            ed1 = None
        if node._right is not None:
            ed2 = discovered[node._right]
        else:
            ed2 = None
        ed3 = discovered[v]

        for e in G.incident_edges(v):
            if e is not ed1 and e is not ed2 and e is not ed3:
                bridge = False

    tree[v] = (node,bridge)
