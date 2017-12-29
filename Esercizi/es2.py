from Esercizi.TdP_collections.graphs.graph import Graph
from Esercizi.TdP_collections.graphs.dfs import DFS_complete
from Esercizi.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree

class Node:
    def __init__(self):
        self._left = None
        self._right = None
        self._parent = None

def MakeTreeDict(discovered, nodeList, treeDict):
    """
    usata nella binaryTreeFromDfs restituisce l'albero della dfs come dict
    :param discovered: (key:vertex, value:edge)
    :param nodeList: lista dei vertici ordinata
    :return treeDict: albero restituito come dict

    """
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
    """
    usata nella binaryTreeFromDfs prende l'albero come dict e lo trasforma in un LinkedBinaryTree
    :param p: current_position
    :param tree: tree as dict
    :return bt: LinkedBinaryTree
    """
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
    """
    chiama una DFS_Complete sul grafo G -> restituisce l'albero della dfs come LinkedBinaryTree e i vertici in discovered (key:vertex, value:edge)
    :param G: graph
    :return: bt LinkedBinaryTree, discovered dict
    """
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

    return bt, discovered

def findBridges(G):
    """
    ricerca gli archi bridge partendo dai risultati della binaryTreeFromDfs
    :param G: graph
    :return: bridgeEdges list
    """
    bt, discovered = binaryTreeFromDfs(G)

    i = 1
    nd = 1
    reached = []
    ed1 = None
    ed2 = None

    for p in bt.postorder():
        if bt.left(p) is not None:
            nd += discovered[bt.left(p).element()][2]
        if bt.right(p) is not None:
            nd += discovered[bt.right(p).element()][2]

        discovered[p.element()] = (discovered[p.element()], i, nd, 0, 0)
                                                                            #reset
        i += 1
        nd = 1

    for p in bt.postorder():
        if bt.left(p) is not None:
            reached.append(discovered[bt.left(p).element()][3])
            reached.append(discovered[bt.left(p).element()][4])
            ed1 = discovered[bt.left(p).element()][0]
        if bt.right(p) is not None:
            reached.append(discovered[bt.right(p).element()][3])
            reached.append(discovered[bt.right(p).element()][4])
            ed2 = discovered[bt.right(p).element()][0]

        ed3 = discovered[p.element()][0]

        for e in G.incident_edges(p.element()):
            if e is not ed1 and e is not ed2 and e is not ed3:              # back edge
                v = e.opposite(p.element())
                reached.append(discovered[v][1])

        old = discovered[p.element()]
        reached.append(old[1])
        low = min(reached)
        high = max(reached)
        discovered[p.element()] = (old[0], old[1], old[2], low, high)
        print(p.element(), discovered[p.element()])
                                                                            #reset
        reached.clear()
        ed1 = None
        ed2 = None

    bridgeEdges = []
    for vertex in discovered:
        edge, number, nd, low, high = discovered[vertex]
        if edge is not None and high <= number and nd > (number - low):     #bridge condition
            bridgeEdges.append(edge)

    return bridgeEdges








def findBridgeOLD(tree,NodeList,discovered):
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


bridgeEdges = findBridges(G)

for edge in bridgeEdges:
    print(edge)