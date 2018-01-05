from es1_min_vertex_cover import MyGraph
import random

def knownGraphs(n):
    G = MyGraph()

    if (n == 1):
        a = G.insert_vertex("a")
        b = G.insert_vertex("b")
        c = G.insert_vertex("c")
        d = G.insert_vertex("d")
        e = G.insert_vertex("e")
        f = G.insert_vertex("f")
        g = G.insert_vertex("g")
        h = G.insert_vertex("h")
        i = G.insert_vertex("i")
        G.insert_edge(a, b)
        G.insert_edge(b, c)
        G.insert_edge(a, c)
        G.insert_edge(c, d)
        G.insert_edge(d, e)
        G.insert_edge(e, f)
        G.insert_edge(f, g)
        G.insert_edge(g, d)
        G.insert_edge(c, h)
        G.insert_edge(b, h)
        G.insert_edge(h, i)

        return G
    if (n == 2):
        a = G.insert_vertex("a")
        b = G.insert_vertex("b")
        c = G.insert_vertex("c")
        d = G.insert_vertex("d")
        e = G.insert_vertex("e")
        f = G.insert_vertex("f")
        g = G.insert_vertex("g")
        h = G.insert_vertex("h")
        i = G.insert_vertex("i")
        l = G.insert_vertex("l")
        m = G.insert_vertex("m")
        n = G.insert_vertex("n")
        o = G.insert_vertex("o")
        p = G.insert_vertex("p")
        q = G.insert_vertex("q")
        r = G.insert_vertex("r")
        s = G.insert_vertex("s")

        G.insert_edge(a, b)
        G.insert_edge(c, a)
        G.insert_edge(d, b)
        G.insert_edge(f, b)
        G.insert_edge(f, g)
        G.insert_edge(c, e)
        G.insert_edge(h, g)
        G.insert_edge(h, l)
        G.insert_edge(i, h)
        G.insert_edge(i, m)
        G.insert_edge(n, m)
        G.insert_edge(n, o)
        G.insert_edge(o, p)
        G.insert_edge(r, q)
        G.insert_edge(s, q)
        G.insert_edge(q, p)
        G.insert_edge(r, i)

        return G
    if (n == 3):
        a = G.insert_vertex("a")
        b = G.insert_vertex("b")
        c = G.insert_vertex("c")
        d = G.insert_vertex("d")
        e = G.insert_vertex("e")
        f = G.insert_vertex("f")
        g = G.insert_vertex("g")
        h = G.insert_vertex("h")
        i = G.insert_vertex("i")
        l = G.insert_vertex("l")
        m = G.insert_vertex("m")
        n = G.insert_vertex("n")

        G.insert_edge(a, b)
        G.insert_edge(b, c)
        G.insert_edge(d, b)
        G.insert_edge(d, c)
        G.insert_edge(a, m)
        G.insert_edge(a, l)
        G.insert_edge(c, e)
        G.insert_edge(d, f)
        G.insert_edge(i, e)
        G.insert_edge(l, i)
        G.insert_edge(n, i)
        G.insert_edge(m, n)
        G.insert_edge(m, l)
        G.insert_edge(n, h)
        G.insert_edge(h, f)
        G.insert_edge(h, g)
        G.insert_edge(g, f)
        G.insert_edge(e, g)

        return G

    return None


def generateGraph(n, m):
    G = MyGraph()
    l = []

    for i in range(n):
        l.append(G.insert_vertex(i))

    possible_edge = []
    all_edge = 0

    for i in range(n):
        for j in range(n):
            if i != j and i > j:
                possible_edge.append((i,j))
                all_edge += 1

    for j in range(m):
        index = random.randrange(0, len(possible_edge))
        n1, n2 = possible_edge.pop(index)
        G.insert_edge(l[n1], l[n2])

    return G