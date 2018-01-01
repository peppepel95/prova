from Esercizi.TdP_collections.graphs.graph import Graph
from Esercizi.TdP_collections.graphs.dfs import DFS_complete
from Esercizi.TdP_collections.tree.linked_binary_tree import LinkedBinaryTree


class Node:
    def __init__(self):
        self._left = None
        self._right = None
        self._parent = None


def make_tree_dict(discovered, node_list, tree_dict):
    """
    Usata nella binaryTreeFromDfs restituisce l'albero della dfs come dict [O(n)]
    :param discovered: (key:vertex, value:edge)
    :param node_list: lista dei vertici ordinata
    :param tree_dict: albero restituito come dict

    """
    for i in range(1, len(node_list) + 1):  # O(n)
        v = node_list[-i]
        e = discovered[v]
        if e is not None:
            u = e.opposite(v)
            if tree_dict[u]._left is None:
                tree_dict[u]._left = v
            else:
                tree_dict[u]._right = v
            tree_dict[v]._parent = u


def from_tree_dict_to_bin_tree(p, tree, bt):
    """
    Usata nella binaryTreeFromDfs prende l'albero come dict e lo trasforma in un LinkedBinaryTree [O(n)]
    :param p: current_position
    :param tree: tree as dict
    :param bt: LinkedBinaryTree
    """
    if p is not None:
        vertex = p.element()
        node = tree[vertex]
        if node._left is not None:
            pos = bt._add_left(p,node._left)
            from_tree_dict_to_bin_tree(pos,tree,bt)
        if node._right is not None:
            pos = bt._add_right(p,node._right)
            from_tree_dict_to_bin_tree(pos, tree, bt)


def binary_tree_from_dfs(G):
    """
    Chiama una DFS_Complete sul grafo G
    restituisce l'albero della dfs come LinkedBinaryTree e i vertici in discovered (key:vertex, value:edge) [O(n+m)]
    :param G: graph
    :return: bt LinkedBinaryTree, discovered dict
    """
    discovered = DFS_complete(G)  # O(n+m)
    node_list = []
    tree = {}
    count = 0

    for node in discovered:  # O(n)
        if node is None:
            count += 1
        node_list.append(node)
        tree[node] = Node()

    if count > 1:
        raise TypeError("Grafo G non connesso")

    make_tree_dict(discovered, node_list, tree)  # O(n)
    bt = LinkedBinaryTree()
    p = bt._add_root(node_list[0])
    from_tree_dict_to_bin_tree(p, tree, bt)  # O(n)

    return bt, discovered


def bridge(G):
    """
    Ricerca gli archi bridge partendo dai risultati della binaryTreeFromDfs [O(n+m)]
    :param G: graph
    :return: bridgeEdges list or None
    """
    bt, discovered = binary_tree_from_dfs(G)  # O(n+m)

    i = 1
    nd = 1
    reached = []
    ed1 = None
    ed2 = None

    for p in bt.postorder():  # O(n)
        if bt.left(p) is not None:
            nd += discovered[bt.left(p).element()][2]
        if bt.right(p) is not None:
            nd += discovered[bt.right(p).element()][2]

        discovered[p.element()] = (discovered[p.element()], i, nd, 0, 0)

        i += 1                                                              # reset
        nd = 1

    for p in bt.postorder():  # O(n+m)
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

        reached.clear()                                                     # reset
        ed1 = None
        ed2 = None

    bridgeEdges = []
    for vertex in discovered:
        edge, number, nd, low, high = discovered[vertex]
        if edge is not None and high <= number and nd > (number - low):     # bridge condition
            bridgeEdges.append(edge)

    if len(bridgeEdges):
        return bridgeEdges
    else:
        return None


"""*******************************************MAIN*******************************************"""


G1 = Graph()

a = G1.insert_vertex("a")
b = G1.insert_vertex("b")
c = G1.insert_vertex("c")
d = G1.insert_vertex("d")
e = G1.insert_vertex("e")
f = G1.insert_vertex("f")
g = G1.insert_vertex("g")
G1.insert_edge(a, b)
G1.insert_edge(a, c)
G1.insert_edge(b, c)
G1.insert_edge(c, d)
G1.insert_edge(d, e)
G1.insert_edge(e, f)
G1.insert_edge(c, f)
G1.insert_edge(c, g)

G2 = Graph()

a = G2.insert_vertex("a")
b = G2.insert_vertex("b")
c = G2.insert_vertex("c")
d = G2.insert_vertex("d")
e = G2.insert_vertex("e")
f = G2.insert_vertex("f")
g = G2.insert_vertex("g")
h = G2.insert_vertex("h")
i = G2.insert_vertex("i")
G2.insert_edge(a, b)
G2.insert_edge(b, c)
G2.insert_edge(a, c)
G2.insert_edge(c, d)
G2.insert_edge(d, e)
G2.insert_edge(e, f)
G2.insert_edge(f, g)
G2.insert_edge(g, d)
G2.insert_edge(c, h)
G2.insert_edge(b, h)
G2.insert_edge(h, i)


bridgeEdges = bridge(G2)

if bridgeEdges is not None:
    for edge in bridgeEdges:
        print(edge)