from Progetto_4.Utilities import generateGraph, read_graph_from_file
from Progetto_4.es1 import MyGraph
import cProfile
import pstats

"""
for i in range(50):

    m = 250 + i*15
    print('\033[1;31m_____________________________G\033[1;m',"( 50 ,", m, ")")

    print('\033[1;31m_____________________________min_vertex_cover\033[1;m')
    G = generateGraph(50, m)

    print("Random graph generated")

    vertex_cover = []
    cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
    p = pstats.Stats('test')
    p.files.pop(0)
    p.print_stats(0)
    print(len(vertex_cover))

    print('\033[1;31m_____________________________greedy_vertex_cover\033[1;m')

    vertex_cover = []
    cProfile.run("vertex_cover = G.greedy_vertex_cover()", "test")
    p = pstats.Stats('test')
    p.files.pop(0)
    p.print_stats(0)
    print(len(vertex_cover))
"""


G = read_graph_from_file("./Test_files/miserabili.txt")
vertex_cover = []
cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
p = pstats.Stats('test')
p.files.pop(0)
p.print_stats(0)
print(len(vertex_cover))





"""
G = MyGraph()
V = []

V.append(G.insert_vertex('a'))
V.append(G.insert_vertex('b'))
V.append(G.insert_vertex('c'))
V.append(G.insert_vertex('d'))
V.append(G.insert_vertex('e'))
V.append(G.insert_vertex('f'))
V.append(G.insert_vertex('g'))
V.append(G.insert_vertex('h'))
V.append(G.insert_vertex('i'))
V.append(G.insert_vertex('j'))
V.append(G.insert_vertex('k'))
V.append(G.insert_vertex('l'))
V.append(G.insert_vertex('m'))
V.append(G.insert_vertex('n'))
V.append(G.insert_vertex('o'))
V.append(G.insert_vertex('p'))
V.append(G.insert_vertex('q'))
V.append(G.insert_vertex('r'))
V.append(G.insert_vertex('s'))
V.append(G.insert_vertex('t'))
V.append(G.insert_vertex('u'))
V.append(G.insert_vertex('v'))
V.append(G.insert_vertex('w'))
V.append(G.insert_vertex('x'))
V.append(G.insert_vertex('y'))
V.append(G.insert_vertex('z'))


for i in range(len(V)):
    if i != 0:
        G.insert_edge(V[0],V[i])

for i in range(len(V)):
    if i != 0 and i != len(V) - 1:
        G.insert_edge(V[i],V[i + 1])

G.insert_edge(V[-1], V[1])

for i in range(len(V)):
    if i != 0 and (i != len(V) - 2 and i != len(V) - 1):
        G.insert_edge(V[i],V[i + 2])

vertex_cover = []
cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
p = pstats.Stats('test')
p.files.pop(0)
p.print_stats(0)
print(len(vertex_cover))
for v in vertex_cover:
    print(v)
"""