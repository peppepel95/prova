from Esercizi.TdP_collections.graphs.graph import Graph
from Esercizi.TdP_collections.graphs.dfs import DFS_complete
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

def binTree(p, tree, bt):
    if p is not None:
        vertex = p.element()
        node = tree[vertex]
        if node._left is not None:
            pos = bt._add_left(p,node._left)
            binTree(pos,tree,bt)
        if node._right is not None:
            pos = bt._add_right(p,node._right)
            binTree(pos, tree, bt)

def binaryTreeFromDfs(G):
    discovered = DFS_complete(G)
    NodeList = []
    tree = {}
    count = 0

    for node in discovered:
        if node is None:
            count += 1
        NodeList.append(node)
        tree[node] = Node()

    if count > 1:
        raise TypeError("Grafo G non connesso")

    MakeTreeDict(discovered,NodeList,tree)
    bt = LinkedBinaryTree()
    p = bt._add_root(NodeList[0])
    binTree(p,tree,bt)

    return bt



def findBridge(tree,NodeList,discovered):
    for el in tree:
        tree[el] = (tree[el], False)

    for i in range(1,len(NodeList)+1):
        v = NodeList[-i]
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





"""*******************************************MAIN*******************************************"""


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


binaryTreeFromDfs(G)