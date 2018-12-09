from Progetto_4.Utilities import generateGraph, read_graph_from_file
import cProfile
import pstats



for i in range(50):

    m = 300 + i*10
    n = 50
    print('\033[1;31m_____________________________G\033[1;m',"(", n, ",", m, ")")

    print('\033[1;31m_____________________________min_vertex_cover\033[1;m')
    G = generateGraph(n, m)

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


G = read_graph_from_file("../Test_files/zachary_club.txt")
vertex_cover = []
cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
p = pstats.Stats('test')
p.files.pop(0)
p.print_stats(0)
print(len(vertex_cover))
